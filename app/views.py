# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse, QueryDict
from django import template
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.contrib import messages

from accounting_kzi_nki_kned_diia_cold_reserve.models import Accounting_KZI_NKI_KNED_DIIA_COLD_RESERVE
from accounting_kzi_nki_kned_diia_main_site.models import Accounting_KZI_NKI_KNED_DIIA_MAIN_SITE
from accounting_kzi_nki_kned_diia_reserve_site.models import Accounting_KZI_NKI_KNED_DIIA_RESERVE_SITE
from accounting_kzi_nki_kned_diia_software_tools.models import Accounting_KZI_NKI_KNED_DIIA_SOFTWARE_TOOLS
from authentication.models import User
from backup_registration_log.forms import  BackupRegistrationLogForm
from backup_registration_log.models import BackupRegistrationLog
from app.utils import set_pagination
from app.forms import TransactionForm
from app.models import Transaction , SignInvate
from key_data_log.models import KeyDataLog
from record_seals_stamp_safe.models import RecordSealsStampSafe
from accounting_kzi_nki_kned_diia.models import Accounting_KZI_NKI_KNED_DIIA
from vpr_to_itc.models import VPRPTOITC
from gbrd_log.models import GRDBLog
from backup_registration_log_vprp.models import BackupRegistrationLogVPRP
from accounting_kzi_nki_vprp.models import Accounting_KZI_NKI_VPRP
import uuid

# @login_required
# def RecordSealsStampSafeCreate(request):
#     data = {}
#     form = RecordSealsStampSafeForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             log = RecordSealsStampSafe(numbers_imprint_individual_seal = form.cleaned_data['numbers_imprint_individual_seal'],
#                                        number_safe= form.cleaned_data['number_safe'],
#                                        registration_issue_date = form.cleaned_data['registration_issue_date'],
#                                        notes = form.cleaned_data['notes'],
#                                         created=now())
#
#             log.save()
#             return redirect('record_seals_stamp_safe/list')
#     data['form'] = form
#     return render(request, 'app/record_seals_stamp_safe/record_seals_stamp_safe_create.html', data)

def get_jornal_name(value):
    data = {
        "record_seals_stamp_safe": "Журналу обліку печаток, штампів та сейфів",
        "backup_registration_log": "Журнал резервних копій ІКС",
        "backup_registration_log_vprp": "Журнал резервних копій ВПРП",
        "accounting_kzi_nki_kned_diia": "Журнал обліку КЗІ та НКІ КНЕД Дія",
        "accounting_kzi_nki_vprp": "Журнал обліку КЗІ та НКІ ВПРП",

        "accounting_kzi_nki_kned_diia_cold_reserve" : "Журнал обліку засобів криптографічного захисту інформації та носіїв ключової інформації інформаційно-комунікаційної системи КНЕДП «Дія» (Холодний резерв).",
        "vpr_to_itc": "Журнал обліку ВПРП, що підключені до ІТС КНЕДП Дія",
        "gbrd_log": "Журнал генерації, рез. копіюв., відновл. та знищ. кл. даних",
        "key_data_log": "Журнал ключових даних"

    }
    if value in data:
        return data[value]
    else:
        return None


def get_model_by_jornal(jornal_name):
    mod = {
        "record_seals_stamp_safe": RecordSealsStampSafe,
        "backup_registration_log": BackupRegistrationLog,
        "backup_registration_log_vprp": BackupRegistrationLogVPRP,
        "accounting_kzi_nki_kned_diia": Accounting_KZI_NKI_KNED_DIIA,
        "accounting_kzi_nki_kned_diia_cold_reserve": Accounting_KZI_NKI_KNED_DIIA_COLD_RESERVE,
        "accounting_kzi_nki_kned_diia_main_site": Accounting_KZI_NKI_KNED_DIIA_MAIN_SITE,
        "accounting_kzi_nki_kned_diia_reserve_site": Accounting_KZI_NKI_KNED_DIIA_RESERVE_SITE,
        "accounting_kzi_nki_kned_diia_software_tools": Accounting_KZI_NKI_KNED_DIIA_SOFTWARE_TOOLS,
        "vpr_to_itc": VPRPTOITC,
        "gbrd_log" : GRDBLog,
        "accounting_kzi_nki_vprp": Accounting_KZI_NKI_VPRP,
        "key_data_log": KeyDataLog,


    }
    if jornal_name in mod:
        return mod[jornal_name]
    else:
        return None

def get_template_by_jornal(jornal_name):
    data = {
        "record_seals_stamp_safe": "app/templates/record_seals_stamp_safe_list.html"
    }
    if jornal_name in data:
        return data[jornal_name]
    else:
        return None

def change_jornal_sign(model, context, sign_id):
    if context["jurnal"]['system_name'] == "record_seals_stamp_safe":
        if context['field_name'] == "author_position_signature":
            model.objects.filter(id=context["record_id"]).update(author_position_signature = sign_id)
        elif context['field_name'] == "security_signature":
            model.objects.filter(id=context["record_id"]).update(security_signature=sign_id)
    elif context["jurnal"]['system_name'] == "backup_registration_log":
        model.objects.filter(id=context["record_id"]).update(user_sign=sign_id)
    elif context["jurnal"]['system_name'] == "accounting_kzi_nki_kned_diia":
        if context['field_name'] == "accounting_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(accounting_kzi_nki_sign=sign_id)
        elif context['field_name'] == "get_remedy_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(get_remedy_kzi_nki_sign=sign_id)
        elif context['field_name'] == "note_return_means_sign":
            model.objects.filter(id=context["record_id"]).update(note_return_means_sign=sign_id)
    elif context["jurnal"]['system_name'] == "accounting_kzi_nki_kned_diia_cold_reserve":
        if context['field_name'] == "accounting_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(accounting_kzi_nki_sign=sign_id)
        elif context['field_name'] == "get_remedy_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(get_remedy_kzi_nki_sign=sign_id)
        elif context['field_name'] == "note_return_means_sign":
            model.objects.filter(id=context["record_id"]).update(note_return_means_sign=sign_id)
    elif context["jurnal"]['system_name'] == "accounting_kzi_nki_kned_diia_main_site":
        if context['field_name'] == "accounting_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(accounting_kzi_nki_sign=sign_id)
        elif context['field_name'] == "get_remedy_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(get_remedy_kzi_nki_sign=sign_id)
        elif context['field_name'] == "note_return_means_sign":
            model.objects.filter(id=context["record_id"]).update(note_return_means_sign=sign_id)
    elif context["jurnal"]['system_name'] == "accounting_kzi_nki_kned_diia_reserve_site":
        if context['field_name'] == "accounting_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(accounting_kzi_nki_sign=sign_id)
        elif context['field_name'] == "get_remedy_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(get_remedy_kzi_nki_sign=sign_id)
        elif context['field_name'] == "note_return_means_sign":
            model.objects.filter(id=context["record_id"]).update(note_return_means_sign=sign_id)
    elif context["jurnal"]['system_name'] == "accounting_kzi_nki_kned_diia_software_tools":
        if context['field_name'] == "accounting_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(accounting_kzi_nki_sign=sign_id)
        elif context['field_name'] == "get_remedy_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(get_remedy_kzi_nki_sign=sign_id)
        elif context['field_name'] == "note_return_means_sign":
            model.objects.filter(id=context["record_id"]).update(note_return_means_sign=sign_id)
    elif context["jurnal"]['system_name'] == "vpr_to_itc":
        if context['field_name'] == "denotation_vprp_sign":
            model.objects.filter(id=context["record_id"]).update(denotation_vprp_sign=sign_id)
        elif context['field_name'] == "connection_information_vprp_sysadmin_sign":
            model.objects.filter(id=context["record_id"]).update(connection_information_vprp_sysadmin_sign=sign_id)
        elif context['field_name'] == "disconectation_vprp_sysadmin_sign":
            model.objects.filter(id=context["record_id"]).update(disconectation_vprp_sysadmin_sign=sign_id)
        elif context['field_name'] == "disconectation_vprp_seqadmin_sign":
            model.objects.filter(id=context["record_id"]).update(disconectation_vprp_seqadmin_sign=sign_id)
    elif context["jurnal"]['system_name'] == "gbrd_log":
        if context['field_name'] == "user_sign":
            model.objects.filter(id=context["record_id"]).update(user_sign=sign_id)
        elif context['field_name'] == "admin_sign":
            model.objects.filter(id=context["record_id"]).update(admin_sign=sign_id)
    elif context["jurnal"]['system_name'] == "backup_registration_log_vprp":
        model.objects.filter(id=context["record_id"]).update(user_sign=sign_id)
    elif context["jurnal"]['system_name'] == "accounting_kzi_nki_vprp":
        if context['field_name'] == "accounting_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(accounting_kzi_nki_sign=sign_id)
        elif context['field_name'] == "get_remedy_kzi_nki_sign":
            model.objects.filter(id=context["record_id"]).update(get_remedy_kzi_nki_sign=sign_id)
        elif context['field_name'] == "note_return_means_sign":
            model.objects.filter(id=context["record_id"]).update(note_return_means_sign=sign_id)
    elif context["jurnal"]['system_name'] == "key_data_log":
        if context['field_name'] == "user_sign":
            model.objects.filter(id=context["record_id"]).update(user_sign=sign_id)
        elif context['field_name'] == "admin_sign":
            model.objects.filter(id=context["record_id"]).update(admin_sign=sign_id)







@login_required
def sign_invite_create(request, jurnal,  field_name, record_id):
    context = {
        "jurnal" : {
            "name" : get_jornal_name(jurnal),
            "system_name" : jurnal
        },
        "field_name" : field_name,
        "record_id" : record_id
    }

    if request.method == 'POST':
        model_name =  get_model_by_jornal(jurnal)
        records = get_object_or_404(model_name, id=int(record_id))
        invite = SignInvate(
                        jurnal=jurnal,
                        record_id=record_id,
                        field_name=field_name,
                        status=0,
                        user_sign_id=request.POST['user_sign']
                        )
        try:
            invite.save()
            change_jornal_sign(model_name, context, invite.id)
            messages.success(request, 'Запит на підпис успішно створено')
        except Exception as e:
            messages.warning(request, 'Запит на підпис вже існує')
        return redirect("/"+jurnal+'/list')

    users = User.objects.all()
    context['users'] = users

    return render(request, 'app/sign_invite/create_invite.html', context)



@login_required
def incoming_sign_request(request):
    # context = {}
    invite_list = list()
    user_incoming_invite = SignInvate.objects.filter(user_sign_id=request.user.id, status=0)


    for invite in user_incoming_invite:
        model_name = get_model_by_jornal(invite.jurnal)
        record = model_name.objects.filter(id = invite.record_id).first()
        invite_list.append({
            "records" : record,
            "invite" : invite,
        })


        # print(model_name)
    context = {"invates" : user_incoming_invite, "mod": True}
    return render(request, 'app/sign_invite/incoming_invite.html', context)

def preview_sign_request(request,invite_id):
    invite = get_object_or_404(SignInvate, id=int(invite_id))
    if invite.user_sign_id != request.user.id:
        messages.warning(request, 'Відмовлено в доступі')
        return redirect("/signinvate/incoming")
    model_name = get_model_by_jornal(invite.jurnal)
    record = model_name.objects.get(id = invite.record_id)
    context = {'record' : record, 'invite' : invite}
    return render(request, 'app/sign_invite/invite_preview.html', context)

@login_required
def sigtature(request):
    if request.method == 'POST':
        SignInvate.objects.filter(id=request.POST['invite_id']).update(
            sing = str(uuid.uuid4().hex),
            status = 1
        )
    return redirect("/signinvate/incoming")







@login_required
def modal(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('app/partial/ui-modals.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

class BackupRegistrationLogViewNew(View):
    model = BackupRegistrationLog
    template_name = 'app/transactions/backup_registration_log_list.html'

class BackupRegistrationLogView(View):
    context = {'segment': 'backup_registration_log'}
    def get(self, request, template=None, *args, **kwargs):
        transactions = BackupRegistrationLog.objects.all()
        self.context['transactions'] = transactions
        template = loader.get_template('app/transactions/backup_registration_log_list.html')
        # return HttpResponse("Hello!!! async world!)")
        # template = loader.get_template("backup_registration_log_list.html")
        return HttpResponse(template.render(self.context, request))



class BackupRegistrationLogCreate(View):
    context = {'segment': 'backup_registration_log_create'}
    def get(self, request, template=None, *args, **kwargs):


        template = loader.get_template('app/transactions/backup_registration_log_edit.html')
        self.context['form'] = BackupRegistrationLogForm(instance=transaction)
        # return HttpResponse("Hello!!! async world!)")
        # template = loader.get_template("backup_registration_log_list.html")
        return HttpResponse(template.render(self.context, request))
    def post(self, request, template=None, *args, **kwargs):
        print(self.request.POST['number_device_beckup_info'])

class TransactionView(View):
    context = {'segment': 'transactions'}

    def get(self, request, pk=None, action=None):
        if request.is_ajax():
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            elif pk and not action:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('transactions')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        transaction = self.get_object(pk)
        transaction.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('transactions')

        response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(bill_for__icontains=key.strip())
                    else:
                        filter_params |= Q(bill_for__icontains=key.strip())

        transactions = Transaction.objects.filter(filter_params) if filter_params else Transaction.objects.all()

        self.context['transactions'], self.context['info'] = set_pagination(request, transactions)
        if not self.context['transactions']:
            return False, self.context['info']

        return self.context, 'app/transactions/list.html'

    def edit(self, request, pk):
        transaction = self.get_object(pk)

        self.context['transaction'] = transaction
        self.context['form'] = TransactionForm(instance=transaction)

        return self.context, 'app/transactions/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        transaction = self.get_object(pk)
        form = TransactionForm(instance=transaction)
        context = {'instance': transaction, 'form': form}
        return render_to_string('app/transactions/edit_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        transaction = get_object_or_404(Transaction, id=pk)
        return transaction

    def get_row_item(self, pk):
        transaction = self.get_object(pk)
        edit_row = render_to_string('app/transactions/edit_row.html', {'instance': transaction})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        transaction = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = TransactionForm(form_data, instance=transaction)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Transaction saved successfully')

            return True, 'Transaction saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'
