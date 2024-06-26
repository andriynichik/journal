# Generated by Django 5.0.6 on 2024-05-17 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_kzi_nki_vprp', '0001_initial'),
        ('app', '0003_useragreement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting_kzi_nki_vprp',
            name='accounting_kzi_nki_sign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accounting_kzi_nki_vprp_sign', to='app.signinvate'),
        ),
        migrations.AlterField(
            model_name='accounting_kzi_nki_vprp',
            name='get_remedy_kzi_nki_sign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='get_remedy_kzi_nki_vprp_sign', to='app.signinvate'),
        ),
        migrations.AlterField(
            model_name='accounting_kzi_nki_vprp',
            name='note_return_means_sign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='note_return_means_vprp_sign', to='app.signinvate'),
        ),
    ]
