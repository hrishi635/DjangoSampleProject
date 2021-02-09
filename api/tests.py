import json
from django.test import TestCase,Client
from .models import Transaction
from .serializers import TransactionSerializer
from django.urls import reverse

client=Client()

class createNewTransaction(TestCase):
    def setUp(self):
        self.request_valid_transaction = {
            'item_id': 'pepsi',
            'quantity': 10,
            'expiry_date': '2022-10-02',
            'mrp': 85,
            'lot_number':30,
            'transaction_id':'1',
            'transaction_type':'4',
            'transaction_ts':'2021-01-10'
        }
        self.request_missing_quantity = {
            'item_id': 'pepsi',
            'expiry_date': '2022-10-22',
            'mrp': 85,
            'lot_number':30,
            'transaction_id':'1',
            'transaction_type':'12',
            'transaction_ts':'2021-02-04'

        }

        self.request_empty_quantity = {
            'item_id': 'pepsi',
            'quantity':'',
            'expiry_date': '2022-10-21',
            'mrp': 85,
            'lot_number':30,
            'transaction_id':'1',
            'transaction_type':'12',
            'transaction_ts':'2021-01-10'

        }

        self.request_invalid_expiry_date={
            'item_id': 'pepsi',
            'quantity':'14',
            'expiry_date': '2020-10-13',
            'mrp': 85,
            'lot_number':30,
            'transaction_id':'1',
            'transaction_type':'12',
            'transaction_ts':'2021-02-05'
        }


    def test_request_valid_transaction(self):
        response=client.post(
            reverse('addTransaction'),
            data=json.dumps(self.request_valid_transaction),
            content_type='application/json'
        )
        self.assertEqual(response.status_code,201)

    def test_request_missing_quantity(self):
        response=client.post(
            reverse('addTransaction'),
            data=json.dumps(self.request_missing_quantity),
            content_type='application/json'
        )
        self.assertEqual(response.status_code,400)
        
    def test_request_empty_quantity(self):
        response=client.post(
            reverse('addTransaction'),
            data=json.dumps(self.request_empty_quantity),
            content_type='application/json'
        )
        self.assertEqual(response.status_code,400)

    def test_request_invalid_expiry_date(self):
        response=client.post(
            reverse('addTransaction'),
            data=json.dumps(self.request_invalid_expiry_date),
            content_type='application/json'
        )
        self.assertEqual(response.status_code,400)
# Create your tests here.
