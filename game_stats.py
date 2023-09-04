class GameStats:
    """Monitorowanie danych statystycznych w grze."""

    def __init__(self, game):
        """Inicjalziacja danych statystycznych."""
        self.settings = game.settings
        self.reset_stats()

        # Uruchomienie gry w stanie nieaktywnym.
        self.game_active = False

        # Najwyższy wynik nigdy nie powinien zostać wyzerowany.
        self.high_score = 0

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, które mogą zmieniać się w
        trakcie gry."""
        self.ships_left = self.settings.ship_limit
        self.points = 0
        self.level = 1
