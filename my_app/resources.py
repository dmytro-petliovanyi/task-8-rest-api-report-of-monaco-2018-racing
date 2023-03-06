from flask import request
from flask_restful import Resource

from my_app.constants import OrderEnum
from my_app.functions_view import (format_check, groper_from_config,
                                   num_racers_dict, racer_to_str,
                                   racers_to_dict, sorted_racers)


class Report(Resource):
    def get(self):
        args = request.args.to_dict()
        racers_dict = racers_to_dict(groper_from_config())

        return format_check(args, racers_dict)


class Drivers(Resource):
    def get(self):
        args = request.args.to_dict()
        racers_list = groper_from_config()

        if driver_id := args.get("driver_id"):
            driver_info = {driver_id: racer_to_str(driver_id)}
            return format_check(args, driver_info)

        elif args.get("order"):
            order = OrderEnum(args.get("order"))

            if order == OrderEnum.asc:
                racers_dict = num_racers_dict(sorted_racers(racers_list))

                return format_check(args, racers_dict)

            elif order == OrderEnum.desc:
                racers_dict = num_racers_dict(sorted_racers(racers_list, True))

                return format_check(args, racers_dict)

        return format_check(args, num_racers_dict(sorted_racers(racers_list)))
