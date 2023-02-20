from flask import render_template, request

from my_app import app
from my_app.constants import OrderEnum
from my_app.functions_view import form_racers, racer_to_str


@app.route("/")
@app.route("/report")
def report() -> str:
    return render_template("report.html")


@app.route("/report/drivers")
def drivers() -> str:
    args = request.args.to_dict()
    order_bool = False

    if args:
        order = OrderEnum(args.get("order"))

        if order == OrderEnum.desc:
            order_bool = True

        elif order == OrderEnum.asc:
            order_bool = False

    return render_template("drivers.html", racers=form_racers(order_bool))


@app.route("/report/drivers/driver_id=<driver_id>")
def single_driver(driver_id: str) -> str:
    racer_info = racer_to_str(driver_id)
    return render_template("driver_info.html", racer_info=racer_info)
