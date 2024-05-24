from .models import  Accounting_KZI_NKI_KNED_DIIA_RESERVE_SITE
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import Accounting_KZI_NKI_KNED_DIIA_RESERVE_SITEForm
from django.utils.timezone import now
from django.contrib import messages

@login_required
def Accounting_KZI_NKI_KNED_DIIA_MAIN_SITE_List(request):
    transactions = Accounting_KZI_NKI_KNED_DIIA_RESERVE_SITE.objects.all().select_related()

    data = {'transactions': transactions}
    return render(request, 'app/accounting_kzi_nki_kned_diia_reserve_site/accounting_kzi_nki_kned_diia_reserve_site_list.html', context=data)


@login_required
def Accounting_KZI_NKI_KNED_DIIA_MAIN_SITE_Create(request):
    data = {}
    form = Accounting_KZI_NKI_KNED_DIIA_RESERVE_SITEForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            log = Accounting_KZI_NKI_KNED_DIIA_RESERVE_SITE(tool_kzi_type = form.cleaned_data['tool_kzi_type'],
                                       tool_kzi_number= form.cleaned_data['tool_kzi_number'],
                                       nki_type = form.cleaned_data['nki_type'],
                                       nki_number = form.cleaned_data['nki_number'],
                                       act_commissioning_kzi_facilities=form.cleaned_data['act_commissioning_kzi_facilities'],
                                               date_taking_account_kzi_nki=form.cleaned_data['date_taking_account_kzi_nki'],
                                               inverter_numbers_peom=form.cleaned_data['inverter_numbers_peom'],
                                               note_romove_means_sign=form.cleaned_data['note_romove_means_sign'],
                                       created=now())
            log.save()
            messages.success(request, 'Запис успішно створено')
            return redirect('accounting_kzi_nki_kned_diia_reserve_site/list')

        else:
            error = dict()
            for field in form.errors:
                error[field] = form.errors[field].as_text()
            messages.error(request, 'Помилка заповнення даних'+str(error))



    data['form'] = form
    return render(request, 'app/accounting_kzi_nki_kned_diia_reserve_site/accounting_kzi_nki_kned_diia_reserve_site_create.html', data)




@login_required
def Accounting_KZI_NKI_KNED_DIIA_MAIN_SITE_Edit(request, pk_id):
    if request.method == "POST":
        form = Accounting_KZI_NKI_KNED_DIIA_RESERVE_SITEForm(request.POST)
        if form.is_valid():
            Accounting_KZI_NKI_KNED_DIIA_RESERVE_SITE.objects.filter(pk=pk_id).update(
                tool_kzi_type=form.cleaned_data['tool_kzi_type'],
                tool_kzi_number=form.cleaned_data['tool_kzi_number'],
                nki_type=form.cleaned_data['nki_type'],
                nki_number=form.cleaned_data['nki_number'],
                act_commissioning_kzi_facilities=form.cleaned_data['act_commissioning_kzi_facilities'],
                date_taking_account_kzi_nki=form.cleaned_data['date_taking_account_kzi_nki'],
                inverter_numbers_peom=form.cleaned_data['inverter_numbers_peom'],
                note_romove_means_sign=form.cleaned_data['note_romove_means_sign'],
            )
            messages.success(request, 'Дані змінено')
            return redirect('/accounting_kzi_nki_kned_diia_reserve_site/list')
        else:
            messages.error(request, 'Не вірно заповнена форма')

    jurnal = Accounting_KZI_NKI_KNED_DIIA_RESERVE_SITE.objects.get(pk=pk_id)
    form = Accounting_KZI_NKI_KNED_DIIA_RESERVE_SITEForm(instance=jurnal)
    if jurnal.accounting_kzi_nki_sign or jurnal.get_remedy_kzi_nki_sign or jurnal.note_return_means_sign:
        form.fields['tool_kzi_type'].widget.attrs['readonly'] = 'readonly'
        form.fields['tool_kzi_type'].widget.attrs['style']= 'pointer-events: none;'
        form.fields['tool_kzi_number'].widget.attrs['readonly']= 'readonly'
        form.fields['tool_kzi_number'].widget.attrs['style'] = 'pointer-events: none;'
        form.fields['nki_type'].widget.attrs['readonly']= 'readonly'
        form.fields['nki_type'].widget.attrs['style'] = 'pointer-events: none;'
        form.fields['nki_number'].widget.attrs['readonly']= 'readonly'
        form.fields['nki_number'].widget.attrs['style'] = 'pointer-events: none;'
        form.fields['act_commissioning_kzi_facilities'].widget.attrs['readonly'] = 'readonly'
        form.fields['act_commissioning_kzi_facilities'].widget.attrs['style'] = 'pointer-events: none;'
        form.fields['date_taking_account_kzi_nki'].widget.attrs['readonly'] = 'readonly'
        form.fields['date_taking_account_kzi_nki'].widget.attrs['style'] = 'pointer-events: none;'

    context = {'jurnal' : jurnal, 'form': form}
    return render(request, 'app/accounting_kzi_nki_kned_diia_reserve_site/accounting_kzi_nki_kned_diia_reserve_site_edit.html', context)

