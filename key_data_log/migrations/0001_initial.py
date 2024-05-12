# Generated by Django 5.0.6 on 2024-05-12 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyDataLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('operation_type', models.IntegerField(choices=[(1, 'Генерація'), (2, 'Формування'), (3, 'Знищення'), (4, 'Скасування'), (5, 'Відновлення'), (6, 'Резервне копіювання')])),
                ('date_time', models.DateTimeField()),
                ('data_type', models.CharField(max_length=128)),
                ('number_document', models.CharField(max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('admin_sign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_sign_key_data', to='app.signinvate')),
                ('user_sign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_sign_key_data', to='app.signinvate')),
            ],
            options={
                'db_table': 'key_data_log',
            },
        ),
    ]
