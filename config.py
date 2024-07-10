import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

REGEX_TAG = r'\{\{(.*?)\}\}'