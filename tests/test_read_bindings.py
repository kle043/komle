import os
import pytest
from komle.bindings.v1411.read import witsml

sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'samples')

@pytest.mark.parametrize("test_filename", 
                        ["log.xml", 
                         "message.xml", 
                         "mudLog.xml", 
                         "risk.xml", 
                         "trajectory.xml", 
                         "wellbore.xml"])
def test_unmarshalling(test_filename):
    '''Test unmarshalling energistics well A test files'''
    with open(os.path.join(sample_path, test_filename), 'r') as test_file:
        obj = witsml.CreateFromDocument(test_file.read())






