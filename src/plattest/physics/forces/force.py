from abc import ABC, abstractmethod

from plattest.physics.primitives.particle import Particle


class Force(ABC):
    @abstractmethod
    def apply_force(self, particle: Particle, dt) -> None: ...
