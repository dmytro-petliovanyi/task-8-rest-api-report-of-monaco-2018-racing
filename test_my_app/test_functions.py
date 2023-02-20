from unittest.mock import patch

from my_app.functions_view import form_racers, get_abbr, racer_to_str
from test_my_app.conftest import racers_for_patch


@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("my_app.app.config", return_value="some_text")
def test_racer_to_str_works_as_expected(patch_config,
                                        patch_groper):
    result = racer_to_str("DRR")
    patch_groper.assert_called()
    assert result == "Daniel Ricciardo              | RED BULL RACING TAG HEUER     | 2:47.987"


@patch("my_app.functions_view.get_abbr")
@patch("my_app.functions_view.sort_racers", return_value=sorted(racers_for_patch))
@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("my_app.app.config", return_value="some_text")
def test_form_racers_works_as_expected(patch_config,
                                       patch_groper,
                                       patch_get_racer,
                                       patch_get_abbr):
    patch_get_abbr.side_effect = ["SVF", "DRR", "LHM"]
    result = form_racers()
    patch_get_abbr.assert_called()
    patch_get_racer.assert_called()
    patch_groper.assert_called()
    assert result == {"SVF": "Sebastian Vettel              | FERRARI                       | 1:04.415",
                      "DRR": "Daniel Ricciardo              | RED BULL RACING TAG HEUER     | 2:47.987",
                      "LHM": "Lewis Hamilton                | MERCEDES                      | 6:47.54"}


def test_get_abbr_works_as_expected():
    assert [get_abbr(racer) for racer in racers_for_patch] == ["DRR", "SVF", "LHM"]
