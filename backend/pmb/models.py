from datetime import date
from django.db import models
from uuid import uuid1

# Create your models here.

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    iban = models.CharField(max_length=34)
    amount = models.FloatField()
    due_date = models.DateField(default=date.today)
    variable_symbol = models.CharField(default='', max_length=10)
    specific_symbol = models.CharField(default='', max_length=10)
    constant_symbol = models.CharField(default='', max_length=4)
    payment_note = models.CharField(default='', max_length=99)
    beneficiary_name = models.CharField(default='', max_length=99)
    beneficiary_address1 = models.CharField(default='', max_length=99)
    beneficiary_address2 = models.CharField(default='', max_length=99)
