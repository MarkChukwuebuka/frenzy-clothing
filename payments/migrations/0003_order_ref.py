# Generated by Django 5.0.7 on 2024-12-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_bankaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
