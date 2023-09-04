class GameStats:
    """Monitorowanie danych statystycznych w grze."""

    def __init__(self, game):
        """Inicjalziacja danych statystycznych."""
        self.settings = game.settings
        self.reset_stats()

        # Uruchomienie gry w stanie nieaktywnym.
        self.game_active = False

        # Wczytanie najwyższego wyniku z pliku .txt.
        self.load_high_score()

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, które mogą zmieniać się w
        trakcie gry."""
        self.ships_left = self.settings.ship_limit
        self.points = 0
        self.level = 1

    def load_high_score(self):
        """Wczytuje najwyższy wynik gry z pliku high_score.txt"""
        try:
            with open(self.settings.filename_high_score) as file_object:
                high_score = file_object.read()
        except FileNotFoundError:
            self.save_high_score("0")
            self.load_high_score()
        else:
            try:
                self.high_score = int(high_score)
            except ValueError:
                self.save_high_score("0")
                self.load_high_score()
            else:
                self.high_score = int(high_score)

    def save_high_score(self, high_score):
        """Zapisuje podaną w argumencie liczbę do pliku high_score.txt"""
        with open(self.settings.filename_high_score, "w") as file_object:
            file_object.write(high_score)
