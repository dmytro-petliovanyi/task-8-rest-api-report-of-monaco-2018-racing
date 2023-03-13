from flasgger import swag_from
from flask import jsonify, make_response, request
from flask_restful import Resource

from my_app.constants import OrderEnum
from my_app.functions_view import HandleMyData

handle = HandleMyData()


class Report(Resource):
    @swag_from('swagger/report.yml')
    def get(self):
        args = request.args.to_dict()
        racers_dict = handle.racers_to_dict(handle.groper_from_config())

        return make_response(handle.format_check(args, racers_dict), 200)


class Drivers(Resource):
    @swag_from('swagger/drivers.yml')
    def get(self):
        args = request.args.to_dict()
        racers_list = handle.groper_from_config()
        order_bool = False

        if args.get("order"):
            order = OrderEnum(args.get("order"))

            if order == OrderEnum.asc:
                order_bool = False

            elif order == OrderEnum.desc:
                order_bool = True

        return make_response(handle.format_check(
            args, handle.num_racers_dict(handle.sorted_racers(racers_list, order_bool))
        ), 200)


class Driver(Resource):
    @swag_from("swagger/driver.yml")
    def get(self, driver_id: str):
        args = request.args.to_dict()

        if driver_id:
            driver_info = {driver_id: handle.racer_to_str(driver_id)}

            if driver_info[driver_id]:
                return make_response(handle.format_check(args, driver_info), 200)

            return make_response(jsonify("Driver not found"), 404)
