from plattest.physics.forces.force import Force
from plattest.physics.primitives.rigidbody import RigidBody


class ForceRegister:
    def __init__(self, body: RigidBody, force: Force) -> None:
        self.body: RigidBody = body
        self.force: Force = force
