import sys
import pygame
from random import randint
from time import time
from pygame import Vector2, rect
from plattest.config import SCREEN_HEIGHT, SCREEN_WIDTH
from plattest.physics.physics_system import PhysicsSystem
from plattest.physics.rigid_body.rigidbody import RigidBody
from plattest.physics.shapes.circle import Circle
from plattest.physics.shapes.rect import Rect
from plattest.rendering.camera import Camera


def main():
    pygame.init()
    physics = PhysicsSystem()
    for _ in range(20):
        body = RigidBody(
            pygame.Vector2(randint(-200, 200), 0),
            10,
            Circle(
                pygame.Vector2(
                    60 + randint(0, SCREEN_WIDTH - 120),
                    300 + randint(0, SCREEN_HEIGHT) / 2,
                ),
                20,
                (0, 255, 0),
            ),
        )
        physics.add_body(body)

    borders = [
        (Vector2(0, 0), Vector2(SCREEN_WIDTH, 30)),
        (Vector2(0, 0), Vector2(30, SCREEN_HEIGHT)),
        (
            Vector2(0, SCREEN_HEIGHT),
            Vector2(SCREEN_WIDTH, SCREEN_HEIGHT - 30),
        ),
        (Vector2(SCREEN_WIDTH, SCREEN_HEIGHT), Vector2(SCREEN_WIDTH - 30, 0)),
    ]

    for b_start, b_end in borders:
        physics.add_body(
            RigidBody(
                vel=Vector2(0, 0),
                mass=0,
                shape=Rect.from_corners(b_start, b_end),
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
