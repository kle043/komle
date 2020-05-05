'''A small witsml python example

Should be possible to run each cell denoted by #%% in vscode or atom(using hydrogen), 
or just run it using python3
'''


#%%

import os
from komle.bindings.v20 import witsml
from komle.uom_converter import conversion_factor, get_unit
from komle import utils as ku
import pandas as pd # Not included in komle setup.py

sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'tests', 'samples')

#%% Open a mud log and unmarshall it
 
with open(os.path.join(sample_path, 'Trajectory.xml'), 'r') as mud_file:
    traj = witsml.CreateFromDocument(mud_file.read())

# %%

print(traj.DTimTrajStart)

# %% Convert stations to dataframe

geo_dict = ku.plural_dict(traj.TrajectoryStation)
pd.DataFrame(geo_dict)



#%% Work with log files

with open(os.path.join(sample_path, 'Log.xml'), 'r') as log_file:
    # logs is a regular python object according to the witsml schema
    logs = witsml.CreateFromDocument(log_file.read())

#%%

print(logs.ChannelSet[0]._element().documentation())
# Need to walk the singular of the object, that is the list in the object

# Get the schema location for logCurveInfo
print(logs.ChannelSet[0]._element().xsdLocation().locationBase)

#%%

# It is helpful to pretty save the object we look at