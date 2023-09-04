import pygame.font


class Scoreboard:
    """Klasa przeznaczona do przedstawiania informacji o punktacji."""

    def __init__(self, game):
        """Inicjalizacja atrybutów dotyczących punktacji."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Ustawienie czcionki dla informacji dotyczących punktacji.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Przygotowanie początkowych obrazów z pynktacją.
        self.prep_score()

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz."""
        score_str = str(self.stats.points)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)

        # Wyświetlenie punktacji w prawym górnym rogu ekranu.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Wyświetlenie punktacji na ekranie."""
        self.screen.blit(self.score_image, self.score_rect)
