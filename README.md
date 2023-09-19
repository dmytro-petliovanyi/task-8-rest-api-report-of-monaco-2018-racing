# Task 8 - REST API report of monaco 2018 racing


<img alt="Static Badge" src="https://img.shields.io/badge/flask-2.2.3-orange">
<img alt="Static Badge" src="https://img.shields.io/badge/python-3.10-blue">
<img alt="Static Badge" src="https://img.shields.io/badge/task_6_report_of_monaco_2018_racing_by_petliovany-0.0.4-red">
<img alt="Static Badge" src="https://img.shields.io/badge/flask_restful-0.3.9-violet">
<img alt="Static Badge" src="https://img.shields.io/badge/dicttoxml-1.7.16-white">
<img alt="Static Badge" src="https://img.shields.io/badge/flasgger-0.9.5-yellow">
<img alt="Static Badge" src="https://img.shields.io/badge/pytest-7.2.2-black">


## Swagger docs: http://localhost:5000/apidocs/

### Contains resources:

#### /api/v1/report/

    Returns a list of all reports

    Has 2 query parameters:
        format: The format of the response (json or xml)
        order: The order to sort drivers (asc or desc)

    responces:
        200:[
              {
                "abbr": "SVF",
                "fullname": "Sebastian Vettel",
                "team": "FERRARI",
                "time": "0:01:04.415000"
              }
            ]

#### /api/v1/report/drivers/

    Get a list of all drivers

    Has 1 query parameters:
        format: The format of the response (json or xml)

    responces:
        200:[
              {
                "abbr": "SVF",
                "fullname": "Sebastian Vettel"
              }
            ]

#### /api/v1/report/drivers/{driver_id}/

    Returns the driver with the specified ID

    Has 2 parameters:
        format(query): The format of the response (json or xml)
        driver_id(path): The order to sort drivers (asc or desc)

    responces:
        200:{
                "abbr": "SVF",
                "fullname": "Sebastian Vettel",
                "team": "FERRARI",
                "time": "0:01:04.415000"
             }

        404: Driver not found
