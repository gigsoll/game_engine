from plattest.physics.forces.force import Force
from plattest.physics.primitives.particle import Particle


class ForceRegister:
    def __init__(self, particle: Particle, force: Force) -> None:
        self.particle: Particle = particle
        self.force: Force = force
