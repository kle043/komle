import pytest
from pyxb.namespace import Namespace, utility


@pytest.fixture(scope='session', autouse=True)
def setup():
    # If running all the tests at once, we can't have two equal namespaces
    # So reset in case read_bindings is loaded and load the write_binding
    for name in utility.AvailableNamespaces():
        getattr(super(Namespace, name), '_reset', lambda *args, **kw: None)()
        name._Namespace__initialNamespaceContext = None

    yield
    # Reset namespace after test is finished
    for name in utility.AvailableNamespaces():
        getattr(super(Namespace, name), '_reset', lambda *args, **kw: None)()
        name._Namespace__initialNamespaceContext = None


def test_logs():
    from komle.bindings.v1411.write import witsml

    logs = witsml.logs(version=witsml.__version__)
    log = witsml.obj_log(
        uidWell='1',
        uidWellbore='2',
        uid='3',
        nameWell='SomeWell',
        nameWellbore='SomeWellbore',
        name='SomeName',
    )

    logs.append(log)

    logs.toDOM()


def test_trajecorys():
    from komle.bindings.v1411.write import witsml

    trajs = witsml.trajectorys(version=witsml.__version__)

    traj = witsml.obj_trajectory(
        uidWell='4',
        uidWellbore='5',
        uid='6',
        nameWell='SomeWell2',
        nameWellbore='SomeWellbore',
        name='SomeName2',
    )
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
