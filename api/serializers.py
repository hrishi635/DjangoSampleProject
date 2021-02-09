from rest_framework import serializers;
from .models import Transaction
from datetime import date,datetime
from rest_framework.exceptions import ValidationError

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=['item_id','quantity','expiry_date','mrp','lot_number','transaction_id','transaction_type','transaction_ts']

    def validate(self,data):
        error = []
        transaction_type=data.get('transaction_type')
        if transaction_type <1 or transaction_type >4 :
            error.append(ValidationError('transaction_type must be between 1-4',code=400))

        mrp=data.get('mrp')
        if mrp <=0 :
            error.append(ValidationError('Not a valid mrp',code=400))

        quantity=data.get('quantity')
        if quantity <= 0 :
            error.append(ValidationError('Not a valid quantity',code=400))
        
        expiry_date=data.get('expiry_date')
        if expiry_date < date.today() :
            error.append(ValidationError('Invalid expiry_date',code=400))

        # transaction_ts=data.get('transaction_ts')
        # date=transaction_ts.date()
        # time=transaction_ts.time()
        # if date.today() > date :
        #     raise serializers.ValidationError('transaction_ts field cannot be exceeding current time') 
        # if date.today() == date and datetime.time() >= time :
        #     raise serializers.ValidationError('transaction_ts field cannot be exceeding current time')

        if error:
            raise ValidationError(error)
        return data
