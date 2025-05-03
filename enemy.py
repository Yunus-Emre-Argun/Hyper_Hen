import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [
            pygame.image.load("assets/c1.png").convert_alpha(),
            pygame.image.load("assets/c2.png").convert_alpha()
        ]
        # İlk görselin boyutlarını al
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(x, y))

        # İstediğiniz küçültme oranını belirleyin
        self.scale_factor = 0.5
        self.new_width = int(self.rect.width * self.scale_factor)
        self.new_height = int(self.rect.height * self.scale_factor)

        # Görselleri yeniden boyutlandır
        self.scaled_images = [
            pygame.transform.scale(img, (self.new_width, self.new_height)) for img in self.images
        ]
        self.image = self.scaled_images[0]
        self.rect = self.image.get_rect(topleft=(x, y)) # Rect'i yeniden oluştur

        self.speed_x = 2
        self.move_direction = 1
        self.animation_index = 0
        self.animation_speed = 10  # Animasyon hızı YAVAŞLATILDI (değeri artırıldı)
        self.animation_counter = 0
        self.enemyX = x   # Başlangıç x koordinatı
        self.enemyY = y   # Başlangıç y koordinatı
        self.width = self.new_width
        self.height = self.new_height
        self.enemyDirx = self.speed_x * self.move_direction # Başlangıç hareket yönü

    def update_animation(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.animation_index = (self.animation_index + 1) % len(self.scaled_images)
            self.image = self.scaled_images[self.animation_index]
            self.rect = self.image.get_rect(topleft=self.rect.topleft) # Rect'i güncelle

    def moveEnemy(self):
        self.rect.x += self.speed_x * self.move_direction
        self.enemyX = self.rect.x # enemyX'i güncelle

    def enemyRangeControl(self):
        if self.rect.right > 800:
            self.move_direction *= -1
        if self.rect.left < 0:
            self.move_direction *= -1
        self.enemyDirx = self.speed_x * self.move_direction # enemyDirx'i güncelle

    def update(self):
        self.moveEnemy()
        self.enemyRangeControl()
        self.update_animation()

    def drawEnemy(self, screen):
        screen.blit(self.image, self.rect)