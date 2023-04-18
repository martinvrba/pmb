from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "amount",
        "beneficiary_address1",
        "beneficiary_address2",
        "beneficiary_name",
        "constant_symbol",
        "due_date",
        "iban",
        "id",
        "payment_note",
        "specific_symbol",
        "timestamp",
        "variable_symbol",
    )


# Register your models here.

admin.site.register(Payment, PaymentAdmin)
