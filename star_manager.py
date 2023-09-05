import random

import pygame
from pygame.sprite import Sprite

from star import Star


class StarManager(Sprite):
    """Klasa do tworzenia egzemplarzy gwiazd oraz ich zarządzania."""

    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.stars = pygame.sprite.Group()

        self.create_stars()

    def create_stars(self):
        """Tworzy początkowe gwiazdy na ekranie."""
        for i in range(self.settings.stars_allowed):
            self._create_star(True)

    def _create_star(self, first=False):
        """Tworzy gwiazdę nad w losowym miejscu nad ekranem, jeżeli
        przekazano True wtedy tworzy gwiazde losowo na ekranie."""
        rand_x = random.randrange(0, self.settings.screen_width)
        if first:
            rand_y = random.randrange(0, self.settings.screen_height)
        else:
            rand_y = random.randrange(-self.settings.screen_height, 0)
        star = Star(self, (rand_x, rand_y))
        self.stars.add(star)

    def _update_stars(self):
        self.stars.update()
        # Usunięcie pocisków, które znajdują się poza ekranem.
        for star in self.stars.copy():
            if star.rect.top >= self.settings.screen_height:
                self.stars.remove(star)
                self._create_star()

    def update(self):
        self.stars.update()
        self._update_stars()
        for star in self.stars.sprites():
            star.draw_star()
