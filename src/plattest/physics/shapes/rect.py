from pygame import Vector2
from plattest.physics.shapes.shape import Shape


class Rect(Shape):
    def __init__(self, size: Vector2, position: Vector2, rotation: float) -> None:
        min_point = position - size / 2
        max_point = position + size / 2
        self._vertecies = [
            Vector2(min_point.x, max_point.y),
            Vector2(max_point.x, max_point.y),
            Vector2(max_point.x, min_point.y),
            Vector2(min_point.x, min_point.y),
        ]
        self._centroid: Vector2 = position
        self._color = (0, 255, 0)
        self.rotate(rotation)

    @classmethod
    def from_corners(cls, min: Vector2, max: Vector2) -> Rect:
        size: Vector2 = max - min
        position: Vector2 = min + size / 2
        return cls(size, position, 0)
