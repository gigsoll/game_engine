import unittest

from pygame import Vector2

from plattest.physics.rigid_body.intersection_detection import IntersectionDetection
from plattest.physics.shapes.circle import Circle
from plattest.physics.shapes.rect import Rect


class RectAndCircle(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.rectangle = Rect.from_corners(Vector2(4, 4), Vector2(10, 10))
        self.cirlce: Circle = Circle(Vector2(0, 0), 3, (0, 0, 0))

    def test_sides_true(self):
        sides: dict = {
            "left": Vector2(1.79, 7.18),
            "top": Vector2(6.93, 12.58),
            "right": Vector2(12.22, 7.18),
            "bottom": Vector2(7.13, 2.17),
        }
        for key, value in sides.items():
            self.cirlce.centroid = value
            self.assertTrue(
                IntersectionDetection.rect_and_circle(self.rectangle, self.cirlce),
                f"side {key} failed",
            )

    def test_false(self):
        self.cirlce.centroid = Vector2(100, 100)
        self.assertFalse(
            IntersectionDetection.rect_and_circle(self.rectangle, self.cirlce)
        )
