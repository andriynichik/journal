# # -*- encoding: utf-8 -*-
# """
from django.db import models
from authentication.models import User

class SignInvate(models.Model):
    id = models.AutoField(primary_key=True)
    jurnal = models.CharField(max_length=128)
    record_id = models.IntegerField()
    field_name = models.CharField(max_length=128)
    user_sign = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    sing = models.CharField(max_length=128,  null=True)

    class Meta:
        unique_together = (('jurnal', 'record_id', 'field_name'),)

class Transaction(models.Model):
    bill_for = models.CharField(max_length=100)
    issue_date = models.DateField()
    due_date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=10)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'

    @property
    def status_info(self):
        res = {'class': None}

        if self.status == "Paid":
            res['class'] = 'text-success'
        elif self.status == "Due":
            res['class'] = 'text-warning'
        elif self.status == "Canceled":
            res['class'] = 'text-danger'

        return res


#Журнал реєстрації резервних копій


# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username.strip(), email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(username, email, password, **extra_fields)
# # Адміністратор безпеки має ведучу роль по таблицям Надавача (редагування, перегляд та підпис).
# # Перегляд для нього доступний всіх таблиць Надавача та ВПР.
# # Системний адміністратор, адміністратор реєстрації та сертифікації, адміністратор аудиту доступно лише перегляд (ознайомлення з інформацією для підпису) та підпис.
# # Адміністратор аудиту - перегляд всіх таблиць.
# #
# #
# #
# #
# # Також, ВЗІ доступно редагування, перегляд та підпис у журналах для ВПР. ВАР - лише ознайомлення та підпис.
#
# class CustomUser(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('security_admin', 'Адміністратор безпеки'),
#         ('system_admin', 'Системний адміністратор'),
#         ('reg_cert_admin', 'Адміністратор реєстрації та сертифікації'),
#         ('audit_admin', 'Адміністратор аудиту'),
#     )
#     user_type = models.CharField(max_length=64, choices=USER_TYPE_CHOICES)
#     def is_security_admin(self):
#         return self.user_type == 'security_admin'
#
#     def is_system_admin(self):
#         return self.user_type == 'system_admin'
#
#     def is_reg_cert_admin(self):
#         return self.user_type == 'reg_cert_admin'
#
#     def is_audit_admin(self):
#         return self.user_type == 'audit_admin'
#
#     objects = CustomUserManager()
#


# class User(models.Model):
#     pass
#     # position =
