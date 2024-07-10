from documents_processing import docx_processor, xlsx_processor


def process_docx():
    # Получаем все теги, которые есть в данном шаблоне
    tags = docx_processor.get_all_tags(template)
    print(tags)
    # Просим пользователя заполнить поля
    # values = {'name': 'Makar', 'title': 'lecturer', 'purpose': 'Пережить летнюю практику', 'date': '09.07.2024',
    #           'result1': 'Провести тестирование программы', 'result2': 'Стать крутым специалистом'}
    # docx_processor.fill_docx_template(template, output, values)

    # values = dict()
    # for element in tags:
    #     print(f"Input {element}: ")
    #     values[element] = input()
    # docx_processor.fill_docx_template(template, output, values)

    values = {'name': 'Ilya Tyamin', 'phone': '+79056538930', 'day': '23', 'month': '07', 'year': '2',
              'email': 'egg@mail.ru', 'group': 'bse226', 'year2digits': '24', 'date': '23.08.2025', 'rector': 'Pussy Doggy'}
    docx_processor.fill_docx_template(template, output, values)


def process_xlsx():
    tags = xlsx_processor.get_all_tags_xlsx(template)
    print(tags)
    # Просим пользователя заполнить поля
    # values = {'name': 'Makar', 'title': 'lecturer', 'purpose': 'Пережить летнюю практику', 'date': '09.07.2024',
    #           'result1': 'Провести тестирование программы', 'result2': 'Стать крутым специалистом'}
    # docx_processor.fill_docx_template(template, output, values)

    values = dict()
    for element in tags:
        print(f"Input {element}: ")
        values[element] = input()
    xlsx_processor.fill_xlsx_template(template, output, values)


if __name__ == "__main__":
    # Получаем от пользователя
    template = r'retire.docx'
    output = r'out.docx'

    process_docx()
