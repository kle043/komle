from typing import Dict, List
from komle.read_bindings import witsml

LOG_PRIM_TYPES = {'byte': bytes,
                  'date time': witsml.timestamp,
                  'double': float,
                  'float': float,
                  'int': int,
                  'long': int,
                  'short': int,
                  'string': str,
                  'string40': str,
                  'string16': str,
                  'unknown': str
                 }

def pretty_save(element, file_path:str):
    with open(file_path, 'w') as xml_file:
        xml_file.write(element.toDOM().toprettyxml())

def logdata_to_dict(log: witsml.obj_log, fill_missing: bool=True) -> Dict[str, List[witsml.LogDataType]]:
    '''Convert logData from a witsml log to a dict

    Args:
        log(witsml.obj_log): The log to extract logData from
        fill_missing(bool): If True set missing data to None, else ignore 

    Returns:
       Dict[str, List[witsml.LogDataType]]: A dict with each mnemonic as key and a list as value,
                                            where values are logData.data for the given mnemonic
    '''
    
    mnem_cast_map = {c.mnemonic.value(): LOG_PRIM_TYPES[c.typeLogData] for c in log.logCurveInfo}
    
    # The default delimiter is , 
    delimiter = ',' if log.dataDelimiter is None else log.dataDelimiter
    
    data_list = [(mnem, mnem_cast_map[mnem], []) for mnem in log.logData[0].mnemonicList.split(delimiter)]

    for data_str in log.logData[0].data:
        for i, point_str in enumerate(data_str.split(delimiter)):
            if point_str:
                value_cast = data_list[i][1]
                data_list[i][2].append(value_cast(point_str))

            elif fill_missing:
                data_list[i][2].append(None)
    
    return {mnem:values for mnem, _, values in data_list}

