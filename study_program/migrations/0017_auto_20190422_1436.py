# Generated by Django 2.0.2 on 2019-04-22 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0016_auto_20190422_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 22, 14, 36, 16, 221239)),
        ),
        migrations.AlterField(
            model_name='issue',
            name='sending_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 22, 14, 36, 16, 225228)),
        ),
    ]