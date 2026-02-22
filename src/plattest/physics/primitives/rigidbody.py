from pygame import Vector2
from plattest.physics.primitives.particle import Particle
from plattest.physics.shapes.shape import Shape


class RigidBody(Particle):
    def __init__(self, pos: Vector2, vel: Vector2, mass: float, shape: Shape) -> None:
        super().__init__(pos, vel, mass)
        self._linear_velocity = Vector2(0, 0)
        self._angular_velocity = Vector2(0, 0)
        self.angle: float = 0.0
        self._shape: Shape = shape

    @property
    def shape(self) -> Shape:
        return self._shape

    @property
    def position(self) -> Vector2:
        return self._position

    @position.setter
    def position(self, new_pos: Vector2) -> None:
        self._position = new_pos
        self.shape.centroid = self._position
