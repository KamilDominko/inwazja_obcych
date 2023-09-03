import random
import pygame
from pygame.sprite import Sprite
from pygame import gfxdraw


class Star(Sprite):
    """Klasa tworząca egzemplarz gwiazdy, w różnej wielkości i odcieniu."""

    def __init__(self, game, center):
        super().__init__()
        self.screen = game.screen
        self.color = self._generate_color()
        self.speed = 0.1
        self.max_radius = game.settings.max_radius
        self.radius = self._generate_radius()
        self.center = center
        self.rect = pygame.Rect((center), (self.radius, self.radius))
        self.y = float(self.rect.y)

    def _generate_radius(self):
        """Funkcja losuje przedział, a następnie z tego przedziału rozmiar
        gwiazdy"""
        i = random.randrange(100)
        if i >= 0 and i <= 35:
            radius = random.randrange(self.max_radius // 4)
            self.speed = 0.20
        elif i >= 36 and i <= 60:
            radius = random.randrange(self.max_radius // 4,
                                      self.max_radius // 3)
            self.speed = 0.15
        elif i >= 61 and i <= 90:
            radius = random.randrange(self.max_radius // 3,
                                      self.max_radius // 2)
            self.speed = 0.10
        elif i >= 91 and i <= 100:
            radius = random.randrange(self.max_radius // 2, self.max_radius)
            self.speed = 0.05
        return radius

    def _generate_color(self):
        """Generuje różne kolor dla gwiazdy."""
        rand_choice = random.randint(1, 3)
        if rand_choice == 1:
            rgb = (255, 128, 0)
        elif rand_choice == 2:
            rgb = (255, 255, 0)
        elif rand_choice == 3:
            rgb = (255, 0, 0)
        return rgb

    def draw_star(self):
        """Wyświetlanie gwiadzy na ekranie."""
        pygame.draw.circle(self.screen, self.color, self.rect.center,
                           self.radius)
        # Wersja z gładszymi krawędziami
        # gfxdraw.aacircle(self.screen, self.rect.center[0], self.rect.center[1],
        #                  self.radius,
        #                  self.color)
        # gfxdraw.filled_circle(self.screen, self.rect.center[0],
        #                       self.rect.center[1],
        #                       self.radius, self.color)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
