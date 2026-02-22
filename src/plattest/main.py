import pygame
import sys
from pygame.time import Clock
from pygame import Vector2
from plattest.entities.box_2d_entity import Box2DEntity
from plattest.rendering.camera import Camera
from plattest.physics.physics_system import PhysicsSystem
from plattest.physics.rigidbody.intersection_detection_2d import IntersectionDetection2D
from plattest.physics.rigidbody.rigid_body_2d import RigidBody2D

clock = Clock()


def main() -> None:
    camera: Camera = Camera(0, 0)

    physics = PhysicsSystem(Vector2(0, -9.8), 1 / 20)
    rb1 = RigidBody2D(Vector2(130, 600), 0, 0, 0.5)
    rb2 = RigidBody2D(Vector2(240, 600), 0, 0)

    physics.add_rigid_body(rb1)
    physics.add_rigid_body(rb2)

    rect_a: Box2DEntity = Box2DEntity(Vector2(100, 100), rb1, (0, 0, 0))
    rect_b: Box2DEntity = Box2DEntity(Vector2(100, 100), rb2, (0, 0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        rect_a._box_2d.rigid_body.rotation += 1
        if IntersectionDetection2D.box2d_and_box2d(rect_a._box_2d, rect_b._box_2d):
            rect_a.color = (0, 255, 0)
            rect_b.color = (0, 255, 0)
        else:
            rect_a.color = (255, 0, 0)
            rect_b.color = (255, 0, 0)

        camera.draw_backgroun()
        rect_a.draw(camera)
        rect_b.draw(camera)
        camera.flip()
        physics.fixed_update()
        clock.tick(60)


if __name__ == "__main__":
    main()
