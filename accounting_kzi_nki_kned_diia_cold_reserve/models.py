from authentication.models import User
from app.models import SignInvate
from django.db import models

TOOL_KZI_CHOICE = (
    (1, 'Шлюз захисту "Бар`єр-301"'),
    (2, 'Мережевий IP-шифратор "Канал-401"'),
    (3, 'Мережний криптомодуль "Гряда-301" мікропристрій'),
    (4, 'Мережний криптомодуль "Гряда-301" ВП'),
    (5, '"Електронний ключ" Алмаз-1К'),
    (6, '"Електронний ключ" Кристал-1'),
)

NKI_TYPE_CHOICE = (
    (1, 'Електронний ключ'),
    (2, 'Мережний криптомодуль'),
    (3, 'Шлюз захисту')
)

class Accounting_KZI_NKI_KNED_DIIA_COLD_RESERVE(models.Model):

    id = models.AutoField(primary_key=True)
    tool_kzi_type = models.SmallIntegerField(choices=TOOL_KZI_CHOICE)
    tool_kzi_number = models.IntegerField()
    nki_type = models.SmallIntegerField(choices=NKI_TYPE_CHOICE)
    nki_number = models.IntegerField()
    act_commissioning_kzi_facilities = models.CharField(max_length=128)
    date_taking_account_kzi_nki = models.DateField()
    inverter_numbers_peom =  models.CharField(max_length=128, null=True, blank=True)
    accounting_kzi_nki_sign = models.ForeignKey(SignInvate, on_delete=models.SET_NULL, related_name='accounting_kzi_nki_sign_cold_reserve', null=True)
    get_remedy_kzi_nki_sign = models.ForeignKey(SignInvate, on_delete=models.SET_NULL, related_name='get_remedy_kzi_nki_sign_cold_reserve', null=True)
    note_return_means_sign = models.ForeignKey(SignInvate, on_delete=models.SET_NULL, related_name='note_return_means_sign_cold_reserve', null=True)
    note_romove_means_sign = models.CharField(max_length=128, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=None, editable=True, null=True, blank=True)

    class Meta:
        db_table = 'accounting_kzi_nki_kned_diia_cold_reserve'




from django.db import models

# Create your models here.
