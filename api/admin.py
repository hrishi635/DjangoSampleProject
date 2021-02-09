from django.contrib import admin

# Register your models here.
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['id','item_id','quantity','expiry_date','mrp','lot_number','transaction_id','transaction_type','transaction_ts','request_ts']
