import os
from typing import Union

from komle.bindings import uom

with open(
    os.path.join(os.path.dirname(__file__), "witsmlUnitDict.xml"), "r"
) as uom_file:
    WITSM_UNIT_DICT = uom.CreateFromDocument(uom_file.read())


def __get_factor(unit: uom.unitDictionaryType):

    factor = 1.0

    if unit.ConversionToBaseUnit is not None:
        if unit.ConversionToBaseUnit.Factor is not None:
            factor = unit.ConversionToBaseUnit.Factor
        elif (
            unit.ConversionToBaseUnit.Fraction.Numerator is not None
            and unit.ConversionToBaseUnit.Fraction.Denominator is not None
        ):
            factor = (
                unit.ConversionToBaseUnit.Fraction.Numerator
                / unit.ConversionToBaseUnit.Fraction.Denominator
            )

    elif unit.BaseUnit is None:

        raise ValueError(f'{unit.id} does not have a conversion to base unit')

    return factor


def conversion_factor(source_uom: str, target_uom: str) -> float:
    """Retrieve a witsml convertion factor for a given unit to a target_uom unit.

    Uses the witsml unit dict as a lookup of unit conversion factors

    Args:
        source_uom (str): annotation of the source_uom for example m, ft, m/s, km/h etc
        target_uom (str): annotation of target_uom for example m, ft,m/s, km/h etc

    Returns:
        factor (float): multiplication factor for conversion from source_uom
    """

    source_unit = target_unit = None

    for unit in WITSM_UNIT_DICT.UnitsDefinition.UnitOfMeasure:
        if unit.annotation == source_uom:
            source_unit = unit
        elif unit.annotation == target_uom:
            target_unit = unit

        if source_unit is not None and target_unit is not None:
            break

    if source_unit is None or target_unit is None:
        raise KeyError("Unit not found")

    source_factor = __get_factor(source_unit)
    target_factor = __get_factor(target_unit)

    return source_factor / target_factor


def get_unit(uom_str: str) -> Union[uom.unitDictionaryType, None]:
    """Print witsml uom info

    Args:
        uom (str): annotation of the uom for example, m,m/s etc

    Returns:
        uom.unitDictionaryType, None: a witsml unit for the given unit annotation, or None if not found.
    """

    for unit in WITSM_UNIT_DICT.UnitsDefinition.UnitOfMeasure:
        if unit.annotation == uom_str:
            return unit

    return None
