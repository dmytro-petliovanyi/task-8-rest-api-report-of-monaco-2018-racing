import datetime

import pytest
from report_of_monaco_racing import Racer

from my_app import app
from my_app.my_settings.config import DefaultConfig

full_list_of_dict_for_test_with_place = [
    {
        "abbr": "DRR",
        "fullname": "Daniel Ricciardo",
        "place": 1,
        "team": "RED BULL RACING TAG HEUER",
        "time": "0:02:47.987000"
    },
    {
        "abbr": "SVF",
        "fullname": "Sebastian Vettel",
        "place": 2,
        "team": "FERRARI",
        "time": "0:01:04.415000"
    },
    {
        "abbr": "LHM",
        "fullname": "Lewis Hamilton",
        "place": 3,
        "team": "MERCEDES",
        "time": "0:06:47.540000"
    }
]

full_list_of_dict_for_test = [
    {
        "abbr": "DRR",
        "fullname": "Daniel Ricciardo",
        "team": "RED BULL RACING TAG HEUER",
        "time": "0:02:47.987000"
    },
    {
        "abbr": "SVF",
        "fullname": "Sebastian Vettel",
        "team": "FERRARI",
        "time": "0:01:04.415000"
    },
    {
        "abbr": "LHM",
        "fullname": "Lewis Hamilton",
        "team": "MERCEDES",
        "time": "0:06:47.540000"
    }
]

small_list_of_dict_for_test = [
    {
        "abbr": "DRR",
        "fullname": "Daniel Ricciardo",
    },
    {
        "abbr": "SVF",
        "fullname": "Sebastian Vettel",
    },
    {
        "abbr": "LHM",
        "fullname": "Lewis Hamilton"
    }
]

racers_for_patch = [
        Racer(
            'Daniel Ricciardo',
            'RED BULL RACING TAG HEUER',
            datetime.time(12, 14, 12, 54000),
            datetime.time(12, 11, 24, 67000)
        ),
        Racer(
            'Sebastian Vettel',
            'FERRARI',
            datetime.time(12, 2, 58, 917000),
            datetime.time(12, 4, 3, 332000)
        ),
        Racer(
            'Lewis Hamilton',
            'MERCEDES',
            datetime.time(12, 18, 20, 125000),
            datetime.time(12, 11, 32, 585000)
        )
    ]


@pytest.fixture
def client():
    app.config.from_object(DefaultConfig)
    with app.test_client() as client:
        yield client


racers_dict = {
    "DRR": "Daniel Ricciardo | RED BULL RACING TAG HEUER | 2:47.987",
    "SVF": "Sebastian Vettel | FERRARI | 1:04.415",
    "LHM": "Lewis Hamilton | MERCEDES | 6:47.545"
}
