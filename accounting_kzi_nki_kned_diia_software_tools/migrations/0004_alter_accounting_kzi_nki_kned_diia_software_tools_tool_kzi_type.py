# Generated by Django 5.0.6 on 2024-05-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_kzi_nki_kned_diia_software_tools', '0003_alter_accounting_kzi_nki_kned_diia_software_tools_accounting_kzi_nki_sign_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting_kzi_nki_kned_diia_software_tools',
            name='tool_kzi_type',
            field=models.SmallIntegerField(choices=[(1, 'Програмний комплекс взаємодії віддалених автоматизованих робочих місць пунктів реєстрації послуг Mobile ID на територіях центрів обслуговування клієнт'), (2, 'Програмний комплекс користувача центру сертифікації ключів"ІІТ Користувач ЦСК-1"з комплектом багатоплатформенних криптографічних бібліотек та додатків'), (3, 'Програмний комплекс віддаленого управління шлюзами захисту "ІІТ Захист з`єднань-2. Віддалене управління шлюзами захисту'), (4, 'Програмний комплекс ЦСК "ІІТ ЦСК-1"'), (5, 'Програмний комплекс користувача ЦСК "ІІТ Користувач ЦСК-1"'), (6, 'Програмний комплекс клієнта захисту мережних з`єднань "ІІТ Захист з`єднань-2. Клієнт захисту з`єднань"')]),
        ),
    ]
