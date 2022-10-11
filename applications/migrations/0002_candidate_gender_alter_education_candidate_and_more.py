# Generated by Django 4.1.1 on 2022-09-09 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='gender',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='education',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='applications.candidate'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='applications.candidate'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='applications.candidate'),
        ),
    ]