class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry"""
        # Ustawienia ekranu.
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (230, 230, 230)
        self.bg_color = (0, 0, 50)
        self.fps = 60

        # Ustawienia dotyczące statku.
        self.ship_limit = 3

        # Ustawienia dotyczące pocisku.
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Ustawienia dotyczące gwiazd.
        self.max_radius = 15
        self.stars_allowed = 120
        self.fastest_star = 4
        self.fast_star = 3
        self.slow_star = 2
        self.slowest_star = 1

        # Ustawienia dotyczące obcych.
        self.fleet_drop_speed = 10

        # Wartość fleet_direction wynosząca 1 oznacza prawo, -1 - lewo.
        self.fleet_direction = 1

        # Łatwa zmiana szybkości gry.
        self.speedup_scale = 1.2

        # Łatwa zmiana liczby punktów przyznawanych za zestrzelenie obcego.
        self.score_scale = 1.5

        # Nazwy plików.
        self.filename_high_score = "high_score.txt"

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry."""
        # Prędkości: statku gracza, pocisków gracza, statków obcych.
        self.ship_speed = 3.5
        self.bullet_speed = 10.0
        self.alien_speed = 1.0

        # Punktacja
        self.alien_points = 50

        # Wartość fleet_direction wynosząca 1 oznacza prawo, -1 - lewo.
        self.fleet_direction = 1

    def increase_speed(self):
        """Zmiana ustawień dotyczących szybkości gry i liczby przyznawanych
        punktów."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
