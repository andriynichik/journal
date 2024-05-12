from .models import  Accounting_KZI_NKI_VPRP
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import Accounting_KZI_NKI_VPRPForm
from django.utils.timezone import now
from django.contrib import messages

@login_required
def Accounting_KZI_NKI_VPRPList(request):
    transactions = Accounting_KZI_NKI_VPRP.objects.all().select_related()

    data = {'transactions': transactions}
    return render(request, 'app/accounting_kzi_nki_kned_vprp/accounting_kzi_nki_vprp_list.html', context=data)


@login_required
def Accounting_KZI_NKI_VPRPCreate(request):
    data = {}
    form = Accounting_KZI_NKI_VPRPForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            log = Accounting_KZI_NKI_VPRP(tool_kzi_type = form.cleaned_data['tool_kzi_type'],
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
            return redirect('accounting_kzi_nki_vprp/list')
    data['form'] = form
    return render(request, 'app/accounting_kzi_nki_kned_vprp/accounting_kzi_nki_vprp_create.html', data)




@login_required
def Accounting_KZI_NKI_VPRPEdit(request, pk_id):
    if request.method == "POST":
        form = Accounting_KZI_NKI_VPRPForm(request.POST)
        if form.is_valid():
            Accounting_KZI_NKI_VPRP.objects.filter(pk=pk_id).update(
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
            return redirect('accounting_kzi_nki_vprp/list')
    jurnal = Accounting_KZI_NKI_VPRP.objects.get(pk=pk_id)
    form = Accounting_KZI_NKI_VPRPForm(instance=jurnal)

    context = {'jurnal' : jurnal, 'form': form}
    return render(request, 'app/accounting_kzi_nki_kned_vprp/accounting_kzi_nki_vprp_edit.html', context)
