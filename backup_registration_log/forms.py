from django import forms
from.models import BackupRegistrationLog

class BackupRegistrationLogForm(forms.ModelForm):
    # np = forms.CharField(label="НП", widget=forms.TextInput(attrs={'class': 'form-control'}))
    number_device_beckup_info = forms.CharField(label="№ НОСІЯ ІНФОРМАЦІЇ З РЕЗЕРВНОЮ КОПІЄЮ", widget=forms.TextInput(attrs={'class': 'form-control'}))

    # date_created = forms.DateField(label="Фактична дата стоворення")
    class Meta:
        model = BackupRegistrationLog
        fields = [ 'number_device_beckup_info']