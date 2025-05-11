import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 400
        self.y = 700
        self.width = 80
        self.height = 80

        self.playerDirx = 7
        self.health = 5
        self.killCounter=0

        self.heart_img = pygame.image.load("assets/heart.jpg")
        self.heart_img = pygame.transform.scale(self.heart_img, (30, 30))


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

        self.current_frame = 5
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x + self.width // 2, self.y + self.height // 2)

        self.animation_counter = 0
        self.animation_speed = 3
        self.moving_left = False
        self.moving_right = False

    def moveRight(self):
        self.x += self.playerDirx
        self.rect.x = self.x
        self.moving_right = True
        self.moving_left = False

    def moveLeft(self):
        self.x -= self.playerDirx
        self.rect.x = self.x
        self.moving_left = True
        self.moving_right = False

    def rangeControl(self):
        if self.x > 800 - self.width:
            self.x = 800 - self.width
        if self.x < 0:
            self.x = 0
        self.rect.x = self.x

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

    def reduce_health(self):
        if self.health > 0:
            self.health -= 1
        if self.health == 0:

            print("YOU LOSE!")
            pygame.quit()
            quit()

    def draw_health(self, screen):
        for i in range(self.health):
            screen.blit(self.heart_img, (10 + i * 33, 10))

