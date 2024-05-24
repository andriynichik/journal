from django import forms

from .models import KeyDataLog, OPERATION_TYPE_CHOICE

class KeyDataLogForm(forms.ModelForm):

    operation_type = forms.CharField(
        label="Тип операції з ключовими даними",
        widget=forms.Select( attrs={

                "class": "form-control"
            }, choices=OPERATION_TYPE_CHOICE),
    )
    date_time = forms.DateField(required=False ,
                                  label="Дата", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    data_type = forms.CharField(
        label="Тип ключових даних",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Тип ключових даних",
                "class": "form-control"
            }
        ))
    number_document = forms.CharField(
        required=False,
        label="Обл.№ ключового документу",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Обл.№ ключового документ",
                "class": "form-control"
            }
        ))

    notes = forms.CharField(
        required=False,
        label="Примітки",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Примітки",
                "class": "form-control"
            }
        ))


    class Meta:
        model = KeyDataLog
        fields = (
            'operation_type', 'date_time', 'data_type', 'number_document',
            'notes'
        )