# Generated by Django 5.0.3 on 2024-05-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signinvate',
            name='sing',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
