# Generated by Django 3.1.5 on 2021-04-02 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_transaction_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
