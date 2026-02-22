import pygame
from pygame import Vector2
from plattest.entities.entity import Entity

from plattest.physics.primitives import Box2D
from plattest.physics.rigidbody import RigidBody2D
from plattest.rendering.camera import Camera


class Box2DEntity(Entity):
    def __init__(
        self,
        size: Vector2,
        rigid_body: RigidBody2D,
        color: tuple[int, int, int],
    ) -> None:
        self._color: tuple[int, int, int] = color
        self._box_2d = Box2D(size, rigid_body)
        self._rotation = rigid_body.rotation

    @property
    def color(self) -> tuple[int, int, int]:
        return self._color

    @color.setter
    def color(self, color: tuple[int, int, int]) -> None:
        self._color = color

    def draw(self, camera: Camera) -> None:
        camera_position: Vector2 = camera.calc_screen_coords(
            self._box_2d.rigid_body.position
        )
        camera_box: Box2D = Box2D(
            self._box_2d.size,
            RigidBody2D(camera_position, self._box_2d.rigid_body.rotation),
        )

        points: list[Vector2] = camera_box.vertices
        pygame.draw.polygon(camera.screen, self.color, points, width=2)
