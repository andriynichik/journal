# Generated by Django 5.0.3 on 2024-05-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record_seals_stamp_safe', '0004_alter_recordsealsstampsafe_security_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordsealsstampsafe',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]