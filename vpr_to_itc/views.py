from .models import VPRPTOITC
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import VPRPTOITCForm
from django.utils.timezone import now
from django.contrib import messages

@login_required
def VPRPTOITC_List(request):
    transactions = VPRPTOITC.objects.all().select_related()

    data = {'transactions': transactions}
    return render(request, 'app/vpr_to_itc/vpr_to_itc_list.html', context=data)


@login_required
def VPRPTOITC_Create(request):
    data = {}
    form = VPRPTOITCForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            log = VPRPTOITC(numbers_jornal = form.cleaned_data['numbers_jornal'],
                                       denotation_vprp_basis= form.cleaned_data['denotation_vprp_basis'],
                                       denotation_vprp_date = form.cleaned_data['denotation_vprp_date'],
                                       connection_information_vprp_basis = form.cleaned_data['connection_information_vprp_basis'],
                                       connection_information_vprp_date=form.cleaned_data['connection_information_vprp_date'],
                                       created=now())

            log.save()
            messages.success(request, 'Запис успішно створено')
            return redirect('vpr_to_itc/list')
    data['form'] = form
    return render(request, 'app/vpr_to_itc/vpr_to_itc_create.html', data)




@login_required
def VPRPTOITC_Edit(request, pk_id):
    if request.method == "POST":
        form = VPRPTOITCForm(request.POST)
        if form.is_valid():
            VPRPTOITC.objects.filter(pk=pk_id).update(
                numbers_jornal=form.cleaned_data['numbers_jornal'],
                denotation_vprp_basis=form.cleaned_data['denotation_vprp_basis'],
                denotation_vprp_date=form.cleaned_data['denotation_vprp_date'],
                connection_information_vprp_basis=form.cleaned_data['connection_information_vprp_basis'],
                connection_information_vprp_date=form.cleaned_data['connection_information_vprp_date'],
            )
            messages.success(request, 'Дані змінено')
            return redirect('vpr_to_itc/list')
    jurnal = VPRPTOITC.objects.get(pk=pk_id)
    form = VPRPTOITCForm(instance=jurnal)

    context = {'jurnal' : jurnal, 'form': form}
    return render(request, 'app/vpr_to_itc/vpr_to_itc_edit.html', context)

