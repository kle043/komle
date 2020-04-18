#%%
import os
from komle.read_bindings import witsml
from komle.soap_client import StoreClient, pretty_save

sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'tests', 'samples')

#%% Open a mud log and unmarshall it 
with open(os.path.join(sample_path, 'mudLog.xml'), 'r') as mud_file:
    mud_logs = witsml.CreateFromDocument(mud_file.read())

# %%
pretty_save(mud_logs, 'mudlog.xml')

# %%

print(mud_logs.mudLog[0].name)

# %% Take the mudLog, mud_logs is a container for several mudLog
mud_log = mud_logs.mudLog[0]
print(f'nameWellbore = {mud_log.nameWellbore}')
print(f'Start {mud_log.startMd.value()} {mud_log.startMd.uom}')
for geo_int in mud_log.geologyInterval:
    # need to call value on leaf nodes with attributes
    print(f'{geo_int.mdBottom.value()} - {geo_int.mdTop.value()}  {geo_int.mdTop.uom}')
    for lit in geo_int.lithology:
        print(f'Lit: {lit.lithPc.value()} {lit.lithPc.uom}')

# %% Work with log files

with open(os.path.join(sample_path, 'log.xml'), 'r') as log_file:
    # logs is a regular python object according to the witsml schema
    logs = witsml.CreateFromDocument(log_file.read())

# Need to walk the singular of the object, that is the list in the object
print(logs._element().documentation())

#%%

print([l.name for l in logs.log])

#%%
# It is helpful to pretty save the object we look at
pretty_save(logs, 'log.xml')

#%%

log = logs.log[0]
# logData is also a list, but according to the schema the length should be 1
print(log.logData[0].mnemonicList)
# Print the documentation from the schema for logData
print(log.logData[0]._element().documentation())

# %% Build a dict of data points from logData

# There can be other primitive types then the ones in this log
prim_types = {'date time':witsml.timestamp, 'double':float, 'string':str} 
# Get the types from curveInfo, we are looking at date time as the indexCurve
mnem_cast_map = {c.mnemonic.value():prim_types[c.typeLogData] for c in log.logCurveInfo}

#%%

#The default delimiter is , 
delimiter = ',' if log.dataDelimiter is None else log.dataDelimiter

data_list = [(mnem, mnem_cast_map[mnem], []) for mnem in log.logData[0].mnemonicList.split(delimiter)]
unit_dict = {mnem:uom for mnem, uom in zip(log.logData[0].mnemonicList.split(delimiter),
                                           log.logData[0].unitList.split(delimiter))}
for data_str in log.logData[0].data:
    for i, point_str in enumerate(data_str.split(delimiter)):
        if point_str:
            value_cast = data_list[i][1]
            data_list[i][2].append(value_cast(point_str))
        else:
            data_list[i][2].append(None)

data_dict = {mnem:values for mnem, _, values in data_list}

# %%
print(f'Unit TIME {unit_dict["TIME"]}')
print([str(t) for t in data_dict['TIME'][0:5]])
print(f'Unit GS_CFM2CUMDVOL {unit_dict["GS_CFM2CUMDVOL"]}')
print([v for v in data_dict['GS_CFM2CUMDVOL'][0:5]])

# %% Soap client using wsdl
# This will fail if you don't have credentials to a witsml server
store_client = StoreClient(service_url='https://my-witsml-server',
                           username='myusername',
                           password='mypassword')
# %%

id_logs = store_client.get_logs(witsml.obj_log())

len(id_logs.log)

# %%

full_log = store_client.get_logs(id_logs.log[0], returnElements='all')

pretty_save(full_log, 'log.xml')

# %%
# You can make a query on for example nameWell, uidWell, nameWellbore etc
traj_ids_mywell = store_client.get_trajectory(witsml.obj_trajectory(nameWell='mynameWell'))

print([traj.name for traj in traj_ids_mywell.trajectory])