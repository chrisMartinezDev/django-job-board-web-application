# Generated by Django 5.0.1 on 2024-02-06 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_jobBoard', '0004_application_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_jobBoard.job'),
        ),
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
