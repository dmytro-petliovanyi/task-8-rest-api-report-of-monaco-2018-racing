from flask_restful import Api

from my_app import app
from my_app.resources import Drivers, Report

api = Api(app)


api.add_resource(Report, '/api/v1/report/')
api.add_resource(Drivers, '/api/v1/report/drivers/')
