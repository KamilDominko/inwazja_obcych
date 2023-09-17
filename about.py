import sys

import pygame
from ship import Ship
from button import Button


class About:
    """Klasa tworząca ekran z informacjami programie i instrukcją jak grać."""

    def __init__(self, program):
        pygame.init()
        self.program = program
        self.running = True
        self.settings = program.settings
        self.clock = program.clock
        self.screen = program.screen
        self.font = pygame.font.SysFont(None, 48)
        self.star_manager = program.star_manager
        self.text_color = (255, 255, 255)

        btn_x = self.screen.get_rect().centerx
        btn_y = self.screen.get_rect().height // 8 * 7
        pos_cent = (btn_x, btn_y)
        self.back_btn = Button(self.screen, pos_cent, "POWRÓT", self.back)

        self._player_ships_info()
        self._high_score_info()
        self._score_wave_info()
        self._prep_info_surface()

    def back(self):
        self.running = False

    def about_info(self):
        """Wyświetla ogólne informacje o grze."""

        # Wyświetl pole na ogólne informacje o grze.
        self.screen.blit(self.about_surface, self.about_rect)

        # Wyświetl ogólne informacje o grze.
        text = "Prosta gra inspirowana space invaders z 1978 roku.\n" \
               "Gracz porusza się lewo prawo klawiszami:\n" \
               "\"A\" lub strzałka w lewo - ruch w lewo\n" \
               "\"D\" lub strzałka w prawo - ruch w prawo\n" \
               "\"SPACJA\" - strzelanie\n" \
               "\"E\" - powrót do poprzedniego ekranu\n" \
               "\"Q\" - wyjście z programu\n\n" \
               "Program opracowany na podstawie książki:\n" \
               "\"Python instrukcje dla programisty wydanie II\"\n" \
               "napisany i rozwijany przez Kamila Dominko."
        words = []
        for line in text.splitlines():
            # word = line.split(" ")
            words.append(line.split(" "))
        space = self.font.size(" ")[0]
        max_width = self.about_rect.right
        x = self.about_rect.x
        y = self.about_rect.y
        for line in words:
            for word in line:
                word_surface = self.font.render(word, True, self.text_color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = self.about_rect.x
                    y += word_height
                self.screen.blit(word_surface, (x, y))
                x += word_width + space
            x = self.about_rect.x
            y += word_height

    def blit_text(self, surface, text, pos, font, color=pygame.Color(
        'black')):
        # 2D array where each row is a list of words.
        words = [word.split(' ') for word in text.splitlines()]
        print(words)
        # The width of a space.
        space = font.size(' ')[0]
        max_width = surface.get_size()[0] // 4 * 3
        max_height = surface.get_size()[1] // 4 * 3
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    # Reset the x.
                    x = pos[0]
                    # Start on new row.
                    y += word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space
            # Reset the x.
            x = pos[0]
            # Start on new row.
            y += word_height

    def _prep_info_surface(self):
        """Tworzy pole do wyświetlenia ogólnych informacji o grze."""

        # Zrób prostokąt na centrum ekranu
        rect_x = self.screen.get_rect().width // 6.5
        rect_y = self.screen.get_rect().height // 3.7
        rect_w = self.screen.get_rect().width - rect_x * 2
        rect_h = self.screen.get_rect().height - rect_y * 2
        self.about_rect = pygame.Rect(rect_x, rect_y, rect_w, rect_h)

        # Zrób półprzezroczystą powierzchnię na tekst.
        self.about_surface = pygame.Surface(
            (self.screen.get_rect().width - rect_x * 2,
             self.screen.get_rect().height - rect_y * 2))
        self.about_surface.set_alpha(120)
        self.about_surface.fill((0, 0, 0))

    def _score_wave_info(self):
        """Tworzy w prawym górnym rogu informacje o ilości
        zdobytych punktów i numerze floty obcych"""
        self.msg_score = self.font.render("zdobyte punkty", True,
                                          self.text_color)
        self.msg_score_rect = self.msg_score.get_rect()
        self.msg_score_rect.x = self.screen.get_rect().width - \
                                self.msg_score_rect.width - 20
        self.msg_score_rect.y = self.msg_hs_rect.y

        self.msg_wave = self.font.render("numer fali", True, self.text_color)
        self.msg_wave_rect = self.msg_wave.get_rect()
        self.msg_wave_rect.top = self.msg_score_rect.bottom + 10
        self.msg_wave_rect.right = self.msg_score_rect.right

    def _high_score_info(self):
        """Tworzy u góry na środku ekranu informacje o najwyższym wyniku."""
        self.msg_hs = self.font.render("najwyższy wynik", True, self.text_color)
        self.msg_hs_rect = self.msg_hs.get_rect()
        self.msg_hs_rect.centerx = self.screen.get_rect().width // 2
        self.msg_hs_rect.y = self.msg_ships_rect.y

    def _player_ships_info(self):
        """Tworzy na lewo od grafiki statków informacje co przedstawiają."""
        self._prep_ships()
        self.msg_ships = self.font.render("trzy życia na gre", True,
                                          self.text_color)
        self.msg_ships_rect = self.msg_ships.get_rect()
        self.msg_ships_rect.left = self.ships.sprites()[-1].rect.right
        self.msg_ships_rect.centery = self.ships.sprites()[-1].rect.centery

    def _prep_ships(self):
        """Tworzy statki w lewym górnym rogu ekranu."""
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.settings.ship_limit):
            ship = Ship(self.program)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def _draw_msgs(self):
        """Wyświetla uprzednio przygotowane wiadomości."""
        self.screen.blit(self.msg_ships, self.msg_ships_rect)
        self.screen.blit(self.msg_hs, self.msg_hs_rect)
        self.screen.blit(self.msg_score, self.msg_score_rect)
        self.screen.blit(self.msg_wave, self.msg_wave_rect)
        self.about_info()

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i myszkę."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.back_btn.rect.collidepoint(mouse_pos):
                    self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.running = False
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.star_manager.update(self.clock.delta_time)
        self.ships.draw(self.screen)
        self._draw_msgs()
        self.back_btn.draw_button()
        pygame.display.flip()

    def run(self):
        """Głowna pętla karty About."""
        while self.running:
            self.clock.update_delta_time()
            self._check_events()
            self._update_screen()
            self.clock.tick_clock()
