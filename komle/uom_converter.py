import os
from komle.uom_bindings import uom

with open(os.path.join(os.path.dirname(__file__), "witsmlUnitDict.xml"), 'r') as uom_file:
    WITSM_UNIT_DICT = uom.CreateFromDocument(uom_file.read())

def conversion_factor(source: str, target: str='base') -> float:
    '''Retrieve a witsml convertion factor for a given unit to a target unit.

    Uses the witsml unit dict as a lookup of unit conversion factors

    Args:
        source (str): id of the source witsml uom
        targer (str): id of target uom, default returns base unit

    Returns:
        factor (float): multiplication factor for conversion
    '''
    source_unit = target_unit = None

    for unit in WITSM_UNIT_DICT.UnitsDefinition.UnitOfMeasure:
        if unit.id == source:
            source_unit = unit
        elif unit.id == target:
            target_unit = unit

    source_factor = target_factor = 1.0

    if source_unit.ConversionToBaseUnit is not None:
        source_factor = source_unit.ConversionToBaseUnit.Factor

    if target_unit.ConversionToBaseUnit is not None:
        target_factor = target_unit.ConversionToBaseUnit.Factor


    return source_factor / target_factor

