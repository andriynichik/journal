from django import forms
from.models import RecordSealsStampSafe

class RecordSealsStampSafeForm(forms.ModelForm):

    numbers_imprint_individual_seal = forms.CharField(
        label="№, відбиток індивідульної печатки",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    number_safe = forms.CharField(
        label="№ сейфа",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    registration_issue_date = forms.DateField(label="Дата видачі, реєстрації",
                                              widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    return_date = forms.DateField(required=False ,
                                  label="Дата повернення індивідуальної печатки та/або сеффового ключа", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))


    notes = forms.CharField(
        required=False,
        label="Нотатка",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )




    # date_created = forms.DateField(label="Фактична дата стоворення")
    class Meta:
        model = RecordSealsStampSafe
        fields = [ 'numbers_imprint_individual_seal', 'number_safe', 'registration_issue_date', 'return_date', 'notes' ]