# -*- encoding: utf-8 -*-

import uuid

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

USER_TYPE_CHOICES = (
    ('security_admin', 'Адміністратор безпеки'),
    ('system_admin', 'Системний адміністратор'),
    ('reg_cert_admin', 'Адміністратор реєстрації та сертифікації'),
    ('audit_admin', 'Адміністратор аудиту'),
    ('vzi', 'ВЗІ'),
    ('var', 'ВАР'),
)

# Create your models here.
class User(AbstractUser):



    role = models.CharField(
        max_length=32,
        choices=USER_TYPE_CHOICES,
    )
    last_password_update = models.DateTimeField(auto_now=True , editable=True, null=True, blank=True)
