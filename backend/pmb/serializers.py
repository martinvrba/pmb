from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
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
