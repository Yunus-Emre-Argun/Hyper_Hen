import pygame
import random
import boyut as c

class Yildiz(pygame.sprite.Sprite):
    def __init__(self):
        super(Yildiz, self).__init__()
        self.width = random.randrange(5, 7)
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH)
        self.rect.y = random.randrange(c.DISPLAY_HEIGHT, c.DISPLAY_HEIGHT + 100)  # Başlangıç y pozisyonu ekran dışında
        self.vel_x = 0
        self.vel_y = random.randrange(4, 28)  # Yıldızın hızını rastgele belirliyoruz

    def update(self):
        # Yıldızın yukarı hareket etmesini sağlıyoruz
        self.rect.x += self.vel_x
        self.rect.y -= self.vel_y  # Yukarı hareket

        # Ekranın dışına çıkarsa yeniden ekranın alt kısmından başlasın
        if self.rect.y < 0:
            self.rect.y = random.randrange(c.DISPLAY_HEIGHT, c.DISPLAY_HEIGHT + 100)  # Alt taraftan yeniden başlatıyoruz
            self.rect.x = random.randrange(0, c.DISPLAY_WIDTH)  # Yıldızın X pozisyonunu da rastgele belirliyoruz
