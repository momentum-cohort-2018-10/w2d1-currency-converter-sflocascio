
import pytest
import currency
from currency import convert

def test_match():
    assert convert([], 1, _from="USD", to="USD") == 1
    assert convert([], 2, _from="USD", to="USD") == 2

def test_convert_using_multiplication():
    assert round(convert[("USD", "EUR", 0.74])], value=1, current='USD',to='EUR') == 0.74
    assert round(convert(rates=[("USD", "EUR", 0.74)], value=3, current='USD', to='EUR'), 2) == 2.22

def test_convert_using_division():
    assert round(convert(
        rates=[("USD", "EUR", 0.74)], value=1, current='EUR', to='USD'), 2) == 2.22

def test_convert_multiple_rates():
    rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]
    assert round(convert(rates, value=10, current ="USD", to="EUR"), 2) == 7.4
    assert round(convert(rates, value=10, current ="EUR", to="USD"), 2) == 13.51
    assert round(convert(rates, value=10, current ="EUR", to="JPY"), 2) == 1459.49
    assert round(convert(rates, value=10, current ="JPY", to="EUR"), 2) == 0.69

def test_converting_with_no_matching_rates():
    rates = [("EUR", "JPY", 145.949)]
    with pytest.raises(ValueError):
        convert(rates, value=10, current='EUR', to='MXN')