# Generated by Django 3.1.7 on 2021-09-03 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0004_investment_request_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='ha_payment_status',
            field=models.BooleanField(default=False),
        ),
    ]