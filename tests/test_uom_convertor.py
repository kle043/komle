import pytest

from komle.uom_converter import conversion_factor


@pytest.mark.parametrize(
    'source,target,expected',
    [
        ('m', 'ft', 3.280839895013123),
        ('ft', 'm', 0.3048),
        ('atm', 'Pa', 101325),
        ('atm', 'MPa', 0.101325),
        ('m/s', 'km/h', 3.5999999999999996),
        ('km/h', 'm/s', 1 / 3.6),
        ('kN.m', 'J', 1000),
    ],
)
def test_conversion_factor(source, target, expected):

    assert conversion_factor(source, target) == expected
