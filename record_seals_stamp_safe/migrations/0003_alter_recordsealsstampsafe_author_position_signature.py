# Generated by Django 5.0.3 on 2024-05-09 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_signinvate_sing'),
        ('record_seals_stamp_safe', '0002_remove_recordsealsstampsafe_author_admin_security_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordsealsstampsafe',
            name='author_position_signature',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='signature', to='app.signinvate'),
        ),
    ]