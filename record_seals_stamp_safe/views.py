from django.shortcuts import render
from .models import  RecordSealsStampSafe
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .forms import RecordSealsStampSafeForm
from django.utils.timezone import now
from authentication.models import User
from django.contrib import messages


from django import template


@login_required
def RecordSealsStampSafeList(request):
    transactions = RecordSealsStampSafe.objects.all().select_related()

    data = {'transactions': transactions}
    return render(request, 'app/record_seals_stamp_safe/record_seals_stamp_safe_list.html',context=data)
@login_required
def RecordSealsStampSafeCreate(request):
    data = {}
    form = RecordSealsStampSafeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            log = RecordSealsStampSafe(numbers_imprint_individual_seal = form.cleaned_data['numbers_imprint_individual_seal'],
                                       number_safe= form.cleaned_data['number_safe'],
                                       registration_issue_date = form.cleaned_data['registration_issue_date'],
                                       notes = form.cleaned_data['notes'],
                                        created=now())

            log.save()
            messages.success(request, 'Запис успішно створено')
            return redirect('record_seals_stamp_safe/list')
    data['form'] = form
    return render(request, 'app/record_seals_stamp_safe/record_seals_stamp_safe_create.html', data)


@login_required
def RecordSealsStampSafeEdit(request, pk_id):
    if request.method == "POST":
        form = RecordSealsStampSafeForm(request.POST)
        if form.is_valid():
            RecordSealsStampSafe.objects.filter(pk=pk_id).update(
                numbers_imprint_individual_seal=form.cleaned_data['numbers_imprint_individual_seal'],
                number_safe=form.cleaned_data['number_safe'],
                registration_issue_date = form.cleaned_data['registration_issue_date'],
                notes = form.cleaned_data['notes'],
                return_date=form.cleaned_data['return_date']
            )
            messages.success(request, 'Дані змінено')
            return redirect('record_seals_stamp_safe/list')
    jurnal = RecordSealsStampSafe.objects.get(pk=pk_id)
    form = RecordSealsStampSafeForm(instance=jurnal)

    context = {'jurnal' : jurnal, 'form': form}
    return render(request, 'app/record_seals_stamp_safe/record_seals_stamp_safe_edit.html', context)
