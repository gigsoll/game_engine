from pygame import Vector2
from math import cos, sin
import math


def rotate_point(point: Vector2, angle_degree: float, origin: Vector2):
    radians: float = math.radians(angle_degree)
    s = sin(radians)
    c = cos(radians)

    point.x -= origin.x
    point.y -= origin.y

    x_rot = point.x * c - point.y * s
    y_rot = point.x * s + point.y * c

    point.x = x_rot + origin.x
    point.y = y_rot + origin.y

    return point
