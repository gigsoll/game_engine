from pygame import Vector2
from plattest.physics.rigid_body.collision_manifold import CollisionManifold
from plattest.physics.shapes.circle import Circle
from plattest.physics.shapes.rect import Rect
from plattest.physics.shapes.shape import Shape


class IntersectionDetection:
    @classmethod
    def detect_intersection(cls, s1: Shape, s2: Shape) -> CollisionManifold | None:
        """
        Super method created to combine all the previous ones into united system
        """
        collided: bool = False
        if isinstance(s1, Circle) and isinstance(s2, Circle):
            collided = cls.circle_and_circle(s1, s2)
        elif isinstance(s1, Rect) and isinstance(s2, Circle):
            collided = cls.rect_and_circle(s1, s2)
        elif isinstance(s1, Circle) and isinstance(s2, Rect):
            collided = cls.circle_and_rect(s1, s2)

        if collided:
            # TODO: Add logic to generate manifold
            return CollisionManifold()
        return None

    @staticmethod
    def separatin_axis_theorem(s1: Shape, s2: Shape) -> bool:
        """
        General SAT Algorithm which should be possible to apply for
        any shape, return if collision happened
        """
        axes: list[Vector2] = s1.normals + s2.normals
        s1_verts: list[Vector2] = s1.vertecies
        s2_verts: list[Vector2] = s2.vertecies
        for axis in axes:
            # project points on normals
            s1_dots = [point.dot(axis) for point in s1_verts]
            s2_dots = [point.dot(axis) for point in s2_verts]

            # min max points
            s1_extr: tuple[float, float] = (min(s1_dots), max(s1_dots))
            s2_extr: tuple[float, float] = (min(s2_dots), max(s2_dots))

            # detect gap
            if s1_extr[0] < s1_extr[1] < s2_extr[0] < s2_extr[1]:
                return False  # is separated by axis, means not collided

        return True  # collided

    @classmethod
    def circle_and_circle(cls, c1: Circle, c2: Circle) -> bool:
        direction = (c2.centroid - c1.centroid).normalize()
        c1.apply_normal_verts(direction)
        c2.apply_normal_verts(direction)

        return cls.separatin_axis_theorem(c1, c2)

    @classmethod
    def circle_and_rect(cls, circle: Circle, rect: Rect) -> bool:
        rect_direction = (circle.centroid - rect.centroid).normalize()
        circle.apply_normal_verts(rect_direction)
        return cls.separatin_axis_theorem(circle, rect)

    @classmethod
    def rect_and_rect(cls, r1: Rect, r2: Rect) -> bool:
        return cls.separatin_axis_theorem(r1, r2)

    @classmethod
    def rect_and_circle(cls, rect: Rect, circle: Circle) -> bool:
        return cls.circle_and_rect(circle, rect)
