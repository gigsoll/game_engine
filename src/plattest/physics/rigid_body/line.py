from pygame import Vector2


class Line:
    def __init__(self, start: Vector2, end: Vector2) -> None:
        self._start: Vector2 = start
        self._end: Vector2 = end

    @property
    def start(self) -> Vector2:
        return self._start

    @property
    def end(self) -> Vector2:
        return self._end
