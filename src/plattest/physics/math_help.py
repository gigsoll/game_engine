from pygame import Vector2
from math import cos, sin
import math

from plattest.physics.rigid_body.line import Line


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


def calc_normal(line: Line) -> Vector2:
    """
    returns normalized vector of normal pointing away from a line
    """
    return Vector2(line.end.y - line.start.y, line.start.x - line.end.x).normalize()
