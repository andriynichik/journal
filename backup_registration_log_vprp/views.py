from .models import  BackupRegistrationLogVPRP
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import BackupRegistrationLogVPRPForm
from django.utils.timezone import now
from django.contrib import messages



@login_required
def BackupRegistrationLogVPRPList(request):
    transactions = BackupRegistrationLogVPRP.objects.all().select_related()

    data = {'transactions': transactions}
    return render(request, 'app/backup_registration_log_vprp/backup_registration_log_vprp_list.html',context=data)
@login_required
def BackupRegistrationLogVPRPCreate(request):
    data = {}
    form = BackupRegistrationLogVPRPForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            log = BackupRegistrationLogVPRP(number_device_beckup_info = form.cleaned_data['number_device_beckup_info'],
                                         author_id=request.user.id,
                                         created=now())

            log.save()
            messages.success(request, 'Запис успішно створено')
            return redirect('backup_registration_log_vprp/list')
    data['form'] = form
    return render(request, 'app/backup_registration_log_vprp/backup_registration_log_vprp_create.html', data)


@login_required
def BackupRegistrationLogVPRPEdit(request, log_id):
    if request.method == "POST":
        form = BackupRegistrationLogVPRPForm(request.POST)
        if form.is_valid():
            BackupRegistrationLogVPRP.objects.filter(pk=log_id).update(
                number_device_beckup_info=form.cleaned_data['number_device_beckup_info']
            )
            messages.success(request, 'Дані успішно змінено')
            return redirect('backup_registration_log_vprp/list')
    jurnal = BackupRegistrationLogVPRP.objects.get(pk=log_id)
    form = BackupRegistrationLogVPRPForm(instance=jurnal)
    context = {'jurnal' : jurnal, 'form': form}
    return render(request, 'app/backup_registration_log_vprp/backup_registration_log_vprp_edit.html', context)
