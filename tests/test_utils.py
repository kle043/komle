import pytest
from komle.utils import log_to_dict

sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'samples')

def test_log_to_dict():
    with open(os.path.join(sample_path, 'small_depth_log.xml'), 'r') as test_file:
        logs = witsml.CreateFromDocument(test_file.read())
    
    log_dict = log_to_dict(logs.log[0])
