from datetime import date
from django.db import models
from uuid import uuid1

# Create your models here.


class Payment(models.Model):
    amount = models.FloatField()
    beneficiary_address1 = models.CharField(blank=True, default="", max_length=99)
    beneficiary_address2 = models.CharField(blank=True, default="", max_length=99)
    beneficiary_name = models.CharField(blank=True, default="", max_length=99)
    constant_symbol = models.CharField(blank=True, default="", max_length=4)
    due_date = models.DateField(blank=True, default=date.today)
    iban = models.CharField(max_length=34)
    id = models.UUIDField(default=uuid1, editable=False, primary_key=True)
    payment_note = models.CharField(blank=True, default="", max_length=99)
    specific_symbol = models.CharField(blank=True, default="", max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    variable_symbol = models.CharField(blank=True, default="", max_length=10)
