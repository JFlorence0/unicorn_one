# Generated by Django 4.0.4 on 2022-06-06 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vareaze', '0010_remove_contract_text_alter_contract_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_added',
            field=models.DateTimeField(default='2022-06-05'),
        ),
    ]
