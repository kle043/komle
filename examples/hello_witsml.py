'''A small witsml python example

Should be possible to run each cell denoted by #%% in vscode or atom(using hydrogen), 
or just run it using python3
'''


#%%

import os
from komle.bindings.v1411.read import witsml
from komle.soap_client import StoreClient
from komle.uom_converter import conversion_factor, get_unit
from komle import utils as ku
import pandas as pd # Not included in komle setup.py

sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'tests', 'samples')

#%% Open a mud log and unmarshall it
 
with open(os.path.join(sample_path, 'mudLog.xml'), 'r') as mud_file:
    mud_logs = witsml.CreateFromDocument(mud_file.read())

# %%

print(mud_logs.mudLog[0].name)
# it is convenient with a pretty xml 
ku.pretty_save(mud_logs, 'mudlog.xml')

# %% Take the mudLog, mud_logs is a container for several mudLog

mud_log = mud_logs.mudLog[0]
print(f'nameWellbore = {mud_log.nameWellbore}')
print(f'Start {mud_log.startMd.value()} {mud_log.startMd.uom}')
for geo_int in mud_log.geologyInterval:
    # need to call value on leaf nodes with attributes
    print(f'{geo_int.mdBottom.value()} - {geo_int.mdTop.value()}  {geo_int.mdTop.uom}')
    for lit in geo_int.lithology:
        print(f'Lit: {lit.lithPc.value()} {lit.lithPc.uom}')

# %% Construct a dictonary out of the plural geologyIntervall
# This can be feed into a data frame

geo_dict = ku.plural_dict(mud_log.geologyInterval)
pd.DataFrame(geo_dict)

#%%
# Or just use lithology for intervall 1, excluding attributes
lit_dict = ku.plural_dict(mud_log.geologyInterval[1].lithology, include_attr=False)
pd.DataFrame(lit_dict)

#%% Lookup a witsml unit annotation

uom = get_unit('ft')
print(uom.Name)
print([quantity for quantity in uom.QuantityType])
print(uom.toxml())

# %% Use the witml unit dict binding to convert unit
feet_factor = conversion_factor(mud_log.startMd.uom, 'ft')
print(mud_log.startMd.value()*feet_factor)

#%% Work with log files

with open(os.path.join(sample_path, 'log.xml'), 'r') as log_file:
    # logs is a regular python object according to the witsml schema
    logs = witsml.CreateFromDocument(log_file.read())

#%%

print(logs._element().documentation())
# Need to walk the singular of the object, that is the list in the object
print([l.name for l in logs.log])

# Get the schema location for logCurveInfo
print(logs.log[0].logCurveInfo[0]._element().xsdLocation().locationBase)

#%%

# It is helpful to pretty save the object we look at
ku.pretty_save(logs, 'log.xml')

#%%

log = logs.log[0]

# logData is also a list, but according to the schema the length should be 1
print(log.logData[0].mnemonicList)

# Print the documentation from the schema for logData
print(log.logData[0]._element().documentation())

# %% Build a dict of data points from logData using ku

data_dict = ku.logdata_dict(log)
pd.DataFrame(data_dict)

# %% Get the corresponding logCurveInfo as dict

curve_dict = ku.plural_dict(log.logCurveInfo)
pd.DataFrame(curve_dict)

# %% Print some data points you can also push data_dict into a dataframe

# The default delimiter is ,
delimiter = ',' if log.dataDelimiter is None else log.dataDelimiter
unit_dict = {mnem:uom for mnem, uom in zip(log.logData[0].mnemonicList.split(delimiter), log.logData[0].mnemonicList.split(delimiter))}
print(f'Unit TIME {unit_dict["TIME"]}')
print([str(t) for t in data_dict['TIME'][0:5]])
print(f'Unit GS_CFM2CUMDVOL {unit_dict["GS_CFM2CUMDVOL"]}')
print([v for v in data_dict['GS_CFM2CUMDVOL'][0:5]])
print(f'Type of GS_CFM2CUMDVOL data {type(data_dict["GS_CFM2CUMDVOL"][0])}')

# %% Soap client using wsdl

# This will fail if you don't have credentials to a witsml server
store_client = StoreClient(service_url='https://MY-WITSML-SERVER/store/witsml',
                           username='myusername',
                           password='mypassword')
# %%

id_logs = store_client.get_logs(witsml.obj_log())

len(id_logs.log)

# %%

full_log = store_client.get_logs(id_logs.log[0], returnElements='all')

ku.pretty_save(full_log, 'log.xml')

# %%

# You can make a query on for example nameWell, uidWell, nameWellbore etc
traj_ids_mywell = store_client.get_trajectorys(witsml.obj_trajectory(nameWell='mynameWell'))

print([traj.name for traj in traj_ids_mywell.trajectory])