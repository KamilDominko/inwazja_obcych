"""Projekt z wykorzystaniem biblioteki pygame.
Gra inwazja obcych, w której gracz steruje statkiem kosmicznym na dole
ekranu, poruszając się w lewo i prawo zestrzeliwując nadciągające wrogie
statki. Jeżeli wrogi statek dotknie gracza lub zejdzie poniżej określonej
wysokości ekranu, gracz traci jedno życie. Po zestrzeleniu wrogiego statku
gracz dostaje jeden punkt, po zniszczeniu wszystkich statków w fali dostaje
dziesięć punktów"""

import sys
import random
import time

import pygame

from alien import Alien
from bullet import Bullet
from ship import Ship
from star import Star
from game_stats import GameStats
from scoreboard import Scoreboard


class Game:
    """Główna klasa gry przeznaczona do zarządzania zasobami i sposobem
    działania gry."""

    def __init__(self, program):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.running = True
        self.settings = program.settings

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Inwazja Obcych")

        # Utworzenie egzemplarza przechowującego dane statystyczne dotyczące
        # gry.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.bg_color = self.settings.bg_color

        self._create_fleet()
        self._create_stars()
        self._start_game()

    def _create_alien(self, alien_number, row_number):
        """Utworzenie obcego i umieszczenie go w rzędzie."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Utworzenie pełnej floty obcych."""
        # Utworzenie obcego i ustalenie liczby obcych, którzy zmieszczą się w
        # rzędzie.
        # Odległość między poszczególnymi obcymi jest równa szerokości obcego.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Ustalenie ile rzędów obcych zmieści się na ekranie.
        ship_height = self.ship.rect.height
        available_space_y = (
                self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Utworzenie pełnej floty obcych.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
        # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _start_game(self):
        # Wyzerowanie ustawień dotyczących gry.
        self.settings.initialize_dynamic_settings()

        # Wyzerowanie danych statystycznych gry.
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Usunięcie zawartości list aliens i bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Utworzenie nowej floty i wyśrodkowanie statku.
        self._create_fleet()
        self.ship.center_ship()

        # Ukrycie kursora myszki.
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_g:
            if not self.stats.game_active:
                self._start_game()
        elif event.key == pygame.K_e:
            pygame.mouse.set_visible(True)
            self.running = False
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pocisków."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na
        ekranie. """
        # Uaktualnienie położenia pocisków.
        self.bullets.update()

        # Usunięcie pocisków, które znajdują się poza ekranem.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Reakcja na kolizję między pociskiem i obcym."""
        # Sprawdzenie, czy którykolwiek pocisk trafił obcego.
        # Jeżeli tak, usuwamy zarówno pocisk, jak i obcego.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)
        # Moja metoda sprawia, że zestrzelenie wielu obcych zlicza punkty z
        # każdego zestrzelonego obcego, a nie tylko z pierwszego poprzez
        # wywołanie metody z obcego. Trzeba zmienić w powyższej metodzie
        # sprite.groupcollide ostatni argument na False, aby statek obcego
        # nie był od razu kasowany.
        # for alien in collisions.values():
        #     for a in alien:
        #         a.hit(self.aliens)

        if collisions:
            for aliens in collisions.values():
                self.stats.points += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Pozbycie się istniejących pocisków i utworzenie nowej floty.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Inkrementacja numeru poziomu.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        # Odświeżenie ekranu w trakcie każdej iteracji pętli.
        self.screen.fill(self.bg_color)
        for star in self.stars.sprites():
            star.draw_star()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Wyświetlenie informacji o punktacji.
        self.sb.show_score()
        # Wyświetlenie ostatnio zmodyfikowanego ekranu.
        pygame.display.flip()

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

    def _ship_hit(self):
        """Reakcja na uderzenie obcego w statek."""
        if self.stats.ships_left > 0:
            # Zmniejszenie wartości przechowywanej w ships_left i
            # uaktualnienie tablicy wyników.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Usunięcie zawartości list aliens i bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Utworzenie nowej floty i wyśrodkowanie statku.
            self._create_fleet()
            self.ship.center_ship()

            # Pauza
            time.sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Sprawdzenie, czy którykolwiek obcy dotarł do dolnej krawędzi
        ekranu."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Tak samo, jak w przypadku zderzenia statku z obcym.
                self._ship_hit()
                break

    def _update_aliens(self):
        """Sprawdzenie, czy flota obcych znajduje się przy
        krawędzi, a następnie uaktualnienie położenia wszystkich obcych we
        flocie."""
        self._check_fleet_edges()
        self.aliens.update()

        # Wykrywanie kolizji między obcym i statkiem.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Wyszukiwanie obcych docierających do dolnej krawędzi ekranu.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Przesunięcie całej floty w dół i zmiana kierunku, w którym się
        ona porusza."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def run(self):
        """Rozpoczęcie głównej pętli gry."""
        while self.running:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_stars()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie
    game = Game()
    game.run()
