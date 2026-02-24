from pygame import Vector2


class Line:
    def __init__(self, start: Vector2, end: Vector2) -> None:
        self._start: Vector2 = start
        self._end: Vector2 = end

    def __repr__(self) -> str:
        return f"<Line({self._start}{self._end})>"

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def start(self) -> Vector2:
        return self._start

    @property
    def end(self) -> Vector2:
        return self._end
