from plattest.physics.forces.force_register import ForceRegister


class ForceRegistry:
    def __init__(self) -> None:
        self._force_registers: list[ForceRegister] = []

    def __getitem__(self, index: int) -> ForceRegister:
        return self._force_registers[index]

    def __len__(self) -> int:
        return len(self._force_registers)

    def append(self, fr: ForceRegister) -> None:
        self._force_registers.append(fr)

    def remove(self, fr: ForceRegister) -> None:
        self._force_registers.remove(fr)

    def clear(self) -> None:
        self._force_registers = []

    def update_forces(self, dt: float) -> None:
        for fr in self._force_registers:
            fr.force.apply_force(fr.body, dt)
