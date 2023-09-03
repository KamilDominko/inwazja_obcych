import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Klasa przedstawiającego pojedyńczego obcego we flocie."""

    def __init__(self, game):
        """Inicjalizacja obcego i zdefiniowanie jego położenia początkowego."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load('images/alien2.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obcego w pobliżu lewego rogu ekranu.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowywanie dokładnego poziomego położenia obcego.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Zwraca wartość True, jeśli obcy znajduje się przy krawędzi ekranu."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Przesunięcie obcego w prawo lub lewo."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
