import pygame


class Ship:
    """Klasa przeznaczona do zarządzania statkiem kosmicznym gracza"""

    def __init__(self, game):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Wczytanie obrazu statku i pobranie jego prostokąta
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Każdy nowy statek pojawia się na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Wyświetlenie statku kosmiczniego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)
