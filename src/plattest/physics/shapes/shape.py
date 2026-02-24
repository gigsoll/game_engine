from abc import ABC

from pygame import Vector2
import pygame

from plattest.physics import math_help
from plattest.physics.rigid_body.line import Line
from plattest.rendering.camera import Camera


class Shape(ABC):
    def __init__(
        self,
        vertecies: list[Vector2],
        color: tuple[int, int, int],
        centroid: Vector2,
        rotation: float = 0.0,
    ) -> None:
        self._vertecies: list[Vector2] = vertecies
        self.rotate(rotation)
        self._color: tuple[int, int, int] = color
        self._centroid: Vector2 = centroid

    def __str__(self) -> str:
        return f"<{type(self).__name__}(vertecies={self._vertecies}, centroid={self._centroid})>"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def vertecies(self) -> list[Vector2]:
        return self._vertecies

    @vertecies.setter
    def vertecies(self, vertecies: list[Vector2]):
        self._vertecies = vertecies

    @property
    def color(self) -> tuple[int, int, int]:
        return self._color

    @property
    def centroid(self) -> Vector2:
        return self._centroid

    @centroid.setter
    def centroid(self, new_pos: Vector2) -> None:
        diff = new_pos - self._centroid
        self.vertecies = [vert + diff for vert in self._vertecies]
        self._centroid = new_pos

    @color.setter
    def color(self, color: tuple[int, int, int]) -> None:
        self._color = color

    @property
    def edges(self) -> list[Line]:
        verts: list[Vector2] = self._vertecies
        return [Line(verts[i], verts[(i + 1) % len(verts)]) for i in range(len(verts))]

    @property
    def normals(self) -> list[Vector2]:
        edges: list[Line] = self.edges
        return [math_help.calc_normal(line) for line in edges]

    def draw(self, camera: Camera) -> None:
        camera_verts = camera.transform_array(self._vertecies)
        pygame.draw.circle(
            camera.screen, (100, 100, 100), camera.calc_screen_coords(self._centroid), 2
        )
        pygame.draw.polygon(camera.screen, self._color, camera_verts, 2)

    def rotate(self, angle: float) -> None:
        self._vertecies = [
            math_help.rotate_point(vert, angle, self._centroid)
            for vert in self._vertecies
        ]
