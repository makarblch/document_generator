import config
import os
import re


def create_input_path(template_path: str):
    return os.path.join(config.TEMPLATE_DIR, template_path)


def create_output_path(output_path: str):
    return os.path.join(config.OUTPUT_DIR, output_path)


def clear_string(text: str):
    text = text.strip()
    # Убираем нижние подчеркивания, обозначающие места для записи данных
    text = re.sub(r'_', '', text)
    # Убираем двойные пробелы
    text = re.sub(r' {2}', ' ', text)
    # Для мест, где надо вписать последние 2 цифры года, уберем лишние пробелы
    text = re.sub(r'20 (\d{2,})', r'20\1', text)
    return text
