# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from backup_registration_log import views as backup_registration_views
from record_seals_stamp_safe import views as record_seals_stamp_safe_views
from authentication  import views as users

urlpatterns = [

    # The home page
    # path('', views.index, name='home'),

    re_path(r'^transactions/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.TransactionView.as_view(),
            name='transactions'),
    #

    re_path('backup_registration_log/list', backup_registration_views.BackupRegistrationLogList,
            name='backup_registration_log'),
    re_path('backup_registration_log/create', backup_registration_views.BackupRegistrationLogCreate,
             name='backup_registration_log_create'),
    re_path('backup_registration_log/edit/(?P<log_id>\d+)/$', backup_registration_views.BackupRegistrationLogEdit,
            name='backup_registration_log_edit_view'),


    re_path('record_seals_stamp_safe/list', record_seals_stamp_safe_views.RecordSealsStampSafeList,
            name='record_seals_stamp_safe'),
    re_path('record_seals_stamp_safe/create', record_seals_stamp_safe_views.RecordSealsStampSafeCreate,
            name='record_seals_stamp_safe_create'),
    re_path('record_seals_stamp_safe/edit/(?P<pk_id>\d+)/$', record_seals_stamp_safe_views.RecordSealsStampSafeEdit,
            name='record_seals_stamp_safe_edit_view'),
    re_path('record_seals_stamp_safe/edit/(?P<pk_id>\d+)/$', record_seals_stamp_safe_views.RecordSealsStampSafeEdit,
            name='record_seals_stamp_safe_edit_view'),


    path("signinvate/create/<slug:jurnal>/<slug:field_name>/<int:record_id>/", views.sign_invite_create),

    re_path('signinvate/incoming', views.incoming_sign_request,
            name='incoming_sign_request'),

    re_path('signinvate/preview/(?P<invite_id>\d+)/$', views.preview_sign_request,
            name='preview_sign_request'),

    re_path('users/list', users.UsersList,
            name='users_list'),

    re_path('user/create', users.UserCreate,
            name='user_create'),




    # re_path(r'^backup_registration_log/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.BackupRegistrationLogView.as_view(),
    #         name='backup_registration_log'),


    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
