from django.db import models
from authentication.models import User
from app.models import SignInvate


#  Журнал обліку печаток, штампів та сейфів
class RecordSealsStampSafe(models.Model):

    id = models.AutoField(primary_key=True)
    numbers_imprint_individual_seal = models.TextField()
    number_safe = models.TextField()
    registration_issue_date = models.DateField()
    # author_position = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='author_position_created')
    author_position_signature = models.ForeignKey(SignInvate, on_delete=models.CASCADE, related_name='signature' , null=True)
    # author_admin_security = models.ForeignKey(User,null=True,  on_delete=models.CASCADE, related_name='author_admin_security')
    return_date = models.DateField(null=True, blank=True)
    security_signature = models.ForeignKey(SignInvate, on_delete=models.CASCADE, related_name='signature_admin_security', null=True)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "record_seals_stamp_safe"


