# Generated by Django 5.0.6 on 2024-05-12 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordSealsStampSafe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numbers_imprint_individual_seal', models.TextField()),
                ('number_safe', models.TextField()),
                ('registration_issue_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author_position_signature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='signature', to='app.signinvate')),
                ('security_signature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='signature_admin_security', to='app.signinvate')),
            ],
            options={
                'db_table': 'record_seals_stamp_safe',
            },
        ),
    ]
