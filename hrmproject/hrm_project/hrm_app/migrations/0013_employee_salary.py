# Generated by Django 5.0.4 on 2024-05-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm_app', '0012_employee_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.FloatField(default=0),
        ),
    ]
