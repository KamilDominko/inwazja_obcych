class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry"""
        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (230, 230, 230)
        self.bg_color = (0, 0, 50)
        self.ship_speed = 1.5
        # Ustawienia dotyczące pocisku
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_collor = (60, 60, 60)
        self.bullets_allowed = 3
        # Ustawienia dotyczące gwiazd
        self.max_radius = 20
        self.stars_allowed = 60
        # Ustawienia dotyczące obcych
        self.alien_speed = 0.1
        self.fleet_drop_speed = 10
        # Wartość fleet_direction wynosząca 1 oznacza prawo, -1 - lewo.
        self.fleet_direction = 1
