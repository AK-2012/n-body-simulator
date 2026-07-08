import pytest
from simulator.body import Body


def test_valid_body():
    body = Body(
        mass=7,
        velocity=[1.0, 2.0],
        position=[5.0, 6.0],
        color=(255, 255, 255),
    )
    assert body.mass == 7
    assert body.velocity == [1.0, 2.0]
    assert body.position == [5.0, 6.0]
    assert body.acceleration == [0.0, 0.0]
    assert body.radius == 2
    assert body.color == (255, 255, 255)


def test_invalid_mass_type():
    with pytest.raises(TypeError):
        Body(
            mass="10",
            velocity=[0, 0],
            position=[0, 0],
            color=(255, 255, 255),
        )
    with pytest.raises(TypeError):
        Body(
            mass=True,
            velocity=[0, 0],
            position=[0, 0],
            color=(255, 255, 255),
        )


def test_negative_mass():
    with pytest.raises(ValueError):
        Body(
            mass=-1,
            velocity=[0, 0],
            position=[0, 0],
            color=(255, 255, 255),
        )


def test_velocity_wrong_length():
    with pytest.raises(ValueError):
        Body(
            mass=10,
            velocity=[1],
            position=[0, 0],
            color=(255, 255, 255),
        )
    with pytest.raises(ValueError):
        Body(
            mass=10,
            velocity=[1, 2, 3],
            position=[0, 0],
            color=(255, 255, 255),
        )


def test_position_has_non_number():
    with pytest.raises(TypeError):
        Body(
            mass=10,
            velocity=[0, 0],
            position=[0, "hello"],
            color=(255, 255, 255),
        )
    with pytest.raises(TypeError):
        Body(
            mass=10,
            velocity=[0, 0],
            position=[True, 0],
            color=(255, 255, 255),
        )


def test_invalid_color():
    with pytest.raises(ValueError):
        Body(
            mass=10,
            velocity=[0, 0],
            position=[0, 0],
            color=(256, 0, 0),
        )
    with pytest.raises(ValueError):
        Body(
            mass=10,
            velocity=[0, 0],
            position=[0, 0],
            color=(-1, 0, 0),
        )


def test_color_not_tuple():
    with pytest.raises(TypeError):
        Body(
            mass=10,
            velocity=[0, 0],
            position=[0, 0],
            color=[255, 255, 255],
        )


def test_color_wrong_length():
    with pytest.raises(ValueError):
        Body(
            mass=10,
            velocity=[0, 0],
            position=[0, 0],
            color=(255, 255),
        )

