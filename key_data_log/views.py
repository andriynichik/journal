from .models import KeyDataLog
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import KeyDataLogForm
from django.utils.timezone import now
from django.contrib import messages

@login_required
def KeyDataLog_List(request):
    transactions = KeyDataLog.objects.all().select_related()

    data = {'transactions': transactions}
    return render(request, 'app/key_data_log/key_data_log_list.html', context=data)


@login_required
def KeyDataLog_Create(request):
    data = {}
    form = KeyDataLogForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            log = KeyDataLog(operation_type = form.cleaned_data['operation_type'],
                                       date_time= form.cleaned_data['date_time'],
                                       data_type = form.cleaned_data['data_type'],
                                       number_document = form.cleaned_data['number_document'],
                                       notes=form.cleaned_data['notes'],
                                       created=now())

            log.save()
            messages.success(request, 'Запис успішно створено')
            return redirect('key_data_log/list')
    data['form'] = form
    return render(request, 'app/key_data_log/key_data_log_create.html', data)




@login_required
def KeyDataLog_Edit(request, pk_id):
    if request.method == "POST":
        form = KeyDataLogForm(request.POST)
        if form.is_valid():
            KeyDataLog.objects.filter(pk=pk_id).update(
                operation_type=form.cleaned_data['operation_type'],
                date_time=form.cleaned_data['date_time'],
                data_type=form.cleaned_data['data_type'],
                number_document=form.cleaned_data['number_document'],
                notes=form.cleaned_data['notes'],
            )
            messages.success(request, 'Дані змінено')
            return redirect('key_data_log/list')
    jurnal = KeyDataLog.objects.get(pk=pk_id)
    form = KeyDataLogForm(instance=jurnal)

    context = {'jurnal' : jurnal, 'form': form}
    return render(request, 'app/key_data_log/key_data_log_edit.html', context)

