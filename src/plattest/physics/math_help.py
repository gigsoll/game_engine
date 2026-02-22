from pygame import Vector2
from math import cos, sin
import math


def rotate_point(vertice: Vector2, angle_degree: float, point: Vector2):
    radians: float = math.radians(angle_degree)

    rotated: Vector2 = Vector2(0, 0)
    direction: Vector2 = vertice - point

    rotated.x = direction.x * cos(radians) - direction.y * sin(radians)
    rotated.y = direction.x * sin(radians) - direction.y * cos(radians)

    rotated += point
    return rotated
