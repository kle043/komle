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

