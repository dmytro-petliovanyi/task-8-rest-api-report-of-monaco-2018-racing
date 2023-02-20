from unittest.mock import patch

from test_my_app.conftest import racers_dict


def test_index_route(client):
    response2 = client.get("/")

    assert response2.status_code == 200
    assert "Report" in response2.data.decode("utf-8")


def test_report_route(client):
    response = client.get("/report")

    assert response.status_code == 200
    assert "Report" in response.data.decode("utf-8")


@patch("my_app.views.form_racers", return_value=racers_dict)
def test_drivers_default_route(patch_form_racers, client):
    response = client.get("/report/drivers")
    patch_form_racers.assert_called()
    assert response.status_code == 200
    assert all(value in response.data.decode("utf-8") for value in racers_dict.values()) is True


@patch("my_app.views.form_racers", return_value=racers_dict)
def test_drivers_desc_route(patch_form_racers, client):
    response = client.get("/report/drivers?order=desc")
    patch_form_racers.assert_called()
    assert response.status_code == 200
    assert all(value in response.data.decode("utf-8") for value in racers_dict.values()) is True


@patch("my_app.views.form_racers", return_value=racers_dict)
def test_drivers_asc_route(patch_form_racers, client):
    response = client.get("/report/drivers?order=asc")
    patch_form_racers.assert_called()
    assert response.status_code == 200
    assert all(value in response.data.decode("utf-8") for value in racers_dict.values()) is True


@patch("my_app.views.racer_to_str", return_value=racers_dict["DRR"])
def test_drivers_single_driver(patch_racer_to_str, client):
    response = client.get("/report/drivers/driver_id=DRR")
    patch_racer_to_str.assert_called()
    assert response.status_code == 200
    assert racers_dict["DRR"] in response.data.decode("utf-8")
