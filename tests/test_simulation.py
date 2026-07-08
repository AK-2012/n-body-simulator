import pytest
from simulator.body import Body
from simulator.simulation import Simulation


def test_empty_simulation():
    sim = Simulation()
    assert sim.G == 100
    assert sim.bodies == []


def test_add_body():
    sim = Simulation()
    body = Body(
        mass=10,
        velocity=[0, 0],
        position=[0, 0],
        color=(255, 255, 255),
    )
    sim.add_body(body)
    assert sim.bodies == [body]

def test_add_bodies():
    sim = Simulation()
    body1 = Body(
        mass=10,
        velocity=[0, 0],
        position=[0, 0],
        color=(255, 0, 0)
    )
    body2 = Body(
        mass=10,
        velocity=[0, 0],
        position=[0, 0],
        color=(0, 255, 0)

    )
    sim.add_body(body1, body2)
    assert sim.bodies == [body1, body2]


def test_remove_body():
    sim = Simulation()
    body = Body(
        mass=10,
        velocity=[0, 0],
        position=[0, 0],
        color=(255, 255, 255),
    )
    sim.add_body(body)
    sim.remove_body(body)
    assert sim.bodies == []


def test_clear():
    sim = Simulation()
    body = Body(
        mass=10,
        velocity=[0, 0],
        position=[0, 0],
        color=(255, 255, 255),
    )
    sim.add_body(body)
    sim.clear()
    assert sim.bodies == []


def test_acceleration_direction():
    sim = Simulation()
    body1 = Body(
        mass=10,
        velocity=[0, 0],
        position=[0, 0],
        color=(255, 0, 0),
    )
    body2 = Body(
        mass=10,
        velocity=[0, 0],
        position=[100, 0],
        color=(0, 255, 0),
    )
    sim.add_body(body1)
    sim.add_body(body2)
    sim._update_accelerations()
    # body1 should be pulled toward body2
    assert body1.acceleration[0] > 0
    # no y movement
    assert body1.acceleration[1] == 0
    # body2 should be pulled toward body1
    assert body2.acceleration[0] < 0
    # no y movement
    assert body2.acceleration[1] == 0


def test_equal_mass_equal_acceleration():
    sim = Simulation()
    body1 = Body(
        mass=10,
        velocity=[0, 0],
        position=[0, 0],
        color=(255, 0, 0),
    )
    body2 = Body(
        mass=10,
        velocity=[0, 0],
        position=[100, 0],
        color=(0, 255, 0),
    )
    sim.add_body(body1, body2)
    sim._update_accelerations()
    assert abs(body1.acceleration[0]) == pytest.approx(abs(body2.acceleration[0]))


def test_invalid_body():
    sim = Simulation()
    with pytest.raises(TypeError):
        sim.add_body("this should raise an error")
        

def test_step_position():
    sim = Simulation(0)
    body = Body(
        mass=10,
        velocity=[5, 0],
        position=[0, 0],
        color=(255, 255, 255),
    )
    sim.add_body(body)
    sim.step(1)
    assert body.position == [5, 0]


def test_zero_division_fix():
    sim = Simulation()
    body1 = Body(
        mass=10,
        velocity=[0, 0],
        position=[0, 0],
        color=(255, 0, 0),
    )
    body2 = Body(
        mass=10,
        velocity=[0, 0],
        position=[0, 0],
        color=(0, 255, 0),
    )
    sim.add_body(body1, body2)
    sim._update_accelerations()
    assert body1.acceleration == [0.0, 0.0]
    assert body2.acceleration == [0.0, 0.0]


def test_gravitational_constant():
    sim = Simulation(42)
    assert sim.G == 42