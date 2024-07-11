from documents_processing import start_proccessor
actions = {'1': 'Process docx', '2': 'Process xlsx', '3': 'Save to pdf'}

if __name__ == "__main__":
    # Получаем от пользователя имя входного и выходного файла
    template = r'change_dates.docx'
    output = r'change_dates_out.docx'
    # Пользователь выбирает, что он хочет
    action = 1
    match action:
        case 1:
            start_proccessor.process_docx(template, output)
        case 2:
            start_proccessor.process_xlsx(template, output)
        case 3:
            start_proccessor.process_pdf(template, output)


