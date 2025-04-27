import pygame

class Player:
    def __init__(self):
        self.x = 400
        self.y = 700
        self.width = 80  # Daha büyük genişlik
        self.height = 80 # Daha büyük yükseklik
        self.speed = 5
        self.playerDirx = 4
        self.heal = 3

        # Sprite'ları yükle
        self.frames = []
        for i in range(1, 12):
            filename = f"assets/smallfighter{str(i).zfill(4)}.png"
            try:
                frame = pygame.image.load(filename).convert_alpha()
                frame = pygame.transform.scale(frame, (self.width, self.height))
                self.frames.append(frame)
            except pygame.error as e:
                print(f"Hata: {filename} yüklenirken bir sorun oluştu: {e}")
                pygame.quit()
                quit()

        self.current_frame = 5  # Başlangıçta 6. resim (index 5)
        self.image = self.frames[self.current_frame]
        self.animation_counter = 0
        self.animation_speed = 3 # Animasyon geçiş hızı

        self.moving_left = False
        self.moving_right = False

    def moveRight(self):
        self.x += self.playerDirx
        self.moving_right = True
        self.moving_left = False

    def moveLeft(self):
        self.x -= self.playerDirx
        self.moving_left = True
        self.moving_right = False

    def rangeControl(self):
        if self.x > 800 - self.width:  # Sağ sınırı güncelle
            self.x = 800 - self.width
        if self.x < 0:
            self.x = 0

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
                if self.current_frame < 5:
                    self.current_frame += 1
                elif self.current_frame > 5:
                    self.current_frame -= 1

            self.image = self.frames[self.current_frame]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def reduceHeal(self, bullet):
        import main
        if bullet.enemyBulletCrashPlayer(self):
            self.heal -= 1
            print(main.clock.get_time())
            print(self.heal)