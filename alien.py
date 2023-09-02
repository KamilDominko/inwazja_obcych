import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Klasa przedstawiającego pojedyńczego obcego we flocie."""

    def __init__(self, game):
        """Inicjalizacja obcego i zdefiniowanie jego położenia początkowego."""
        super().__init__()
        self.screen = game.screen

        # Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load('images/alien2.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obcego w pobliżu lewego rogu ekranu.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowywanie dokładnego poziomego położenia obcego.
        self.x = float(self.rect.x)
