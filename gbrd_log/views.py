from .models import GRDBLog
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import GRDBLogForm
from django.utils.timezone import now
from django.contrib import messages
from app.decorators import requires_role

@login_required
@requires_role(roles = ['security_admin'])
def GRDBLog_List(request):
    transactions = GRDBLog.objects.all().select_related()

    data = {'transactions': transactions}
    return render(request, 'app/gbrd_log/gbrd_log_list.html', context=data)


@login_required
@requires_role(roles = ['security_admin'])
def GRDBLog_Create(request):
    data = {}
    form = GRDBLogForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            log = GRDBLog(operation_type = form.cleaned_data['operation_type'],
                                       date_time= form.cleaned_data['date_time'],
                                       data_type = form.cleaned_data['data_type'],
                                       number_document = form.cleaned_data['number_document'],
                                       notes=form.cleaned_data['notes'],
                                       created=now())

            log.save()
            messages.success(request, 'Запис успішно створено')
            return redirect('gbrd_log/list')
    data['form'] = form
    return render(request, 'app/gbrd_log/gbrd_log_create.html', data)




@login_required
@requires_role(roles = ['security_admin'])
def GRDBLog_Edit(request, pk_id):
    if request.method == "POST":
        form = GRDBLogForm(request.POST)
        if form.is_valid():
            GRDBLog.objects.filter(pk=pk_id).update(
                operation_type=form.cleaned_data['operation_type'],
                date_time=form.cleaned_data['date_time'],
                data_type=form.cleaned_data['data_type'],
                number_document=form.cleaned_data['number_document'],
                notes=form.cleaned_data['notes'],
            )
            messages.success(request, 'Дані змінено')
            return redirect('gbrd_log/list')
    jurnal = GRDBLog.objects.get(pk=pk_id)
    form = GRDBLogForm(instance=jurnal)

    context = {'jurnal' : jurnal, 'form': form}
    return render(request, 'app/gbrd_log/gbrd_log_edit.html', context)

