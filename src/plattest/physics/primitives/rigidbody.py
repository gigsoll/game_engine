from pygame import Vector2
from plattest.physics.shapes.shape import Shape


class RigidBody:
    def __init__(self, vel: Vector2, mass: float, shape: Shape) -> None:
        self._mass: float = mass
        self._velocity = vel
        self._linear_velocity = Vector2(0, 0)
        self._angular_velocity = Vector2(0, 0)
        self.angle: float = 0.0
        self._shape: Shape = shape

    @property
    def shape(self) -> Shape:
        return self._shape

    @property
    def position(self) -> Vector2:
        return self._shape.centroid

    @position.setter
    def position(self, new_pos: Vector2) -> None:
        # self.shape.centroid = new_pos.copy()
        ...

    @property
    def velocity(self) -> Vector2:
        return self._velocity

    @velocity.setter
    def velocity(self, new_vel: Vector2) -> None:
        self._velocity = new_vel

    @property
    def mass(self) -> float:
        return self._mass
