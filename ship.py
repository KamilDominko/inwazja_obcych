import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Klasa przeznaczona do zarządzania statkiem kosmicznym gracza"""

    def __init__(self, game):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Wczytanie obrazu statku i pobranie jego prostokąta
        self.image = pygame.image.load("images/ship6.bmp")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        # Każdy nowy statek pojawia się na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom

        # Położenie poziome statku jest przechowywane w postaci liczby
        # zmiennoprzecinkowej.
        self.x = float(self.rect.x)

        # Opcje wskazujące na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Uaktualnienie położenia statku na podstawie opcji wskazującej na
        jego ruch"""
        # Uaktualnienie wartości współrzędnej X statku, a nie jego prostokąta.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Uaktualnienie obiektu rect na podstawie wartości self.x.
        self.rect.x = self.x

    def blitme(self):
        """Wyświetlenie statku kosmiczniego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Umieszczenie satku na środku przy dolnej krawędzi ekranu."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
