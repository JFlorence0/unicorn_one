# Generated by Django 4.0.4 on 2022-06-04 13:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vareaze', '0002_alter_contract_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 13, 22, 15, 316715, tzinfo=utc)),
        ),
    ]