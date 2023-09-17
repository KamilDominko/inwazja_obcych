import time

import pygame


class Clock:
    """Klasa do oblicznia delta_time i utrzymywania stałych fps"""

    def __init__(self, settings):
        self.settings = settings
        self.clock = pygame.time.Clock()
        self.delta_time = None
        self.last_time = time.time()

    def update_delta_time(self):
        """Aktualizuje delta_delta time."""
        self.delta_time = time.time() - self.last_time
        self.delta_time *= self.settings.fps
        self.last_time = time.time()

    def tick_clock(self):
        self.clock.tick(self.settings.fps)

    def show_fps(self):
        """Pokazuje fps."""
        pass
