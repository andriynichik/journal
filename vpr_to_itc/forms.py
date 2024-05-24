from django import forms

from .models import VPRPTOITC

class VPRPTOITCForm(forms.ModelForm):

    numbers_jornal = forms.CharField(
        label="№",
        widget=forms.TextInput( attrs={
                "placeholder": "№",
                "class": "form-control"
            }),
    )

    denotation_vprp_basis = forms.CharField(
        label="Позначення ВПРП - Підстава",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Позначення ВПРП - Підстава",
                "class": "form-control"
            }
        ))

    denotation_vprp_date = forms.DateField(required=False ,
                                  label="Позначення ВПРП - Дата", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    connection_information_vprp_basis = forms.CharField(
        required=False,
        label="Відомості про відключення ВПРП- Підстава",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Відомості про підключення ВПРП - Підстава",
                "class": "form-control"
            }
        ))

    connection_information_vprp_date = forms.DateField(required=False ,
                                  label="Відомості про відключення ВПРП - Дата", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))



    class Meta:
        model = VPRPTOITC
        fields = ('numbers_jornal', 'denotation_vprp_basis', 'denotation_vprp_date', 'connection_information_vprp_basis',
                  'connection_information_vprp_date')