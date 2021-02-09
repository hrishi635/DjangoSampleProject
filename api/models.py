# Create your models here.

from django.db import models
 
# Create your models here.

class Transaction(models.Model):
    item_id=models.CharField(max_length=30)
    quantity=models.IntegerField()
    expiry_date=models.DateField()
    mrp=models.IntegerField()
    lot_number=models.IntegerField()
    transaction_id=models.CharField(max_length=30,unique=True)
    transaction_type=models.IntegerField()
    transaction_ts=models.DateTimeField()
    request_ts=models.DateTimeField(auto_now_add=True)
