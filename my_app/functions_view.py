from xml.dom.minidom import parseString

from dicttoxml import dicttoxml
from flask import Response, jsonify
from report_of_monaco_racing import Racer, groper, sort_racers

from my_app import app
from my_app.constants import FormatEnum


def racer_to_str(driver_id: str) -> str | None:
    drivers = groper(app.config["TARGET_DIR"])
    for driver in drivers:
        driver_abbr = get_abbr(driver)
        if driver_abbr == driver_id:
            return str(driver)


def groper_from_config() -> list[Racer]:
    return groper(app.config["TARGET_DIR"])


def sorted_racers(racers: list[Racer], reverse: bool = False) -> list[Racer]:
    return sort_racers(racers, reverse)


def racers_to_dict(racers: list[Racer]) -> dict:
    return {get_abbr(racer): str(racer) for racer in racers}


def num_racers_dict(racers: list[Racer]):
    return {racers.index(racer) + 1: str(racer) for racer in racers}


def get_abbr(driver: Racer) -> str:
    name_split = driver.fullname.split()
    driver_abbr = name_split[0][0] + name_split[1][0] + driver.team[0]
    return driver_abbr


def format_check(args: dict, racers_dict: dict) -> Response | str:
    if args.get("format"):
        form = FormatEnum(args.get("format"))

        if form == FormatEnum.json:
            return jsonify(racers_dict)

        elif form == FormatEnum.xml:
            xml = dicttoxml(racers_dict, attr_type=False)
            dom = parseString(xml)

            return dom.toprettyxml()

    return jsonify(racers_dict)
