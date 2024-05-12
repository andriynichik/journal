# Generated by Django 5.0.6 on 2024-05-12 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounting_KZI_NKI_VPRP',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tool_kzi_type', models.SmallIntegerField(choices=[(1, '"Електронний ключ" Кристал-1'), (2, '"Електронний ключ" Алмаз-1К')])),
                ('tool_kzi_number', models.IntegerField()),
                ('nki_type', models.SmallIntegerField(choices=[(1, 'Електронний ключ'), (2, 'Мережний криптомодуль'), (3, 'Шлюз захисту')])),
                ('nki_number', models.IntegerField()),
                ('act_commissioning_kzi_facilities', models.CharField(max_length=128)),
                ('date_taking_account_kzi_nki', models.DateField()),
                ('inverter_numbers_peom', models.CharField(max_length=128)),
                ('note_romove_means_sign', models.CharField(blank=True, max_length=128, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('accounting_kzi_nki_sign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounting_kzi_nki_vprp_sign', to='app.signinvate')),
                ('get_remedy_kzi_nki_sign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_remedy_kzi_nki_vprp_sign', to='app.signinvate')),
                ('note_return_means_sign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_return_means_vprp_sign', to='app.signinvate')),
            ],
            options={
                'db_table': 'accounting_kzi_nki_vprp',
            },
        ),
    ]