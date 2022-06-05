# Generated by Django 4.0.4 on 2022-06-04 22:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vareaze', '0008_alter_contract_date_added_alter_contract_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 22, 47, 0, 337627, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]