import os
import pytest
from komle.bindings.v20 import witsml
from pyxb.namespace import Namespace, utility

sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'samples')

@pytest.mark.parametrize("test_filename", 
                        ["BhaRun.xml",
                         "Log.xml", 
                         "MudLogReport.xml",
                         "Trajectory.xml",
                         "Tubular.xml",
                         "Well.xml",
                         "Wellbore.xml"
                        ])
def test_unmarshalling(test_filename):
    '''Test unmarshalling energistics well A test files'''
    with open(os.path.join(sample_path, test_filename), 'r') as test_file:
        obj = witsml.CreateFromDocument(test_file.read())






