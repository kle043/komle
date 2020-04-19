import os
from komle.uom_bindings import uom

with open(os.path.join(os.path.dirname(__file__), "witsmlUnitDict.xml"), 'r') as uom_file:
    witsm_unit_dict = uom.CreateFromDocument(uom_file.read())

def conversion_factor(source: str, target: str='base') -> float:
    '''Retrieve a witsml convertion factor for a given unit to a target unit.

    Uses the witsml unit dict as a lookup of unit conversion factors

    Args:
        source (str): id of the source witsml uom
        targer (str): id of target uom, default returns base unit

    Returns:
        factor (float): multiplication factor for conversion
    '''

    return 0.0

