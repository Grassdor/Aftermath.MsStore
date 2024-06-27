"""Some useful stuff"""


def camel_case_generator(field_name: str):
    """Pydantic camel case generator"""
    init, *temp = field_name.split('_')
    return ''.join([init.lower(), *map(str.title, temp)])
