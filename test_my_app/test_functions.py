from unittest.mock import patch

from my_app.functions_view import HandleMyData
from test_my_app.conftest import (full_list_of_dict_for_test,
                                  full_list_of_dict_for_test_with_place,
                                  racers_for_patch,
                                  small_list_of_dict_for_test)


@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("my_app.functions_view.HandleMyData.get_drivers_data", return_value=racers_for_patch)
@patch("my_app.app.config", return_value="some_text")
def test_find_racer_works_as_expected(patch_config,
                                      patch_get_driver_data,
                                      patch_groper):
    handle = HandleMyData("")
    result = handle.find_racer("DRR")
    patch_get_driver_data.assert_called()
    patch_groper.assert_called()
    assert result == racers_for_patch[0]


@patch("my_app.functions_view.HandleMyData.racer_to_full_dict", side_effect=full_list_of_dict_for_test)
@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("my_app.app.config", return_value="some_text")
def test_racers_list_of_full_dict_works_as_expected(patch_config,
                                                    patch_groper,
                                                    patch_racer_to_full_dict):
    handle = HandleMyData("")
    result = handle.racers_list_of_full_dict(racers_for_patch)
    patch_groper.assert_called()
    patch_racer_to_full_dict.assert_called()
    assert result == full_list_of_dict_for_test


@patch("my_app.functions_view.HandleMyData.racer_to_small_dict", side_effect=small_list_of_dict_for_test)
@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("my_app.app.config", return_value="some_text")
def test_racers_list_of_small_dict_works_as_expected(patch_config,
                                                     patch_groper,
                                                     patch_racer_to_small_dict):
    handle = HandleMyData("")
    result = handle.racers_list_of_small_dict(racers_for_patch)
    patch_groper.assert_called()
    patch_racer_to_small_dict.assert_called()
    assert result == small_list_of_dict_for_test


@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("my_app.app.config", return_value="some_text")
def test_racer_to_full_dict(patch_config,
                            patch_groper):
    handle = HandleMyData("")
    result = handle.racer_to_full_dict(racers_for_patch[0])
    patch_groper.assert_called()
    assert result == full_list_of_dict_for_test[0]


@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("my_app.app.config", return_value="some_text")
def test_racer_to_small_dict(patch_config,
                             patch_groper):
    handle = HandleMyData("")
    result = handle.racer_to_small_dict(racers_for_patch[0])
    patch_groper.assert_called()
    assert result == small_list_of_dict_for_test[0]


@patch("my_app.functions_view.HandleMyData.add_place", side_effect=full_list_of_dict_for_test_with_place)
@patch("my_app.functions_view.groper", return_value=racers_for_patch)
def test_racers_add_place(patch_groper,
                          patch_add_place):
    handle = HandleMyData("")
    result = handle.racers_add_place(full_list_of_dict_for_test)
    patch_groper.assert_called()
    patch_add_place.assert_called()
    assert full_list_of_dict_for_test_with_place == result


@patch("my_app.functions_view.HandleMyData.get_abbr", side_effect=["DRR", "SVF", "LHM"])
@patch("my_app.functions_view.HandleMyData.get_drivers_data", return_value=racers_for_patch)
@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("my_app.app.config", return_value="some_text")
def test_find_racer(patch_config,
                    patch_groper,
                    patch_get_data,
                    patch_get_abbr):
    handle = HandleMyData("")
    result = handle.find_racer("DRR")
    patch_groper.assert_called()
    patch_get_data.assert_called()
    patch_get_abbr.assert_called()
    assert result == racers_for_patch[0]


@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("my_app.app.config", return_value="some_text")
def test_get_drivers_data(patch_config,
                          patch_groper):
    handle = HandleMyData("")
    result = handle.get_drivers_data()
    patch_groper.assert_called()
    assert result == racers_for_patch


@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("my_app.app.config", return_value="some_text")
def test_add_place(patch_config,
                   patch_groper):
    handle = HandleMyData("")
    result = handle.add_place(full_list_of_dict_for_test[0], 1)
    patch_groper.assert_called()
    assert result == full_list_of_dict_for_test_with_place[0]


@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("my_app.app.config", return_value="some_text")
def test_get_abbr_works_as_expected(patch_config,
                                    patch_groper):
    handle = HandleMyData("")
    result = [handle.get_abbr(racer) for racer in racers_for_patch]
    patch_groper.assert_called()
    assert result == ["DRR", "SVF", "LHM"]
