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
    
    logdata_dict = ku.logdata_to_dict(logs.log[0])

    for mnem in logs.log[0].logData[0].mnemonicList.split(','):
        assert mnem in logdata_dict
    
    assert len(list(logdata_dict.values())[0]) == len(logs.log[0].logData[0].data)

    if logs.log[0].indexType == 'measured depth':
        assert isinstance(logdata_dict[logs.log[0].indexCurve][0], float)
    else:
        assert isinstance(logdata_dict[logs.log[0].indexCurve][0], datetime)


@pytest.mark.parametrize("test_filename,attr", 
                        [("risk.xml", 'risk'),  
                         ])
def test_to_flat_dict(test_filename, attr):

    with open(os.path.join(sample_path, 'risk.xml'), 'r') as test_file:
        obj = witsml.CreateFromDocument(test_file.read())
    
    flatt_witsml = ku.to_flat_dict(obj.risk[0], True)

    assert flatt_witsml['mitigation[0]'] == 'Call the boss'
    assert flatt_witsml['mitigation[1]'] == 'Run for cover'
    assert flatt_witsml['uidWellbore'] == 'OC-bf-wb1'
    assert flatt_witsml['nameWellbore'] == 'Wellbore Test Bruce'
    assert len(flatt_witsml) == 45