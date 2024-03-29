import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Klasa przeznaczona do zarządzania pociskami wystrzeliwanymi przez
    statek."""

    def __init__(self, game):
        """Utworzenie obiektu pocisku w aktualnym położeniu statku."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # Utworzenie prostokąta pocisku w punkcie (0,0), a następnie
        # zdefiniowanie dla niego odpowiedz niego położenia.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # Położenie pocisku jest zdefiniowane za pomocą wartości
        # zmiennoprzecinkowej.
        self.y = float(self.rect.y)

    def update(self, delta_time):
        """Poruszanie pociskiem po ekranie."""
        # Uaktualnienie położenia pocisku.
        self.y -= self.settings.bullet_speed * delta_time
        # Uaktualnienie położenia prostokąta pocisku.
        self.rect.y = self.y

    def draw_bullet(self):
        """Wyświetlanie pocisku na ekranie."""
        pygame.draw.rect(self.screen, self.color, self.rect)
