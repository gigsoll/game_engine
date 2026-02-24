from pygame import Vector2
from plattest.physics.forces.force import Force
from plattest.physics.forces.force_registry import ForceRegistry
from plattest.physics.forces.force_register import ForceRegister
from plattest.physics.forces.gravity import Gravity
from plattest.physics.rigid_body.rigidbody import RigidBody


class PhysicsSystem:
    def __init__(self) -> None:
        self._elements: list[RigidBody] = []
        self._force_registry = ForceRegistry()
        self._gravity: Gravity = Gravity()

    @property
    def bodies(self) -> list[RigidBody]:
        return self._elements

    def add_body(self, body: RigidBody) -> None:
        self._elements.append(body)
        self._force_registry.append(ForceRegister(body, self._gravity))

    def update(self, dt: float) -> None:
        # update forces
        self._force_registry.update_forces(dt)

        # recalculate position
        for el in self._elements:
            print(f"calculated dp: {el.velocity * dt}")
            new_pos: Vector2 = el.position + el.velocity * dt
            el.position = new_pos

        # detect collisions

        # resolve collisions
