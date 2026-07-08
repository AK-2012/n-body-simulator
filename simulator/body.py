class Body:
    def __init__(
        self,
        mass: int | float,
        velocity: list[int | float],
        position: list[int | float],
        color: tuple[int, int, int],
    ):
        self.mass = self._validate_mass("mass", mass)
        self.velocity = self._validate_vector("velocity", velocity, 2)
        self.position = self._validate_vector("position", position, 2)
        self.acceleration = [0.0, 0.0]
        self.radius = max(2, int(mass ** (1 / 3)))
        self.color = self._validate_color(color)

    @staticmethod
    def _validate_mass(name, value):
        if not isinstance(value, float | int) or isinstance(
            value, bool
        ):  # must be float or int
            raise TypeError(f"{name} must be a integer or float")
        if value <= 0:  # must be greater than 0
            raise ValueError(f"{name} must be greater than 0")
        return value

    @staticmethod
    def _validate_vector(name, values, expected_length):
        if not isinstance(values, list):  # must be a list
            raise TypeError(f"{name} must be a list")
        if len(values) != expected_length:  # must have the expected length
            raise ValueError(f"{name} must have exactly {expected_length} elements")
        for element in values:  # must be numbers
            if not isinstance(element, int | float) or isinstance(element, bool):
                raise TypeError(f"all elements must be integers or floats")
        return values

    @staticmethod
    def _validate_color(color: tuple[int, int, int]):
        if not isinstance(color, tuple):  # must be a tuple
            raise TypeError("color must be a tuple")
        if len(color) != 3:  # must have 3 values
            raise ValueError("color must have exactly 3 values")
        for value in color:  # must be integers between 0-255 inclusive
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError("all color values must be integers")
            if not 0 <= value <= 255:
                raise ValueError("color values must be between 0 and 255")
        return color
