from flasgger import swag_from
from flask import Response, jsonify, make_response, request
from flask_restful import Resource

from my_app import app
from my_app.functions_view import HandleMyData, format_check
from my_app.my_settings.constants import OrderEnum


class Report(Resource):
    @swag_from('swagger/report.yml')
    def get(self) -> Response:
        handle = HandleMyData(app.config['TARGET_DIR'])
        args = request.args.to_dict()
        order_bool = False

        if args.get("order"):
            order = OrderEnum(args.get("order"))

            order_bool = True if order == OrderEnum.desc else False

        racers_list = handle.racers_list_of_full_dict(handle.sort_racers_list(order_bool))

        racers_list = handle.racers_add_place(racers_list)

        return format_check(args.get("format"), racers_list, 200)


class Drivers(Resource):
    @swag_from('swagger/drivers.yml')
    def get(self) -> Response:
        handle = HandleMyData(app.config['TARGET_DIR'])
        args = request.args

        racers_list_of_dict = handle.racers_list_of_small_dict()

        return format_check(args.get("format"), racers_list_of_dict, 200)


class Driver(Resource):
    @swag_from("swagger/driver.yml")
    def get(self, driver_id: str) -> Response:
        handle = HandleMyData(app.config['TARGET_DIR'])
        args = request.args.to_dict()
        driver_id = driver_id.strip().upper()
        driver = handle.find_racer(driver_id)

        if driver:
            driver_dict = handle.racer_to_full_dict(driver)

            return format_check(args.get("format"), driver_dict, 200)

        return make_response(jsonify("Driver not found"), 404)
