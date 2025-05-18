import pygame
import boyut as c

class AlertBox(pygame.sprite.Sprite):
    def __init__(self, message):
        super().__init__()
        self.font = pygame.font.SysFont("arial", 50)
        self.text_color = (255, 0, 0)  # Kırmızı renk

        self.message = message
        # Buton bölgesi için bir dikdörtgen, tıklama kontrolü için
        self.restart_rect = pygame.Rect(c.DISPLAY_WIDTH//2 - 100, c.DISPLAY_HEIGHT//2 + 50, 200, 60)

    def draw(self, screen):
        # Arka plan siyahsa zaten siyah, burada arka plan çizme

        # Mesaj yazısı (örneğin GAME OVER)
        text_surface = self.font.render(self.message, True, self.text_color)
        screen.blit(text_surface, (c.DISPLAY_WIDTH//2 - text_surface.get_width()//2, c.DISPLAY_HEIGHT//2 - 100))

        # Restart yazısı (buton arkaplanı olmadan sadece kırmızı yazı)
        restart_surface = self.font.render("RESTART", True, self.text_color)
        screen.blit(restart_surface, (self.restart_rect.centerx - restart_surface.get_width()//2,
                                      self.restart_rect.centery - restart_surface.get_height()//2))

    def is_restart_clicked(self, pos):
        return self.restart_rect.collidepoint(pos)