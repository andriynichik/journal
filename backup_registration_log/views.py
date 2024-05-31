from .models import  BackupRegistrationLog
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import BackupRegistrationLogForm
from django.utils.timezone import now
from django.contrib import messages
from app.decorators import requires_role



@login_required
@requires_role(roles = ['security_admin'])
def BackupRegistrationLogList(request):
    transactions = BackupRegistrationLog.objects.all().select_related()

    data = {'transactions': transactions}
    return render(request, 'app/transactions/backup_registration_log_list.html',context=data)
@login_required
@requires_role(roles = ['security_admin'])
def BackupRegistrationLogCreate(request):
    data = {}
    form = BackupRegistrationLogForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            log = BackupRegistrationLog(number_device_beckup_info = form.cleaned_data['number_device_beckup_info'],
                                         author_id=request.user.id,
                                         created=now())

            log.save()
            messages.success(request, 'Запис успішно створено')
            return redirect('backup_registration_log/list')
    data['form'] = form
    return render(request, 'app/transactions/backup_registration_log_create.html', data)


@login_required
@requires_role(roles = ['security_admin'])
def BackupRegistrationLogEdit(request, log_id):
    if request.method == "POST":
        form = BackupRegistrationLogForm(request.POST)
        if form.is_valid():
            BackupRegistrationLog.objects.filter(pk=log_id).update(
                number_device_beckup_info=form.cleaned_data['number_device_beckup_info']
            )
            messages.success(request, 'Дані успішно змінено')
            return redirect('backup_registration_log/list')
    jurnal = BackupRegistrationLog.objects.get(pk=log_id)
    form = BackupRegistrationLogForm(instance=jurnal)
    context = {'jurnal' : jurnal, 'form': form}
    return render(request, 'app/transactions/backup_registration_log_edit.html', context)
