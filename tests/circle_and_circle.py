import unittest

from pygame import Vector2

from plattest.physics.rigid_body.intersection_detection import IntersectionDetection
from plattest.physics.shapes.circle import Circle


class CircleAndCircle(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.c1: Circle = Circle(Vector2(0, 5), 10, (0, 0, 0))
        self.c2: Circle = Circle(Vector2(15, 15), 5, (0, 0, 0))

    def test_false(self):
        self.c2.centroid = Vector2(15, 15)
        self.assertFalse(IntersectionDetection.circle_and_circle(self.c1, self.c2))

    def test_inside(self):
        self.c2.centroid = Vector2(-4, 5)
        self.assertTrue(IntersectionDetection.circle_and_circle(self.c1, self.c2))

    def test_clipping(self):
        self.c2.centroid = Vector2(10, 15)
        self.assertTrue(IntersectionDetection.circle_and_circle(self.c1, self.c2))
