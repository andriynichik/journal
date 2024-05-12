from django.db import models

# Create your models here.
from app.models import SignInvate
from django.db import models


class VPRPTOITC(models.Model):

    id = models.AutoField(primary_key=True)
    numbers_jornal =  models.CharField(max_length=32)
    denotation_vprp_basis = models.CharField(max_length=32)
    denotation_vprp_date = models.DateField()
    denotation_vprp_sign = models.ForeignKey(SignInvate, on_delete=models.CASCADE,
                                               related_name='denotation_vpr_sign', null=True)
    connection_information_vprp_sysadmin_sign = models.ForeignKey(SignInvate, on_delete=models.CASCADE,
                                               related_name='connection_information_vprp_admin_sign', null=True)
    connection_information_vprp_basis = models.CharField(max_length=32)
    connection_information_vprp_date = models.DateField(null=True, blank=True)
    disconectation_vprp_sysadmin_sign = models.ForeignKey(SignInvate, on_delete=models.CASCADE,
                                                          related_name='disconectation_vprp_sysadmin_sign', null=True)

    disconectation_vprp_seqadmin_sign = models.ForeignKey(SignInvate, on_delete=models.CASCADE,
                                                          related_name='disconectation_vprp_seqadmin_sign', null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=None, editable=True, null=True, blank=True)

    class Meta:
        db_table = 'vpr_to_itc'



