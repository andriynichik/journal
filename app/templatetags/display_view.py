from django import template

register = template.Library()

@register.filter
def role_view(value):
    if value:
        data = {
            'security_admin': 'Адміністратор безпеки',
            'system_admin': 'Системний адміністратор',
            'reg_cert_admin': 'Адміністратор реєстрації та сертифікації',
            'audit_admin': 'Адміністратор аудиту',
        }
        return data[value]
    else:
        return ''

@register.filter
def get_jornal_name(value):
    data = {
        "record_seals_stamp_safe": "Журнал обліку печаток, штампів та сейфів",
        "backup_registration_log": "Журнал реєстрації резервних копій ІКС"
    }
    if value in data:
        return data[value]
    else:
        return None



