"""Projekt z wykorzystaniem biblioteki pygame.
Gra inwazja obcych, w której gracz steruje statkiem kosmicznym na dole
ekranu, poruszając się w lewo i prawo zestrzeliwując nadciągające wrogie
statki. Jeżeli wrogi statek dotknie gracza lub zejdzie poniżej określonej
wysokości ekranu, gracz traci jedno życie. Po zestrzeleniu wrogiego statku
gracz dostaje jeden punkt, po zniszczeniu wszystkich statków w fali dostaje
dziesięć punktów"""

import sys

import pygame

from settings import Settings
from ship import Ship


class Game:
    """Główna klasa gry przeznaczona do zarządzania zasobami i sposobem
    działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Inwazja Obcych")

        self.ship = Ship(self)
        self.bg_color = self.settings.bg_color

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
        # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        # Odświerzenie ekranu w trakcie każdej iteracji pętli.
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        # Wyświetlenie ostatnio zmodyfikowanego ekranu.
        pygame.display.flip()

    def run(self):
        "Rozpoczęcie głównej pętli gry."
        while True:
            self._check_events()
            self._update_screen()


if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie
    game = Game()
    game.run()
