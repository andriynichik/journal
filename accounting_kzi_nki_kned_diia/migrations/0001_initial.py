# Generated by Django 5.0.6 on 2024-05-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounting_KZI_NKI_KNED_DIIA',
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
            ],
            options={
                'db_table': 'accounting_kzi_nki_kned_diia',
            },
        ),
    ]
