#%% Import the write bindings
# Note that from komle.read_bindings can not be used 
# in the same session as they use the same namespace

from komle.write_bindings import witsml

# %% Create logs, a container for obj_log
 
logs = witsml.logs(version=witsml.__version__)

# %% Create a log

log = witsml.obj_log(uidWell='1', 
                     uidWellbore='2', 
                     uid='3',
                     nameWell='SomeWell',
                     nameWellbore='SomeWellbore',
                     name='SomeName')



# %% Append the log 
logs.append(log)

# %% Write the logs object

with open('out-log.xml', 'w') as log_file:
    log_file.write(logs.toDOM().toprettyxml())

# %% Add an log that is not complete

logs.append(witsml.obj_log(uidWell='4', 
                           uidWellbore='5', 
                           uid='6',
                           nameWell='SomeWell2',
                           name='SomeName2'))

# %% Try to write to file
# This will give an error due to the missing nameWellbore

with open('out-log.xml', 'w') as log_file:
    log_file.write(logs.toDOM().toprettyxml())

# %% Set the missing value and try again

logs.log[1].nameWellbore = "SomeWellbore2"
with open('out-log.xml', 'w') as log_file:
    log_file.write(logs.toDOM().toprettyxml())

# %%
