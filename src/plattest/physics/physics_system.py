from plattest.physics.forces.force import Force
from plattest.physics.forces.force_registry import ForceRegistry
from plattest.physics.forces.force_register import ForceRegister
from .primitives import Particle


class PhysicsSystem:
    def __init__(self) -> None:
        self._elements: list[Particle] = []
        self._force_registry = ForceRegistry()

    def add_force(self, particle: Particle, force: Force) -> None:
        if particle not in self._elements:
            self._elements.append(particle)
        list_part = self._elements[self._elements.index(particle)]
        fr: ForceRegister = ForceRegister(list_part, force)
        if fr in self._force_registry:
            return
        self._force_registry.append(fr)

    def update(self, dt: float) -> None:
        self._force_registry.update_forces(dt)
        for el in self._elements:
            el.position += el.velocity * dt
