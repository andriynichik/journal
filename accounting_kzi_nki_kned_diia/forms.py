from django import forms

from .models import Accounting_KZI_NKI_KNED_DIIA, TOOL_KZI_CHOICE, NKI_TYPE_CHOICE

class Accounting_KZI_NKI_KNED_DIIAForm(forms.ModelForm):
    tool_kzi_type = forms.CharField(
        label="Назва засобу КЗІ",
        widget=forms.Select( attrs={

                "class": "form-control"
            }, choices=TOOL_KZI_CHOICE),
    )
    tool_kzi_number = forms.IntegerField(
        label="Заводський номер засобу КЗІ",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Заводський номер засобу КЗІ",
                "class": "form-control"
            }
        ))

    nki_type = forms.CharField(
        label="Тип НКІ",
        widget=forms.Select(

            attrs={
                "class": "form-control"
            }, choices=NKI_TYPE_CHOICE),
    )
    nki_number = forms.IntegerField(
        label="Заводський номер засобу НКІ",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Обліковий номер НКІ",
                "class": "form-control"
            }
        ))

    act_commissioning_kzi_facilities = forms.CharField(
        label="Акт організаційно-розпорядчого характеру щодо введення в експлуатацію засобів КЗІ",
        widget=forms.TextInput( attrs={
                "placeholder": "Акт організаційно-розпорядчого характеру щодо введення в експлуатацію засобів КЗІ",
                "class": "form-control"
            }),
    )

    date_taking_account_kzi_nki = forms.DateField(required=False ,
                                  label="Дата взяття на облік засобів КЗІ та НКІ", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    inverter_numbers_peom = forms.CharField(
        label="Інвертарні номери ПЕОМ, на яких встановлено (проінстальовано) програмні засоби КЗІ",
        widget=forms.TextInput( attrs={
                "placeholder": "Інвертарні номери ПЕОМ, на яких встановлено (проінстальовано) програмні засоби КЗІ",
                "class": "form-control"
            }),
    )

    note_romove_means_sign = forms.CharField(
        label="Відмітка про знищення засобу КЗІ та НКІ (дата, підпис відповідальної особи)",
        widget=forms.TextInput( attrs={
                "placeholder": "Відмітка про знищення засобу КЗІ та НКІ",
                "class": "form-control"
            }),
    )


    class Meta:
        model = Accounting_KZI_NKI_KNED_DIIA
        fields = ('tool_kzi_type', 'tool_kzi_number', 'nki_type', 'nki_number',
                  'act_commissioning_kzi_facilities', 'date_taking_account_kzi_nki', 'inverter_numbers_peom',
                  'note_romove_means_sign' )