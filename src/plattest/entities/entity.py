from plattest.rendering.camera import Camera
from abc import abstractmethod, ABC


class Entity(ABC):
    @abstractmethod
    def draw(self, camera: Camera) -> None: ...

    # @abstractmethod
    # def move_up(self) -> None: ...
    #
    # @abstractmethod
    # def move_down(self) -> None: ...
    #
    # @abstractmethod
    # def move_left(self) -> None: ...
    #
    # @abstractmethod
    # def move_right(self) -> None: ...
