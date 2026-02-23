from abc import ABC, abstractmethod

from plattest.physics.primitives.rigidbody import RigidBody


class Force(ABC):
    @abstractmethod
    def apply_force(self, body: RigidBody, dt) -> None: ...
