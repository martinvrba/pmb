from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'amount',
            'beneficiary_address1',
            'beneficiary_address2',
            'beneficiary_name',
            'constant_symbol',
            'due_date',
            'iban',
            'id',
            'payment_note',
            'specific_symbol',
            'timestamp',
            'variable_symbol',
        )
