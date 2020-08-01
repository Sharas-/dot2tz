import pytest
from geocoord import GeoCoord

def test_non_numeric_string_format():
    with pytest.raises(ValueError):
        GeoCoord("aa", "bb")

def test_nil_coord():
    with pytest.raises(ValueError):
        GeoCoord("50", None)

def test_empty_string_coord():
    with pytest.raises(ValueError):
        GeoCoord("50", "")

def test_out_of_bound_latitude():
    with pytest.raises(ValueError):
        GeoCoord("91", "180")

def test_out_of_bound_lontitude():
    with pytest.raises(ValueError):
        GeoCoord("50.302", "-181")

def test_good_coord_on_bounds():
     GeoCoord("-90", "180")
     GeoCoord("90", "-180")
     GeoCoord("-90", "-180")
