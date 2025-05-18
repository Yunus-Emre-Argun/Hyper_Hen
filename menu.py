import pygame
import boyut as c

class Menu:
    def __init__(self):
        self.font = pygame.font.SysFont("arial", 40)
        self.text_color = (255, 0, 0)

        self.button_rect = pygame.Rect(c.DISPLAY_WIDTH // 2 - 100, c.DISPLAY_HEIGHT // 2 - 40, 200, 80)
        self.title_font = pygame.font.SysFont("arial", 60)

    def draw(self, screen):
        screen.fill((0, 0, 0))

        # Başlık (renk kırmızı)
        title_surface = self.title_font.render("SPACE GAME", True, (255, 0, 0))
        screen.blit(title_surface, (c.DISPLAY_WIDTH // 2 - title_surface.get_width() // 2, 100))


        text_surface = self.font.render("START", True, self.text_color)
        screen.blit(
            text_surface,
            (self.button_rect.centerx - text_surface.get_width() // 2,
             self.button_rect.centery - text_surface.get_height() // 2)
        )

        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                return "start"
        return None
