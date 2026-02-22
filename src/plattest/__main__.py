import sys
import pygame
from random import randint
from time import time
from plattest.config import SCREEN_HEIGHT, SCREEN_WIDTH
from plattest.physics import physics_system
from plattest.physics.forces.gravity import Gravity
from plattest.physics.physics_system import PhysicsSystem
from plattest.physics.primitives.particle import Particle
from plattest.rendering.camera import Camera


def main():
    pygame.init()
    physics = PhysicsSystem()
    for _ in range(120):
        physics.add_force(
            Particle(
                pygame.Vector2(
                    0 + randint(0, SCREEN_WIDTH), 300 + randint(0, SCREEN_HEIGHT) / 2
                ),
                pygame.Vector2(randint(-100, 100), 10 + randint(0, 500)),
                10,
            ),
            Gravity(),
        )
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
        for part in physics._elements:
            camera.draw_particle(part)
        pygame.display.flip()
        print(dt)


main()
