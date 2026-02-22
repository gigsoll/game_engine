from pygame import Surface, Vector2
import pygame
from plattest.config import SCREEN_WIDTH, SCREEN_HEIGHT
from plattest.physics.primitives.particle import Particle


class Camera:
    def __init__(
        self, x: int, y: int, width: int = SCREEN_WIDTH, height: int = SCREEN_HEIGHT
    ) -> None:
        self.position: Vector2 = Vector2(x, y)
        self.width = width
        self.height = height
        self.screen = self.create_screen()

    def calc_screen_coords(self, world_coord: Vector2) -> Vector2:
        scree_coords: Vector2 = world_coord - self.position
        scree_coords.y = SCREEN_HEIGHT - scree_coords.y
        return scree_coords

    def transform_array(self, world_array: list[Vector2]) -> list[Vector2]:
        result: list[Vector2] = [
            self.calc_screen_coords(point) for point in world_array
        ]
        return result

    def create_screen(self) -> Surface:
        screen: Surface = pygame.display.set_mode((self.width, self.height))
        screen.fill((255, 0, 0))
        return screen

    def draw_backgroun(self) -> None:
        self.screen.fill((239, 241, 245))

    def draw_particle(self, particle: Particle) -> None:
        pos: Vector2 = self.calc_screen_coords(particle.position)
        pygame.draw.circle(self.screen, (0, 255, 0), pos, 20, 2)

    def flip(self):
        pygame.display.flip()
