from pygame import Vector2


class Particle:
    def __init__(self, pos: Vector2, vel: Vector2, mass: float) -> None:
        self._position: Vector2 = pos
        self._velocity: Vector2 = vel
        self._mass: float = mass

    @property
    def position(self) -> Vector2:
        return self._position

    @position.setter
    def position(self, new_pos: Vector2) -> None:
        self._position = new_pos

    @property
    def velocity(self) -> Vector2:
        return self._velocity

    @velocity.setter
    def velocity(self, new_vel: Vector2) -> None:
        self._velocity = new_vel

    @property
    def mass(self) -> float:
        return self._mass
