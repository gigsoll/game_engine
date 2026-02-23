from pygame import Vector2
import pygame

from plattest.physics.rigid_body.line import Line
from plattest.physics.shapes.shape import Shape
from plattest.rendering.camera import Camera


class Circle(Shape):
    def __init__(
        self, centroid: Vector2, radius: float, color: tuple[int, int, int]
    ) -> None:
        self._centroid: Vector2 = centroid
        self._radius: float = radius
        self._color = color
        self._vertecies = [Vector2(self._centroid.x + self._radius, self._centroid.y)]

    @property
    def radius(self):
        return self._radius

    @property
    def edges(self) -> list[Line]:
        return [Line(self._centroid, self.vertecies[0])]

    def draw(self, camera: Camera) -> None:
        pygame.draw.line(
            camera.screen,
            (100, 100, 100),
            camera.calc_screen_coords(self._centroid),
            camera.calc_screen_coords(self.vertecies[0]),
        )
        pygame.draw.circle(
            camera.screen,
            self._color,
            camera.calc_screen_coords(self._centroid),
            self._radius,
            2,
        )
