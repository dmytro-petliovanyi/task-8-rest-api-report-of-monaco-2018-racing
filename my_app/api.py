from flasgger import Swagger
from flask_restful import Api

from my_app import app
from my_app.resources import Driver, Drivers, Report

api = Api(app)
swagger = Swagger(app)


api.add_resource(Report, '/api/v1/report/')
api.add_resource(Drivers, '/api/v1/report/drivers/')
api.add_resource(Driver, '/api/v1/report/drivers/<driver_id>/')
