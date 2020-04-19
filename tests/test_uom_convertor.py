import pytest

from komle.uom_converter import conversion_factor

@pytest.mark.parametrize('source,target,expected', 
                        [('m', 'ft', 3.280839895013123),
                         ('ft','m', 0.3048),
                        ])
def test_conversion_factor(source, target, expected):

    assert conversion_factor(source, target) == expected