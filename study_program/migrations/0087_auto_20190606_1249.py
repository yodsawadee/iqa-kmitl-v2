# Generated by Django 2.0 on 2019-06-06 05:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0086_auto_20190602_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 6, 12, 49, 25, 675010)),
        ),
        migrations.AlterField(
            model_name='issue',
            name='sending_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 6, 12, 49, 25, 676010)),
        ),
    ]
