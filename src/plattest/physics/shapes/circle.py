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

        # circle should have at least two points to work wit SAT
        # initally they are set as points from center to edge along
        # x axis, but may be changed
        self._vertecies = [
            Vector2(self._centroid.x + self._radius, self._centroid.y),
            Vector2(self._centroid.x - self._radius, self._centroid.y),
        ]

    @property
    def radius(self):
        return self._radius

    @property
    def edges(self) -> list[Line]:
        return [
            Line(self._centroid, self.vertecies[0]),
            Line(self._centroid, self.vertecies[1]),
        ]

    def apply_normal_verts(self, normal) -> None:
        self._vertecies[0] = self._centroid + (normal * self._radius)
        self._vertecies[1] = self._centroid - (normal * self._radius)

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
