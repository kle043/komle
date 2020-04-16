import os
import pytest
from komle.read_bindings import witsml

sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'samples')

@pytest.mark.parametrize("test_filename", ["log.xml", 
                                           "message.xml", 
                                           "mudLog.xml", 
                                           "risk.xml", 
                                           "trajectory.xml", 
                                           "wellbore.xml"])
def test_eval(test_filename):
    print(os.path.join(sample_path, test_filename))
    with open(os.path.join(sample_path, test_filename), 'r') as test_file:
        obj = pywitsml.CreateFromDocument(test_file.read())






