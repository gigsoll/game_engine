import sys
import pygame
from random import randint
from time import time
from pygame import Vector2
from plattest.config import SCREEN_HEIGHT, SCREEN_WIDTH
from plattest.physics.physics_system import PhysicsSystem
from plattest.physics.primitives.rigidbody import RigidBody
from plattest.physics.shapes.circle import Circle
from plattest.physics.shapes.rect import Rect
from plattest.rendering.camera import Camera


def main():
    pygame.init()
    physics = PhysicsSystem()
    for _ in range(120):
        body = RigidBody(
            pygame.Vector2(0, 100),
            10,
            Circle(
                pygame.Vector2(
                    0 + randint(0, SCREEN_WIDTH), 300 + randint(0, SCREEN_HEIGHT) / 2
                ),
                30,
                (0, 255, 0),
            ),
        )
        physics.add_body(body)

    physics.add_body(
        RigidBody(
            vel=Vector2(0, 0),
            mass=10,
            shape=Rect(size=Vector2(30, 30), pos=Vector2(100, 700), rotation=10),
        )
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
        for body in physics.bodies:
            body.shape.draw(camera)
        pygame.display.flip()
        print("---------------------")


main()
