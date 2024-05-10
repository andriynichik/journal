# Generated by Django 5.0.3 on 2024-05-10 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_signinvate_sing'),
        ('backup_registration_log', '0004_remove_backupregistrationlog_date_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backupregistrationlog',
            name='user_sign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='signature_backup', to='app.signinvate'),
        ),
    ]