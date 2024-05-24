from app.models import SignInvate
from django.db import models

TOOL_KZI_CHOICE = (
    (1, 'Програмний комплекс взаємодії віддалених автоматизованих робочих місць пунктів реєстрації послуг Mobile ID на територіях центрів обслуговування клієнт'),
    (2, 'Програмний комплекс користувача центру сертифікації ключів"ІІТ Користувач ЦСК-1"з комплектом багатоплатформенних криптографічних бібліотек та додатків'),
    (3, 'Програмний комплекс віддаленого управління шлюзами захисту "ІІТ Захист з`єднань-2. Віддалене управління шлюзами захисту'),
    (4, 'Програмний комплекс ЦСК "ІІТ ЦСК-1"'),
    (5, 'Програмний комплекс користувача ЦСК "ІІТ Користувач ЦСК-1"'),
    (6, 'Програмний комплекс клієнта захисту мережних з`єднань "ІІТ Захист з`єднань-2. Клієнт захисту з`єднань"'),
)

NKI_TYPE_CHOICE = (
    (1, 'Електронний ключ'),
    (2, 'Мережний криптомодуль'),
    (3, 'Шлюз захисту')
)

class Accounting_KZI_NKI_KNED_DIIA_SOFTWARE_TOOLS(models.Model):

    id = models.AutoField(primary_key=True)

    tool_kzi_type = models.SmallIntegerField(choices=TOOL_KZI_CHOICE)
    tool_kzi_number = models.IntegerField()
    nki_type = models.SmallIntegerField(choices=NKI_TYPE_CHOICE)
    nki_number = models.IntegerField()
    act_commissioning_kzi_facilities = models.CharField(max_length=128)
    date_taking_account_kzi_nki = models.DateField()
    inverter_numbers_peom =  models.CharField(max_length=128, null=True, blank=True)
    accounting_kzi_nki_sign = models.ForeignKey(SignInvate, on_delete=models.SET_NULL,
                                                related_name='accounting_kzi_nki_kned_diia_software_tools', null=True)
    get_remedy_kzi_nki_sign = models.ForeignKey(SignInvate, on_delete=models.SET_NULL,
                                                related_name='get_remedy_kzi_nki_sign_software_tools', null=True)
    note_return_means_sign = models.ForeignKey(SignInvate, on_delete=models.SET_NULL,
                                               related_name='note_return_means_sign_software_tools', null=True)
    note_romove_means_sign = models.CharField(max_length=128, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=None, editable=True, null=True, blank=True)

    class Meta:
        db_table = 'accounting_kzi_nki_kned_diia_software_tools'



