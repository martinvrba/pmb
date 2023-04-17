# Generated by Django 4.2 on 2023-04-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pmb", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="cs",
        ),
        migrations.RemoveField(
            model_name="payment",
            name="ss",
        ),
        migrations.RemoveField(
            model_name="payment",
            name="vs",
        ),
        migrations.AddField(
            model_name="payment",
            name="constant_symbol",
            field=models.CharField(default="", max_length=4),
        ),
        migrations.AddField(
            model_name="payment",
            name="specific_symbol",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AddField(
            model_name="payment",
            name="variable_symbol",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="payment",
            name="beneficiary_address1",
            field=models.CharField(default="", max_length=99),
        ),
        migrations.AlterField(
            model_name="payment",
            name="beneficiary_address2",
            field=models.CharField(default="", max_length=99),
        ),
        migrations.AlterField(
            model_name="payment",
            name="beneficiary_name",
            field=models.CharField(default="", max_length=99),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_note",
            field=models.CharField(default="", max_length=99),
        ),
    ]
