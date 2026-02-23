from plattest.physics.forces.force import Force
from pygame import Vector2

from plattest.physics.primitives.rigidbody import RigidBody


class Gravity(Force):
    def apply_force(self, body: RigidBody, dt: float) -> None:
        force: Vector2 = Vector2(0, -9.8)
        acceleration: Vector2 = force * body.mass
        body.velocity += acceleration * dt
