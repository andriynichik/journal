# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from app import views
from backup_registration_log import views as backup_registration_views
from record_seals_stamp_safe import views as record_seals_stamp_safe_views
from authentication  import views as users
from accounting_kzi_nki_kned_diia import views as accounting_kzi_nki_kned_diia_view
from accounting_kzi_nki_kned_diia_cold_reserve import views as accounting_kzi_nki_kned_diia_cold_reserve_view
from accounting_kzi_nki_kned_diia_main_site import views as accounting_kzi_nki_kned_diia_main_site_view
from accounting_kzi_nki_kned_diia_reserve_site import views as accounting_kzi_nki_kned_diia_reserve_site_view
from accounting_kzi_nki_kned_diia_software_tools import views as accounting_kzi_nki_kned_diia_software_tools_view
from vpr_to_itc import views as  vpr_to_itc_view
from gbrd_log import  views as gbrd_log_view
from backup_registration_log_vprp import views as backup_registration_vprp_views
from  accounting_kzi_nki_vprp import views as accounting_kzi_nki_vprp_view
from key_data_log import views as key_data_log_views

urlpatterns = [

    # The home page
    # path('', views.index, name='home'),

    re_path(r'^transactions/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.TransactionView.as_view(),
            name='transactions'),
    #
    re_path('key_data_log/list', key_data_log_views.KeyDataLog_List,
            name='key_data_log'),
    re_path('key_data_log/create', key_data_log_views.KeyDataLog_Create,
            name='key_data_log_create'),
    re_path('key_data_log/edit/(?P<pk_id>\d+)/$', key_data_log_views.KeyDataLog_Edit,
            name='key_data_log_edit_view'),


    re_path('accounting_kzi_nki_vprp/list',
            accounting_kzi_nki_vprp_view.Accounting_KZI_NKI_VPRPList,
            name='accounting_kzi_nki_vprp'),
    re_path('accounting_kzi_nki_vprp/create',
            accounting_kzi_nki_vprp_view.Accounting_KZI_NKI_VPRPCreate,
            name='accounting_kzi_nki_vprp_create'),
    re_path('accounting_kzi_nki_vprp/edit/(?P<pk_id>\d+)/$',
            accounting_kzi_nki_vprp_view.Accounting_KZI_NKI_VPRPEdit,
            name='accounting_kzi_nki_vprp_edit_view'),

    re_path('accounting_kzi_nki_kned_diia/list',
            accounting_kzi_nki_kned_diia_view.Accounting_KZI_NKI_KNED_DIIAList,
            name='accounting_kzi_nki_kned_diia'),
    re_path('accounting_kzi_nki_kned_diia/create',
            accounting_kzi_nki_kned_diia_view.Accounting_KZI_NKI_KNED_DIIACreate,
            name='accounting_kzi_nki_kned_diiac_create'),
    re_path('accounting_kzi_nki_kned_diia/edit/(?P<pk_id>\d+)/$',
            accounting_kzi_nki_kned_diia_view.Accounting_KZI_NKI_KNED_DIIAEdit,
            name='accounting_kzi_nki_kned_diia_edit_view'),

    re_path('accounting_kzi_nki_kned_diia_cold_reserve/list',
            accounting_kzi_nki_kned_diia_cold_reserve_view.Accounting_KZI_NKI_KNED_DIIA_COLD_RESERVE_List,
            name='accounting_kzi_nki_kned_diia_cold_reserve'),
    re_path('accounting_kzi_nki_kned_diia_cold_reserve/create',
            accounting_kzi_nki_kned_diia_cold_reserve_view.Accounting_KZI_NKI_KNED_DIIA_COLD_RESERVE_Create,
            name='accounting_kzi_nki_kned_diia_cold_reserve_create'),
    re_path('accounting_kzi_nki_kned_diia_cold_reserve/edit/(?P<pk_id>\d+)/$',
            accounting_kzi_nki_kned_diia_cold_reserve_view.Accounting_KZI_NKI_KNED_DIIA_COLD_RESERVE_Edit,
            name='accounting_kzi_nki_kned_diia_cold_reserve_edit_view'),

    re_path('accounting_kzi_nki_kned_diia_main_site/list',
            accounting_kzi_nki_kned_diia_main_site_view.Accounting_KZI_NKI_KNED_DIIA_MAIN_SITE_List,
            name='accounting_kzi_nki_kned_diia_main_site'),
    re_path('accounting_kzi_nki_kned_diia_main_site/create',
            accounting_kzi_nki_kned_diia_main_site_view.Accounting_KZI_NKI_KNED_DIIA_MAIN_SITE_Create,
            name='accounting_kzi_nki_kned_diia_main_site_create'),
    re_path('accounting_kzi_nki_kned_diia_main_site/edit/(?P<pk_id>\d+)/$',
            accounting_kzi_nki_kned_diia_main_site_view.Accounting_KZI_NKI_KNED_DIIA_MAIN_SITE_Edit,
            name='accounting_kzi_nki_kned_diia_main_site_edit_view'),


    re_path('accounting_kzi_nki_kned_diia_reserve_site/list',
            accounting_kzi_nki_kned_diia_reserve_site_view.Accounting_KZI_NKI_KNED_DIIA_MAIN_SITE_List,
            name='accounting_kzi_nki_kned_diia_reserve_site'),
    re_path('accounting_kzi_nki_kned_diia_reserve_site/create',
            accounting_kzi_nki_kned_diia_reserve_site_view.Accounting_KZI_NKI_KNED_DIIA_MAIN_SITE_Create,
            name='accounting_kzi_nki_kned_diia_reserve_site_create'),
    re_path('accounting_kzi_nki_kned_diia_reserve_site/edit/(?P<pk_id>\d+)/$',
            accounting_kzi_nki_kned_diia_reserve_site_view.Accounting_KZI_NKI_KNED_DIIA_MAIN_SITE_Edit,
            name='accounting_kzi_nki_kned_diia_reserve_site_edit_view'),

    re_path('accounting_kzi_nki_kned_diia_software_tools/list',
            accounting_kzi_nki_kned_diia_software_tools_view.Accounting_KZI_NKI_KNED_DIIA_SOFTWARE_TOOLS_List,
            name='accounting_kzi_nki_kned_diia_software_tools'),
    re_path('accounting_kzi_nki_kned_diia_software_tools/create',
            accounting_kzi_nki_kned_diia_software_tools_view.Accounting_KZI_NKI_KNED_DIIA_SOFTWARE_TOOLS_Create,
            name='accounting_kzi_nki_kned_diia_software_tools_create'),
    re_path('accounting_kzi_nki_kned_diia_software_tools/edit/(?P<pk_id>\d+)/$',
            accounting_kzi_nki_kned_diia_software_tools_view.Accounting_KZI_NKI_KNED_DIIA_SOFTWARE_TOOLS_Edit,
            name='accounting_kzi_nki_kned_diia_software_tools_edit_view'),


    re_path('backup_registration_log/list', backup_registration_views.BackupRegistrationLogList,
            name='backup_registration_log'),
    re_path('backup_registration_log/create', backup_registration_views.BackupRegistrationLogCreate,
             name='backup_registration_log_create'),
    re_path('backup_registration_log/edit/(?P<log_id>\d+)/$', backup_registration_views.BackupRegistrationLogEdit,
            name='backup_registration_log_edit_view'),

    re_path('backup_registration_log_vprp/list', backup_registration_vprp_views.BackupRegistrationLogVPRPList,
            name='backup_registration_log_vprp'),
    re_path('backup_registration_log_vprp/create', backup_registration_vprp_views.BackupRegistrationLogVPRPCreate,
            name='backup_registration_log_vprp_create'),
    re_path('backup_registration_log_vprp/edit/(?P<log_id>\d+)/$', backup_registration_vprp_views.BackupRegistrationLogVPRPEdit,
            name='backup_registration_log_vprp_edit_view'),


    re_path('vpr_to_itc/list', vpr_to_itc_view.VPRPTOITC_List,
            name='vpr_to_itc'),
    re_path('vpr_to_itc/create', vpr_to_itc_view.VPRPTOITC_Create,
            name='vpr_to_itc_create'),
    re_path('vpr_to_itc/edit/(?P<pk_id>\d+)/$', vpr_to_itc_view.VPRPTOITC_Edit,
            name='vpr_to_itc_edit_view'),

    re_path('gbrd_log/list', gbrd_log_view.GRDBLog_List,
            name='gbrd_log'),
    re_path('gbrd_log/create', gbrd_log_view.GRDBLog_Create,
            name='gbrd_log_create'),
    re_path('gbrd_log/edit/(?P<pk_id>\d+)/$', gbrd_log_view.GRDBLog_Edit,
            name='gbrd_log_edit_view'),


    re_path('record_seals_stamp_safe/list', record_seals_stamp_safe_views.RecordSealsStampSafeList,
            name='record_seals_stamp_safe'),
    re_path('record_seals_stamp_safe/create', record_seals_stamp_safe_views.RecordSealsStampSafeCreate,
            name='record_seals_stamp_safe_create'),
    re_path('record_seals_stamp_safe/edit/(?P<pk_id>\d+)/$', record_seals_stamp_safe_views.RecordSealsStampSafeEdit,
            name='record_seals_stamp_safe_edit_view'),
    # re_path('record_seals_stamp_safe/edit/(?P<pk_id>\d+)/$', record_seals_stamp_safe_views.RecordSealsStampSafeEdit,
    #         name='record_seals_stamp_safe_edit_view'),


    path("signinvate/create/<slug:jurnal>/<slug:field_name>/<int:record_id>/", views.sign_invite_create),

    re_path('signinvate/incoming', views.incoming_sign_request,
            name='incoming_sign_request'),
    re_path('signinvate/sign', views.sign_request,
            name='sign_request'),
    re_path('signinvate/remove/(?P<invite_id>\d+)/$', views.sign_invite_cancel,
            name='sign_invite_cancel'),

    re_path('signinvate/preview/(?P<invite_id>\d+)/$', views.preview_sign_request,
            name='preview_sign_request'),

    re_path('sign/preview/(?P<invite_id>\d+)/$', views.preview_signed,
            name='preview_signed'),


    re_path('users/list', users.UsersList,
            name='users_list'),

    re_path('user/create', users.UserCreate,
            name='user_create'),

    re_path('sigtature', views.sigtature,
            name='user_sigtature'),

    re_path('change_password', users.change_password, name='change_password'),

    re_path("settings/", views.settings, name="settings"),
    re_path("user_agreemen_update/update", views.user_agreemen_update, name="user_agreemen_update")




    # re_path(r'^backup_registration_log/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.BackupRegistrationLogView.as_view(),
    #         name='backup_registration_log'),


    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
