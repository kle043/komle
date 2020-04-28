#%%
from komle.write_bindings import witsml

# %%

log = witsml.obj_log(uidWell='1', 
                     uidWellbore='2', 
                     uid='3',
                     nameWell='SomeWell',
                     nameWellbore='SomeWellbore',
                     name='SomeName')

# %%
logs = witsml.logs(version=witsml.__version__)

# %%
logs.append(log)

# %%

with open('out-log.xml', 'w') as log_file:
    log_file.write(logs.toDOM().toprettyxml())

# %%
