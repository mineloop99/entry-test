from scripts.meta.model import EModel, ESearchValue


def search_input_val(search_num: str):
    search_num = search_num.lower()
    try:
        ESearchValue(search_num)
        return True
    except ValueError:
        return False


def model_input_val(model_num: str):
    model_num = model_num.lower()
    try:
        EModel(model_num)
        return True
    except ValueError:
        return False


def field_input_val(field: str, dict_: dict):
    field = field.lower()
    if field in dict_:
        return True
    return False
