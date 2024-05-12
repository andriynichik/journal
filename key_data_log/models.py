from app.models import SignInvate
from django.db import models

OPERATION_TYPE_CHOICE = (
    (1, 'Генерація'),
    (2, 'Формування'),
    (3, 'Знищення'),
    (4, 'Скасування'),
    (5, 'Відновлення'),
    (6, 'Резервне копіювання'),

)

class KeyDataLog(models.Model):

    id = models.AutoField(primary_key=True)
    operation_type = models.IntegerField(choices=OPERATION_TYPE_CHOICE)
    date_time = models.DateTimeField()
    data_type = models.CharField(max_length=128)
    number_document = models.CharField(max_length=128)
    user_sign = models.ForeignKey(SignInvate, on_delete=models.CASCADE,
                                                related_name='user_sign_key_data', null=True)
    admin_sign = models.ForeignKey(SignInvate, on_delete=models.CASCADE,
                                                related_name='admin_sign_key_data', null=True)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True , editable=True, null=True, blank=True)

    class Meta:
        db_table = 'key_data_log'



