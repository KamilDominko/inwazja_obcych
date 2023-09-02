import random
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Klasa tworząca egzemplarz gwiazdy, w różnej wielkości i odcieniu."""

    def __init__(self, game, center):
        super().__init__()
        self.screen = game.screen
        self.color = self._generate_color()
        self.max_radius = game.settings.max_radius
        self.radius = self._generate_radius()
        self.center = center

    def _generate_radius(self):
        """Funkcja losuje przedział, a następnie z tego przedziału rozmiar
        gwiazdy"""
        i = random.randrange(100)
        if i <= 30:
            radius = random.randrange(self.max_radius // 4)
        elif i > 30 and i <= 50:
            radius = random.randrange(self.max_radius // 4,
                                      self.max_radius // 3)
        elif i > 50 and i <= 80:
            radius = random.randrange(self.max_radius // 3,
                                      self.max_radius // 2)
        elif i > 80:
            radius = random.randrange(self.max_radius // 2, self.max_radius)
        return radius

    def _generate_color(self):
        """Generuje różne kolor dla gwiazdy."""
        r = random.randrange(200, 250, 10)
        g = random.randrange(200, 250, 10)
        b = random.randrange(50, 250, 50)
        return (r, g, b)

    def draw_star(self):
        """Wyświetlanie gwiadzy na ekranie."""
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)
