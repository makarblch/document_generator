from documents_processing import docx_processor, xlsx_processor, pdf_processor
from tools.tags import check_tags, popular_tags


def process_docx(template, output):
    # Получаем все теги, которые есть в данном шаблоне
    tags = docx_processor.get_all_tags(template)
    # print(tags)
    # Пользователь заполняет тэги
    values = dict()
    for element in tags:
        if check_tags(str(element)):
            print(f"Введите: {popular_tags[element]}")
        else:
            print(f"Введите: {element}")
        values[element] = input()
    docx_processor.fill_docx_template(template, output, values)


def process_xlsx(template, output):
    # Получаем все теги, которые есть в данном шаблоне
    tags = docx_processor.get_all_tags(template)
    # print(tags)
    # Пользователь заполняет тэги
    values = dict()
    for element in tags:
        if check_tags(element):
            print(f"Input {popular_tags[element]}: ")
        else:
            print(f"Input {element}: ")
        values[element] = input()
    xlsx_processor.fill_xlsx_template(template, output, values)


def process_pdf(template, output):
    pdf_processor.convert_to_pdf(template, output)