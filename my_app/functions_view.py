from xml.dom.minidom import parseString

from dicttoxml import dicttoxml
from flask import Response, jsonify, make_response
from report_of_monaco_racing import Racer, groper, sort_racers

from my_app.my_settings.constants import FormatEnum


class HandleMyData:
    def __init__(self, location: str) -> None:
        self._drivers_data = groper(location)

    def sort_racers_list(self, order_bool: bool):
        return sort_racers(self._drivers_data, order_bool)

    def racers_list_of_full_dict(self, racers: list[Racer]) -> list[dict]:
        return [self.racer_to_full_dict(racer) for racer in racers]

    def racers_list_of_small_dict(self) -> list[dict]:
        return [self.racer_to_small_dict(racer) for racer in self._drivers_data]

    def racer_to_full_dict(self, racer: Racer) -> dict:
        return {"abbr": self.get_abbr(racer),
                "fullname": racer.fullname,
                "team": racer.team,
                "time": str(racer.best_lap)}

    def racer_to_small_dict(self, racer: Racer) -> dict:
        return {"abbr": self.get_abbr(racer),
                "fullname": racer.fullname}

    def racers_add_place(self, racers_list_of_dict: list[dict]) -> list[dict]:
        for index in range(0, len(racers_list_of_dict)):
            racers_list_of_dict[index] = self.add_place(racers_list_of_dict[index], index + 1)
        return racers_list_of_dict

    def find_racer(self, driver_id: str) -> Racer | None:
        for driver in self.get_drivers_data():
            driver_abbr = self.get_abbr(driver)
            if driver_abbr == driver_id:
                return driver

    def get_drivers_data(self) -> list[Racer]:
        return self._drivers_data

    @staticmethod
    def add_place(racer_dict: dict, place) -> dict:
        racer_dict["place"] = place
        return racer_dict

    @staticmethod
    def get_abbr(driver: Racer) -> str:
        name_split = driver.fullname.split()
        driver_abbr = name_split[0][0] + name_split[1][0] + driver.team[0]
        return driver_abbr


def format_handle(racers_list_or_dict: list[dict] | dict, form: str | None) -> Response | str:
    if form:
        form = FormatEnum(form)

        if form == FormatEnum.xml:
            xml = dicttoxml(racers_list_or_dict, attr_type=False)
            dom = parseString(xml)

            return dom.toprettyxml()

    return jsonify(racers_list_or_dict)


def format_check(form: str | None, racers_list_or_dict: list[dict] | dict, code: int) -> Response:
    data = format_handle(racers_list_or_dict, form)

    return make_response(data, code)
