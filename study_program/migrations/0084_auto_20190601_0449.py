# Generated by Django 2.1.2 on 2019-05-31 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0083_auto_20190601_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 1, 4, 49, 24, 11969)),
        ),
        migrations.AlterField(
            model_name='issue',
            name='sending_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 4, 49, 24, 11969)),
        ),
    ]