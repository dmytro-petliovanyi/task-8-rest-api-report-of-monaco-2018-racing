from enum import Enum

swagger_config = {
    'title': 'My API'
}


class OrderEnum(str, Enum):
    desc = "desc"
    asc = "asc"


class FormatEnum(str, Enum):
    json = "json"
    xml = "xml"
