from enum import Enum

from my_app.functions_view import form_racers


class OrderEnum(str, Enum):
    desc = "desc"
    asc = "asc"


class FormatEnum(str, Enum):
    json = "json"
    xml = "xml"


racers_dict = form_racers()
