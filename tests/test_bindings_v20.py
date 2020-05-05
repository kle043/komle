import os
import pytest
from pyxb.namespace import Namespace, utility

sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'samples')

@pytest.fixture(scope="module", autouse=True)
def setup():
    # If running all the tests at once, we can't have two equal namespaces
    # So reset in case read_bindings is loaded and load the write_binding
    for name in utility.AvailableNamespaces():
        getattr(super(Namespace, name), '_reset', lambda *args, **kw: None)()
        name._Namespace__initialNamespaceContext =  None

    from komle.bindings.v20 import witsml
    global witsml
    yield

    for name in utility.AvailableNamespaces():
        getattr(super(Namespace, name), '_reset', lambda *args, **kw: None)()
        name._Namespace__initialNamespaceContext =  None


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






