import pyxb
from komle.write_bindings import witsml

def test_logs():

    logs = witsml.logs(version=witsml.__version__)
    log = witsml.obj_log(uidWell='1', 
                         uidWellbore='2', 
                         uid='3',
                         nameWell='SomeWell',
                         nameWellbore='SomeWellbore',
                         name='SomeName')
    
    logs.append(log)
    
    logs.toDOM()

def test_trajecorys():
    trajs = witsml.trajectorys(version=witsml.__version__)

    traj = witsml.obj_trajectory(uidWell='4', 
                                 uidWellbore='5', 
                                 uid='6',
                                 nameWell='SomeWell2',
                                 nameWellbore='SomeWellbore',
                                 name='SomeName2')
    traj.objectGrowing = False
    traj.mdMn = 0
    traj.mdMn.uom = 'm'
    traj.mdMx = 1000
    traj.mdMx.uom = 'm'
    traj.serviceCompany = 'Tigergutt'
    traj_station = witsml.cs_trajectoryStation(uid='myuid')
    traj_station.typeTrajStation = 'unknown'
    traj_station.md, traj_station.md.uom = 40, 'm'
    
    traj_station.tvd, traj_station.tvd.uom = 40.1, 'm'
    traj_station.incl, traj_station.incl.uom = 0.2, 'dega'
    traj_station.azi, traj_station.azi.uom = 0.1, 'dega'
    traj_station.dispNs, traj_station.dispNs.uom = 28.0, 'm'
    traj_station.dispEw, traj_station.dispEw.uom = 2.2, 'm'
    traj_station.vertSect, traj_station.vertSect.uom = 0, 'm'
    traj_station.dls, traj_station.dls.uom = 0, 'dega/m'
    
    traj.trajectoryStation.append(traj_station)
    trajs.append(traj)
    trajs.toDOM()
