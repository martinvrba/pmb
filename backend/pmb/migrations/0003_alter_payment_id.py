# Generated by Django 4.2 on 2023-04-17 16:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("pmb", "0002_remove_payment_cs_remove_payment_ss_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid1, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]