# Generated by Django 5.0.7 on 2024-12-28 21:00

import cloudinary.models
import exchange.services.transaction_service
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='network',
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount_in_crypto',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount_in_ngn',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount_in_usd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='receipt',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='receipt'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='ref',
            field=models.CharField(default=exchange.services.transaction_service.generate_trxn_ref, max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='rate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]