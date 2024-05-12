# Generated by Django 5.0.6 on 2024-05-12 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting_kzi_nki_kned_diia_software_tools', '0001_initial'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounting_kzi_nki_kned_diia_software_tools',
            name='accounting_kzi_nki_sign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounting_kzi_nki_kned_diia_software_tools', to='app.signinvate'),
        ),
        migrations.AddField(
            model_name='accounting_kzi_nki_kned_diia_software_tools',
            name='get_remedy_kzi_nki_sign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_remedy_kzi_nki_sign_software_tools', to='app.signinvate'),
        ),
        migrations.AddField(
            model_name='accounting_kzi_nki_kned_diia_software_tools',
            name='note_return_means_sign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_return_means_sign_software_tools', to='app.signinvate'),
        ),
    ]
