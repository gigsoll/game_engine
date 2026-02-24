from pygame import Vector2


class CollisionManifold:
    def __init__(self, depth: float, normal: Vector2, pen_point: Vector2) -> None:
        self._depth: float = depth
        self._normal: Vector2 = normal
        self._pen_point: Vector2 = pen_point

    def resolve_colision(self): ...

    def pos_correction(self): ...

    def draw(): ...
