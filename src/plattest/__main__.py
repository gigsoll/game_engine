import sys
import pygame
from random import randint
from time import time
from plattest.config import SCREEN_HEIGHT, SCREEN_WIDTH
from plattest.physics.forces.gravity import Gravity
from plattest.physics.physics_system import PhysicsSystem
from plattest.physics.primitives.rigidbody import RigidBody
from plattest.physics.shapes.circle import Circle
from plattest.physics.shapes.rect import Rect
from plattest.rendering.camera import Camera


def main():
    pygame.init()
    physics = PhysicsSystem()
    bodies = []
    for _ in range(1200):
        position = pygame.Vector2(
            0 + randint(0, SCREEN_WIDTH), 300 + randint(0, SCREEN_HEIGHT) / 2
        )
        body = RigidBody(
            position.copy(),
            pygame.Vector2(0, 100),
            10,
            Circle(position.copy(), 10, (0, 255, 0)),
        )

        bodies.append(body)
        physics.add_force(body, Gravity())
    camera = Camera(0, 0)
    screen = camera.create_screen()
    cur_time = time()
    prev_time = time()
    while True:
        cur_time = time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        dt: float = cur_time - prev_time
        prev_time = cur_time
        screen.fill((0, 0, 0))
        physics.update(dt)
        for body in bodies:
            body.shape.draw(camera)
        pygame.display.flip()
        print(dt)


main()
