from typing import Dict, List, Any
import pyxb
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

def to_flat_dict(obj: Any, include_attr: bool=False, delimiter: str='/', start_idx: int=0) -> dict:
    '''Flatten a witsml object into a flat dict

    Args:
        obj(Any): A witsml object for example obj_trajectory, obj_mudLog etc
        include_attr(bool):Also take attributes
        delimiter(str): Deplimiter for nested elements, default . as in python
        start_idx(int): Start index for items in list, default 0

    Returns:
        flat_dict(dict): A flatten dict representation of the witsml obj
    '''

    obj_list = [('', obj)]

    flatten_witsml = {}

    while obj_list:
        witsml.obj_bhaRun
        base_name, obj = obj_list.pop()

        if isinstance(obj, pyxb.binding.content._PluralBinding):
            for i, item in enumerate(obj):
                obj_list.append((f'{base_name}[{start_idx}]', item))
        
        if obj._ContentTypeTag in (obj._CT_EMPTY, obj._CT_SIMPLE):

            for cont in obj.orderedContent():

                if cont.elementDeclaration is not None:

                    next_path = delimiter.join(filter(None, [base_name, cont.elementDeclaration.id()]))
                    next_obj = obj._ElementMap[cont.elementDeclaration.name()].value(obj)
                    obj_list.append((next_path, next_obj))
        
        else:
            value = obj
            if obj._CT_SIMPLE == obj._ContentTypeTag:
                value = value.value()
    
            flatten_witsml[base_name] = value

        if include_attr:
            for key, value in obj._AttributeMap.items():
                print(key, value)

    return flatten_witsml

