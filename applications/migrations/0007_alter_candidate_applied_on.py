# Generated by Django 4.1.1 on 2022-10-08 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0006_rename_fname_candidate_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='applied_on',
            field=models.DateField(default=datetime.datetime(2022, 10, 8, 13, 5, 15, 545948, tzinfo=datetime.timezone.utc)),
        ),
    ]