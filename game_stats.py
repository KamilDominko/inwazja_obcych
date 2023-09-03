class GameStats:
    """Monitorowanie danych statystycznych w grze."""

    def __init__(self, game):
        """Inicjalziacja danych statystycznych."""
        self.settings = game.settings
        self.reset_stats()
        self.game_active = True
        self.points = 0

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, które mogą zmieniać się w
        trakcie gry."""
        self.ships_left = self.settings.ship_limit