import random
import sys
import time

import pygame

from star_manager import StarManager
from settings import Settings
from button import Button
from space_invaders import Game
from about import About
from clock import Clock


class Program:
    """Główna klasa programu."""

    def __init__(self):
        pygame.init()
        self.running = True
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Inwazja Obcych 2.0")
        self.star_manager = StarManager(self.screen, self.settings)
        self.create_buttons()

        # Utworzenie zegara
        self.clock = Clock(self.settings)

    def start(self):
        game = Game(self)
        game.run()

    def options(self):
        print("OPCJE")

    def about(self):
        about = About(self)
        about.run()

    def exit(self):
        self.running = False

    def create_buttons(self):
        self.buttons = []
        buttons = ["START", "OPCJE", "O GRZE", "WYJŚCIE"]
        funct = [self.start, self.options, self.about, self.exit]
        x = self.screen.get_rect().width // 2
        y = self.screen.get_rect().height // 8
        for i in range(4):
            button = Button(self.screen, (x, y * (2 * i + 1)),
                            buttons[i], funct[i])
            self.buttons.append(button)

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i myszkę."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False

    def _check_buttons(self, mouse_pos):
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                button.metoda()

    def _update_screen(self):
        """Odświeżanie ekranu."""
        self.screen.fill(self.settings.bg_color)
        self.star_manager.update(self.clock.delta_time)
        for button in self.buttons:
            button.draw_button()
        pygame.display.flip()

    def run(self):
        """Główna pętla programu."""
        while self.running:
            self.clock.update_delta_time()
            self._check_events()
            self._update_screen()
            self.clock.tick_clock()


if __name__ == '__main__':
    Program().run()
