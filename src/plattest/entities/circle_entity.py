import pygame
from pygame import Surface, Vector2
from plattest.entities.entity import Entity
from plattest.physics.primitives.circle import Circle
from plattest.physics.rigidbody.rigid_body_2d import RigidBody2D
from plattest.rendering.camera import Camera


class CircleEntity(Entity):
    def __init__(
        self, radius: float, rigidbody: RigidBody2D, color: tuple[int, int, int]
    ) -> None:
        self._color: tuple[int, int, int] = color
        self._circle: Circle = Circle(radius, rigidbody)

    @property
    def color(self) -> tuple[int, int, int]:
        return self._color

    @color.setter
    def color(self, color: tuple[int, int, int]) -> None:
        self._color = color

    @property
    def circle(self) -> Circle:
        return self._circle

    def draw(self, camera: Camera):
        camera_center: Vector2 = camera.calc_screen_coords(self._circle.center)

        pygame.draw.circle(camera.screen, self.color, camera_center, self.circle.radius)
