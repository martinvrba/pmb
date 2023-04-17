from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'iban',
        'amount',
        'due_date',
        'variable_symbol',
        'specific_symbol',
        'constant_symbol',
        'payment_note',
        'beneficiary_name',
        'beneficiary_address1',
        'beneficiary_address2',
    )

# Register your models here.

admin.site.register(Payment, PaymentAdmin)
