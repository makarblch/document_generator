from docx2pdf import convert
from tools.utilities import create_input_path, create_output_path


def convert_to_pdf(input_file, output_file):
    try:
        convert(create_input_path(input_file), create_output_path(output_file))
    except:
        pass