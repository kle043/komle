#%%
import os
from komle.read_bindings import witsml
from komle.soap_client import StoreClient, pretty_save

sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'tests', 'samples')

#%% Open a mud log and marshall it 
with open(os.path.join(sample_path, 'mudLog.xml'), 'r') as mud_file:
    mud_logs = witsml.CreateFromDocument(mud_file.read())

# %%
pretty_save(mud_logs, 'mudlog.xml')

# %%

mud_logs.mudLog[0].name

# %% Take the mudLog, mud_logs is a container for several mudLog
mud_log = mud_logs.mudLog[0]
print(f'nameWellbore = {mud_log.nameWellbore}')
print(f'Start {mud_log.startMd.value()} {mud_log.startMd.uom}')
for geo_int in mud_log.geologyInterval:
    # need to call value on leaf nodes with attributes
    print(f'{geo_int.mdBottom.value()} - {geo_int.mdTop.value()}  {geo_int.mdTop.uom}')
    for lit in geo_int.lithology:
        print(f'Lit: {lit.lithPc.value()} {lit.lithPc.uom}')

# %%

store_client = StoreClient(service_url='https://my-witsml-server',
                           username='myusername',
                           password='mypassword')
# %%

id_logs = store_client.get_logs(witsml.obj_log())

len(id_logs.log)

# %%

full_log = store_client.get_logs(id_logs.log[0], returnElements='all')

pretty_save(full_log, 'log.xml')