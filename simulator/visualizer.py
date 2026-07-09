import pygame
from .simulation import Simulation


class Visualizer:
    def __init__(self, simulation: Simulation, width: int = 800, height: int = 1200):
        self.width = self._validate_size("width", width)
        self.height = self._validate_size("height", height)
        self.simulation = simulation

    @staticmethod
    def _validate_size(self, name, value):  # checks if width/height is valid
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()
        running = True
        dt = 0

        while running:
            for event in pygame.event.get():  # if user needs to quit
                if event.type == pygame.QUIT:
                    running = False
            self.simulation.step(dt) # update any values
            # update screen & limit FPS to 60
            screen.fill("white")
            self._draw_bodies(screen)
            pygame.display.flip()
            dt = clock.tick(60) / 1000

        pygame.quit()

    def _draw_bodies(self, screen):
        for body in self.simulation.bodies:
            pygame.draw.circle(screen, body.color, body.position, body.radius)
