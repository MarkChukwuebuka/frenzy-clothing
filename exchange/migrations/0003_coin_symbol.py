# Generated by Django 5.0.7 on 2024-12-28 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_remove_transaction_amount_remove_transaction_network_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='symbol',
            field=models.CharField(choices=[('bitcoin', 'Bitcoin'), ('ethereum', 'Ethereum'), ('tether', 'Tether')], default='tether', max_length=255),
        ),
    ]