import random
import sys

import pygame

from star import Star
from settings import Settings
from button import Button
from space_invaders import Game


class Program:
    """Główna klasa programu."""

    def __init__(self):
        pygame.init()
        self.running = True
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Test Menu")
        self.stars = pygame.sprite.Group()

        self.create_buttons()
        self._create_stars()

    def start(self):
        game = Game(self)
        game.run()

    def options(self):
        print("Options")

    def about(self):
        print("ABOUT")

    def exit(self):
        self.running = False

    # def create_buttons(self):
    #     self.buttons = []
    #     self.start_btn = Button(self, "start")
    #     self.buttons.append(self.start_btn)
    #     self.options_btn = Button(self, "options")
    #     self.buttons.append(self.options_btn)
    #     self.about_btn = Button(self, "about")
    #     self.buttons.append(self.about_btn)
    #     self.exit_btn = Button(self, "exit")
    #     self.buttons.append(self.exit_btn)

    def create_buttons(self):
        self.buttons = []
        buttons = ["Start", "Options", "About", "Exit"]
        funct = [self.start, self.options, self.about, self.exit]
        x = self.screen.get_rect().width // 2
        y = self.screen.get_rect().height // 8
        for i in range(4):
            button = Button(self, (x, y * (2 * i + 1)), buttons[i], funct[i])
            self.buttons.append(button)

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i myszkę."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)

    def _check_buttons(self, mouse_pos):
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                button.metoda()

    def _create_stars(self):
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

    def _update_screen(self):
        """Odświeżanie ekranu."""
        self.screen.fill(self.settings.bg_color)
        for star in self.stars.sprites():
            star.draw_star()
        for button in self.buttons:
            button.draw_button()
        pygame.display.flip()

    def run(self):
        """Główna pętla programu."""
        while self.running:
            self._check_events()
            self._update_stars()
            self._update_screen()


if __name__ == '__main__':
    Program().run()
