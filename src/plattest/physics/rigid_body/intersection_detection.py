from pygame import Vector2
from plattest.physics.math_help import calc_normal
from plattest.physics.rigid_body.line import Line
from plattest.physics.shapes.circle import Circle
from plattest.physics.shapes.rect import Rect


class IntersectionDetection:
    @staticmethod
    def circle_and_circle(c1: Circle, c2: Circle) -> bool:
        center1: Vector2 = c1.centroid
        center2: Vector2 = c2.centroid

        direction = center2 - center1
        r1: float = c1.radius
        r2: float = c2.radius

        rad_sum: float = r1 + r2

        return direction.length_squared() < rad_sum**2

    @staticmethod
    def rect_and_circle(rect: Rect, circle: Circle) -> bool:
        distance_x: float = abs(circle.centroid.x - rect.centroid.x)
        distance_y: float = abs(circle.centroid.y - rect.centroid.y)
        distance: Vector2 = Vector2(distance_x, distance_y)

        if distance.x > rect.size.x / 2 + circle.radius:
            return False
        if distance.y > rect.size.y / 2 + circle.radius:
            return False
        if distance.x <= rect.size.x / 2:
            return True
        if distance.y <= rect.size.y / 2:
            return True

        corner_distance_squared = (distance.x - rect.size.x / 2) ** 2 + (
            distance.y - rect.size.y / 2
        ) ** 2
        return corner_distance_squared <= circle.radius**2

    @classmethod
    def circle_and_rect(cls, circle: Circle, rect: Rect) -> bool:
        return cls.rect_and_circle(rect, circle)
