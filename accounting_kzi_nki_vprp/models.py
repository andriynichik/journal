from app.models import SignInvate
from django.db import models

TOOL_KZI_CHOICE = (
    (1, '"Електронний ключ" Кристал-1'),
    (2, '"Електронний ключ" Алмаз-1К')
)

NKI_TYPE_CHOICE = (
    (1, 'Електронний ключ'),
    (2, 'Мережний криптомодуль'),
    (3, 'Шлюз захисту')
)

class Accounting_KZI_NKI_VPRP(models.Model):

    id = models.AutoField(primary_key=True)
    tool_kzi_type = models.SmallIntegerField(choices=TOOL_KZI_CHOICE)
    tool_kzi_number = models.IntegerField()
    nki_type = models.SmallIntegerField(choices=NKI_TYPE_CHOICE)
    nki_number = models.IntegerField()
    act_commissioning_kzi_facilities = models.CharField(max_length=128)
    date_taking_account_kzi_nki = models.DateField()
    inverter_numbers_peom =  models.CharField(max_length=128)
    accounting_kzi_nki_sign = models.ForeignKey(SignInvate, on_delete=models.CASCADE, related_name='accounting_kzi_nki_vprp_sign', null=True)
    get_remedy_kzi_nki_sign = models.ForeignKey(SignInvate, on_delete=models.CASCADE, related_name='get_remedy_kzi_nki_vprp_sign', null=True)
    note_return_means_sign = models.ForeignKey(SignInvate, on_delete=models.CASCADE, related_name='note_return_means_vprp_sign', null=True)
    note_romove_means_sign = models.CharField(max_length=128, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField( auto_now=True, editable=True, null=True, blank=True)


    class Meta:
        db_table = 'accounting_kzi_nki_vprp'





