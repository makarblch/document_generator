popular_tags = {'day': 'День', 'month': 'Месяц', 'year': 'Год', 'year 2 digits': 'Год (последние 2 цифры)',
                'date': 'Дата',
                'start date': 'Дата начала', 'end date': 'Дата окончания', 'full name': 'Ф.И.О',
                'course': 'Курс обучения',
                'educational program': 'Образовательная программа',
                'reason': 'Причина', 'email': 'Электронная почта', 'phone': 'Номер телефона',
                'initials': 'Фамилия и инициалы'}


def check_tags(key):
    return key in popular_tags.keys()