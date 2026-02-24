import math
from pygame import Vector2
from plattest.physics.forces.force import Force
from plattest.physics.forces.force_registry import ForceRegistry
from plattest.physics.forces.force_register import ForceRegister
from plattest.physics.forces.gravity import Gravity
from plattest.physics.rigid_body.intersection_detection import IntersectionDetection
from plattest.physics.rigid_body.rigidbody import RigidBody
from plattest.physics.shapes import shape


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
            new_pos: Vector2 = el.position + el.velocity * dt
            el.position = new_pos

        # detect collisions
        for el_1 in self._elements:
            for el_2 in self._elements:
                if el_1 == el_2:
                    break

                col_res = IntersectionDetection.detect_intersection(
                    el_1.shape, el_2.shape
                )
                # resolve collisions
                # TODO: CLEAN UP THIS
                if col_res.collided:
                    print("intersected")
                    if el_1.mass != 0 and el_2.mass != 0:
                        el_1.position = (
                            el_1.position + col_res.normal * col_res.depth / 2
                        )
                        el_2.position = (
                            el_2.position - col_res.normal * col_res.depth / 2
                        )
                    elif el_1.mass != 0 and el_2.mass == 0:
                        el_1.position = el_1.position - col_res.normal * col_res.depth
                    elif el_1.mass == 0 and el_2.mass != 0:
                        el_2.position = el_2.position - col_res.normal * col_res.depth
                    else:
                        ...

                    el_1.velocity = -el_1.velocity
                    el_2.velocity = -el_2.velocity
