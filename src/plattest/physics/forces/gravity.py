from plattest.physics.forces.force import Force
from plattest.physics.primitives.particle import Particle
from pygame import Vector2


class Gravity(Force):
    def apply_force(self, particle: Particle, dt: float) -> None:
        force: Vector2 = Vector2(0, -9.8)
        acceleration: Vector2 = force * particle.mass
        particle.velocity += acceleration * dt
