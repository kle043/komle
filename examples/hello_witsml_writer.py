#%% Import the write bindings
# Note that from komle.read_bindings can not be used 
# in the same session as they use the same namespace

from datetime import datetime
from komle.write_bindings import witsml
from komle import utils as ku

# %% Create logs, a container for obj_log
 
logs = witsml.logs(version=witsml.__version__)

# %% Create a log
# you can initalize an object giving the attributes in the constructor

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

with open('out_log.xml', 'w') as log_file:
    log_file.write(logs.toDOM().toprettyxml())

# %% Set the missing value and try again
# It is also possible to add values after initalization

logs.log[1].nameWellbore = "SomeWellbore2"
with open('out-log.xml', 'w') as log_file:
    log_file.write(logs.toDOM().toprettyxml())

# %% Create a Trajectorys

trajs = witsml.trajectorys(version=witsml.__version__)


# %% Create trajectory
traj = witsml.obj_trajectory(uidWell='4', 
                             uidWellbore='5', 
                             uid='6',
                             nameWell='SomeWell2',
                             nameWellbore='SomeWellbore',
                             name='SomeName2')

# %% Fill some more values

traj.objectGrowing = False
traj.mdMn = 0
traj.mdMn.uom = 'm'

# %% uom does not accept invalid units

traj.mdMx = 1000
traj.mdMx.uom = 'tt'

# %%

traj.mdMx.uom = 'm'
traj.serviceCompany = 'Tigergutt'

# %% Create a trajectoryStation

traj_station = witsml.cs_trajectoryStation(uid='myuid')


# %%

traj_station.typeTrajStation = 'unknown'
traj_station.md, traj_station.md.uom = 40, 'm'
#%%

traj_station.tvd, traj_station.tvd.uom = 40.1, 'm'
traj_station.incl, traj_station.incl.uom = 0.2, 'dega'
traj_station.azi, traj_station.azi.uom = 0.1, 'dega'
traj_station.dispNs, traj_station.dispNs.uom = 28.0, 'm'
traj_station.dispEw, traj_station.dispEw.uom = 2.2, 'm'
traj_station.vertSect, traj_station.vertSect.uom = 0, 'm'
traj_station.dls, traj_station.dls.uom = 0, 'dega/m'

# %% Add the trajectoryStation and trajectory

traj.trajectoryStation.append(traj_station)
trajs.append(traj)


# %% Write to file
with open('out_trajectory.xml', 'w') as traj_file:
    traj_file.write(trajs.toDOM().toprettyxml())

# %%
