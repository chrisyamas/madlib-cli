import re

def read_template(text_file):
    try:
        with open(text_file) as madlib:
            return madlib.read()
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(template):
    stripped = re.sub(r'{[^}]*}', '{}', template)
    parts = re.findall(r'{(.*?)}', template)
    return stripped, tuple(parts)

def merge(template, content):
    return template.format(*content)