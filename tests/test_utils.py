import os
import pytest
from komle import utils as ku
from komle.read_bindings import witsml
from datetime import datetime

sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'samples')

@pytest.mark.parametrize("test_filename", 
                        ["log.xml",  
                         'small_depth_log.xml'])
def test_log_to_dict(test_filename):

    with open(os.path.join(sample_path, test_filename), 'r') as test_file:
        logs = witsml.CreateFromDocument(test_file.read())
    
    logdata_frame = ku.logdata_dict(logs.log[0])

    for mnem in logs.log[0].logData[0].mnemonicList.split(','):
        assert mnem in logdata_frame
    
    assert len(list(logdata_frame.values())[0]) == len(logs.log[0].logData[0].data)

    if logs.log[0].indexType == 'measured depth':
        assert isinstance(logdata_frame[logs.log[0].indexCurve][0], float)
    else:
        assert isinstance(logdata_frame[logs.log[0].indexCurve][0], datetime)



def test_obj_dict_risk():

    with open(os.path.join(sample_path, 'risk.xml'), 'r') as test_file:
        obj = witsml.CreateFromDocument(test_file.read())
    
    flatt_witsml = ku.obj_dict(obj.risk[0], True)

    assert flatt_witsml['mitigation[0]'] == 'Call the boss'
    assert flatt_witsml['mitigation[1]'] == 'Run for cover'
    assert flatt_witsml['uidWellbore'] == 'OC-bf-wb1'
    assert flatt_witsml['nameWellbore'] == 'Wellbore Test Bruce'
    assert len(flatt_witsml) == 45

def test_obj_dict_mudLog():

    with open(os.path.join(sample_path, 'mudLog.xml'), 'r') as test_file:
        obj = witsml.CreateFromDocument(test_file.read())
    
    print(type(obj))
    flatt_witsml = ku.obj_dict(obj.mudLog[0], True)
    assert flatt_witsml['commonData.comments'] == 'MudLog Object'
    assert len(flatt_witsml) == 1244

def test_plural_frame_geoIntervall():

    with open(os.path.join(sample_path, 'mudLog.xml'), 'r') as test_file:
        obj = witsml.CreateFromDocument(test_file.read())
    
    geo_frame = ku.plural_dict(obj.mudLog[0].geologyInterval, True)
    
    print(geo_frame)
    assert len(geo_frame) == 1244

def test_plural_frame_lithology():

    with open(os.path.join(sample_path, 'mudLog.xml'), 'r') as test_file:
        obj = witsml.CreateFromDocument(test_file.read())
    
    geo_frame = ku.plural_dict(obj.mudLog[0].geologyInterval[1].lithology, True)
    
    print(geo_frame)
    assert len(geo_frame) == 1244