import pygame

class Player:
    def __init__(self):
        self.x = 400
        self.y = 700
        self.speed = 5

        # Sprite'ları yükle
        self.frames = []
        for i in range(1, 12):
            filename = f"assets/smallfighter{str(i).zfill(4)}.png"
            frame = pygame.image.load(filename).convert_alpha()
            self.frames.append(frame)

        self.current_frame = 5  # Başlangıçta 6. resim (index 5)
        self.image = self.frames[self.current_frame]
        self.animation_counter = 0
        self.animation_speed = 3 # Animasyon geçiş hızı (daha küçük değerler daha hızlı geçiş)

        self.moving_left = False
        self.moving_right = False

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def moveLeft(self):
        self.x -= self.speed
        self.moving_left = True
        self.moving_right = False

    def moveRight(self):
        self.x += self.speed
        self.x += self.speed
        self.moving_right = True
        self.moving_left = False

    def rangeControl(self):
        if self.x < 0:
            self.x = 0
        if self.x > 740:
            self.x = 740

    def update_animation(self):
        self.animation_counter += 1

        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            if self.moving_left:
                if self.current_frame > 0:
                    self.current_frame -= 1
            elif self.moving_right:
                if self.current_frame < 10:
                    self.current_frame += 1
            else:
                # Tuş yoksa: kademeli şekilde orta frame'e (5) geri dön
                if self.current_frame < 5:
                    self.current_frame += 1
                elif self.current_frame > 5:
                    self.current_frame -= 1

            self.image = self.frames[self.current_frame]

    def draw(self, screen):
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)

    def reduceHeal(self, enemyBullet):
        pass