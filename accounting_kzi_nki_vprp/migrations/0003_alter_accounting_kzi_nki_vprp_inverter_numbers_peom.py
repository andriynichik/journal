# Generated by Django 5.0.6 on 2024-05-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_kzi_nki_vprp', '0002_alter_accounting_kzi_nki_vprp_accounting_kzi_nki_sign_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting_kzi_nki_vprp',
            name='inverter_numbers_peom',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]