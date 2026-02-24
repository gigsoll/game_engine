from pygame import Vector2


class CollisionData:
    def __init__(self, collided=False, depth=0.0, normal=Vector2()) -> None:
        self.collided: bool = collided
        self.depth: float = depth
        self.normal: Vector2 = normal
