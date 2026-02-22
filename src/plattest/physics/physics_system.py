from pygame import Vector2
from plattest.physics.forces import ForceRegistry, Gravity2D


class PhysicsSystem:
    def __init__(self, gravity: Vector2, fixed_update_dt: float) -> None:
        self._force_registry: ForceRegistry = ForceRegistry()
        self._gravity: Vector2 = gravity
        self._fixed_update: float = fixed_update_dt

        self._rigid_bodies: list[RigidBody2D] = []
        self._bodies1: list[RigidBody2D] = []
        self._bodies2: list[RigidBody2D] = []
        self._collisions: list[CollisionManifold] = []

        self._n_iterations: int = 6

    def _apply_impulse(
        self, r1: RigidBody2D, r2: RigidBody2D, m: CollisionManifold
    ) -> None:
        inv_mass1: float = r1._invert_mass
        inv_mass2: float = r2._invert_mass
        inv_mass_sum: float = inv_mass1 + inv_mass2

        if inv_mass_sum == 0:
            return

        relative_vel: Vector2 = r2.velocity - r1.velocity
        relative_normal: Vector2 = m.normal.normalize()

        # do nothing if moving away
        if relative_vel.dot(relative_normal) >= 0:
            return

        e: float = min(r1.cor, r2.cor)
        numerator = -(1.0 + e) * relative_vel.dot(relative_normal)
        j: float = numerator / inv_mass_sum

        if len(m.contact_points) > 0 and j != 0.0:
            j /= len(m.contact_points)

        impulse: Vector2 = relative_normal * j

        r1.velocity += impulse * inv_mass1 * -1
        r2.velocity += impulse * inv_mass2 * +1

    def fixed_update(self) -> None:
        self._bodies1 = []
        self._bodies2 = []
        self._collisions = []

        # find colisions
        size: int = len(self._rigid_bodies)
        for i in range(0, size, 1):
            for j in range(i, size, 1):
                if i == j:
                    continue
                result: CollisionManifold = CollisionManifold()
                r1: RigidBody2D = self._rigid_bodies[i]
                r2: RigidBody2D = self._rigid_bodies[j]
                c1: Collider2D = r1.collider
                c2: Collider2D = r2.collider

                if (
                    c1 is not None
                    and c2 is not None
                    and not (r1.has_infinite_mass and r2.has_infinite_mass)
                ):
                    result = Collisions.find_collision_features(c1, c2)
                if result is not None and result.is_colliding:
                    self._bodies1.append(r1)
                    self._bodies2.append(r2)
                    self._collisions.append(result)

        # update forces
        self._force_registry.update_forces(self._fixed_update)

        # resolve colissions via iterative impulse resolution
        for _ in range(self._n_iterations):
            for i in range(0, len(self._collisions)):
                j_size = len(self._collisions[i].contact_points)
                for j in range(j_size):
                    r1: RigidBody2D = self._bodies1[i]
                    r2: RigidBody2D = self._bodies2[i]
                    self._apply_impulse(r1, r2, self._collisions[i])

        # update physics
        for rb in self._rigid_bodies:
            rb.physics_update(self._fixed_update)

    def add_rigid_body(self, body: RigidBody2D, add_gravity: bool = True) -> None:
        self._rigid_bodies.append(body)
        if add_gravity:
            self._force_registry.add(body, Gravity2D(self._gravity))
