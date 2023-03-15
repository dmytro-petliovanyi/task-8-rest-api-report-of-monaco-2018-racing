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
        racers_list = handle.racers_list_of_dict(handle.get_drivers_data())

        return make_response(format_check(args, racers_list), 200)


class Drivers(Resource):
    @swag_from('swagger/drivers.yml')
    def get(self) -> Response:
        handle = HandleMyData(app.config['TARGET_DIR'])
        args = request.args
        racers_list = handle.get_drivers_data()
        order_bool = False

        if args.get("order"):
            order = OrderEnum(args.get("order"))

            order_bool = True if order == OrderEnum.desc else False

        ordered_racers_list = handle.sorted_racers(racers_list, order_bool)
        racers_list_of_dict = handle.racers_list_of_dict(ordered_racers_list)
        num_racers_list_of_dict = handle.racers_add_place(racers_list_of_dict)

        return make_response(format_check(
            args, num_racers_list_of_dict
        ), 200)


class Driver(Resource):
    @swag_from("swagger/driver.yml")
    def get(self, driver_id: str) -> Response:
        handle = HandleMyData(app.config['TARGET_DIR'])
        args = request.args.to_dict()

        if driver_id:
            driver = handle.find_racer(driver_id)
            if driver:
                driver_dict = handle.racer_to_dict(driver)

                return make_response(format_check(args, driver_dict), 200)

        return make_response(jsonify({404: "Driver not found"}), 404)
