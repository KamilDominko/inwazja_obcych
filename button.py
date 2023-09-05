import pygame


class Button:
    """Klasa tworząca guziki."""

    def __init__(self, program, pos_cent, text, metoda):
        """Inicjalizacja atrybutów przycisku."""
        self.screen = program.screen
        self.screen_rect = self.screen.get_rect()

        # Zdefiniowanie wymiarów i właściwości przycisku.
        self.width, self.height = 200, 50
        self.button_color = (0, 50, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.metoda = metoda

        # Utworzenie prostokąta przycisku i wyśrodkowanie go.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = pos_cent

        self._prep_msg(text)

    def _prep_msg(self, text):
        self.msg_image = self.font.render(text, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def on_click(self):
        self.metoda()

    def draw_button(self):
        """Wyświetlenie pustego przycisku, a następnie komunikatu na nim"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
