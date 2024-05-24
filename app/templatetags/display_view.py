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
            'vzi': 'ВЗІ',
            'var': 'ВАР'
        }
        return data[value]
    else:
        return ''

@register.filter
def get_jornal_name(value):
    data = {
        "record_seals_stamp_safe": "Журнал обліку печаток, штампів та сейфів",
        "backup_registration_log": "Журнал реєстрації резервних копій ІКС",
        "accounting_kzi_nki_kned_diia": "Журнал обліку КЗІ та НКІ КНЕД Дія",
        "accounting_kzi_nki_kned_diia_cold_reserve": "Журнал обліку засобів криптографічного захисту інформації та носіїв ключової інформації інформаційно-комунікаційної системи КНЕДП «Дія» (Холодний резерв).",
        "accounting_kzi_nki_kned_diia_main_site": "Журнал обліку засобів криптографічного захисту інформації та носіїв ключової інформації інформаційно-комунікаційної системи КНЕДП «Дія» (Основний майданчик).",
        "accounting_kzi_nki_kned_diia_reserve_site": "Журнал обліку засобів криптографічного захисту інформації та носіїв ключової інформації інформаційно-комунікаційної системи КНЕДП «Дія» (Резервний майданчик).",
        "accounting_kzi_nki_kned_diia_software_tools":"Журнал обліку засобів криптографічного захисту інформації та носіїв ключової інформації інформаційно-комунікаційної системи КНЕДП «Дія» (Програмні засоби).",
        "vpr_to_itc": "Журнал обліку ВПРП, що підключені до ІТС КНЕДП Дія",
        "gbrd_log": "Журнал генерації, рез. копіюв., відновл. та знищ. кл. даних",
        "backup_registration_log_vprp": "Журнал резервних копій ВПРП",
        "accounting_kzi_nki_vprp": "Журнал обліку КЗІ та НКІ ВПРП",
        "key_data_log": "Журнал ключових даних"

    }
    if value in data:
        return data[value]
    else:
        return None

@register.filter
def convertation_kzi_software_tools(value):
    data = {
        '1':'Програмний комплекс взаємодії віддалених автоматизованих робочих місць пунктів реєстрації послуг Mobile ID на територіях центрів обслуговування клієнт',
        '2':'Програмний комплекс користувача центру сертифікації ключів"ІІТ Користувач ЦСК-1"з комплектом багатоплатформенних криптографічних бібліотек та додатків',
        '3':'Програмний комплекс віддаленого управління шлюзами захисту "ІІТ Захист з`єднань-2. Віддалене управління шлюзами захисту',
        '4':'Програмний комплекс ЦСК "ІІТ ЦСК-1"',
        '5':'Програмний комплекс користувача ЦСК "ІІТ Користувач ЦСК-1"',
        '6':'Програмний комплекс клієнта захисту мережних з`єднань "ІІТ Захист з`єднань-2. Клієнт захисту з`єднань"',


        }
    if str(value) in data:
        return data[str(value)]
    else:
        return None


@register.filter
def convertation_kzi(value):
    data = {
        '1': 'Шлюз захисту "Бар`єр-301"',
        '2': 'Мережевий IP-шифратор "Канал-401"',
        '3': 'Мережний криптомодуль "Гряда-301" мікропристрій',
        '4': 'Мережний криптомодуль "Гряда-301" ВП',
        '5': '"Електронний ключ" Алмаз-1К',
        '6': '"Електронний ключ" Кристал-1',
    }
    if str(value) in data:
        return data[str(value)]
    else:
        return None

@register.filter
def convertation_nki(value):
    data = {
        '1' : 'Електронний ключ',
        '2': 'Мережний криптомодуль',
        '3': 'Шлюз захисту'
    }

    if str(value) in data:
        return data[str(value)]
    else:
        return None


@register.filter
def convertation_operation(value):
    data = {
        "1": 'Генерація',
        "2": 'Формування',
        "3": 'Знищення',
        "4": 'Скасування',
        "5": 'Відновлення',
        "6": 'Резервне копіювання',
    }
    if str(value) in data:
        return data[str(value)]
    else:
        return None