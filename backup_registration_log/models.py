from django.db import models
from authentication.models import User
from app.models import SignInvate
from django.utils import timezone

# Create your models here.
class BackupRegistrationLog(models.Model):
    id = models.AutoField(primary_key=True)
    number_device_beckup_info = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    user_sign = models.ForeignKey(SignInvate, on_delete=models.SET_NULL, related_name='signature_backup' , null=True)
    updated = models.DateTimeField(auto_now=True, editable=True, null=True, blank=True)

    class Meta:
        db_table = "backup_registration_log"