import math
import unittest

from pygame import Vector2

from plattest.physics.rigid_body.intersection_detection import IntersectionDetection
from plattest.physics.shapes.rect import Rect


class RectAndRect(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.rect1 = Rect(Vector2(10, 10), Vector2(5, 10), math.degrees(0.6))
        self.rect2 = Rect(Vector2(4, 5), Vector2(15, 15), math.degrees(1.15))

    def test_not_colliding(self):
        self.rect2.centroid = Vector2(8, 19)
        self.assertFalse(IntersectionDetection.rect_and_rect(self.rect1, self.rect2))

    def test_inside(self):
        self.rect2.centroid = Vector2(4, 10)
        self.assertTrue(IntersectionDetection.rect_and_rect(self.rect1, self.rect2))

    def test_clipping(self):
        self.rect2.centroid = Vector2(12, 12)
        self.assertTrue(IntersectionDetection.rect_and_rect(self.rect1, self.rect2))
