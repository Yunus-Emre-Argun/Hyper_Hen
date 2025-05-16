import pygame
import random

from pygame.examples.testsprite import Static

import boyut as c




class Enemy(pygame.sprite.Sprite):

    currentEnemyBulletSpeed=0
    enemyCurrentSpeed=0
    def __init__(self):
        super().__init__()






        self.enemyX = random.randrange(50, c.DISPLAY_WIDTH - 50)
        self.enemyY = random.randrange(50, 340)


        self.olasilik=random.randrange(1,5)

        self.randBAslangic =None

        if self.olasilik>1 and self.olasilik<3:
            self.randBAslangic=-1

        else:
            self.randBAslangic=1

        if self.randBAslangic>0:
            self.enemyDirx = 2*self.randBAslangic+Enemy.enemyCurrentSpeed

        else:
            self.enemyDirx=2*self.randBAslangic-Enemy.enemyCurrentSpeed

        self.width = 50
        self.height = 50
        self.hp = 4
        self.score_value = 5


        self.frames = []
        self.load_frames()


        self.damageDuration = 150
        self.damaged_frames = [self.toRed(frame.copy()) for frame in self.frames]


        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_speed = 100


        self.isDamaged = False
        self.damage_Time = 0





    def toRed(self, image):
        red_image = image.copy()


        arr = pygame.surfarray.pixels3d(red_image)
        arr[:, :, 1] = arr[:, :, 1] // 3  # Yeşili azalt
        arr[:, :, 2] = arr[:, :, 2] // 3  # Maviyi azalt
        del arr  # Kilidi bırak (aksi halde başka işleme izin vermez)

        return red_image


    def damageFlash(self, bullet):
        self.isDamaged = True
        self.damage_Time = pygame.time.get_ticks()


    def load_frames(self):
        for i in range(1, 3):
            filename = f"assets/c{i}.png"
            frame = pygame.image.load(filename).convert_alpha()
            frame = pygame.transform.scale(frame, (self.width, self.height))
            self.frames.append(frame)


    def reduce_health(self):
        if self.hp > 0:
            self.hp -= 1
        if self.hp == 0:
            self.destroy()


    def moveEnemy(self):
        self.enemyX += self.enemyDirx


    def enemyRangeControl(self):
        if self.enemyX > c.DISPLAY_WIDTH - self.width or self.enemyX < 0:
            self.enemyDirx = -self.enemyDirx


    def get_hit(self, bullet):
        self.damageFlash(bullet)
        if self.hp <= 0:
            self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            self.image.fill((0, 0, 0, 0))

    def destroy(self):
        self.kill()






    def draw(self, screen):
        now = pygame.time.get_ticks()


        if now - self.last_update > self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = now


        if self.isDamaged:
            if now - self.damage_Time > self.damageDuration:
                self.isDamaged = False


        if self.isDamaged:
            current_image = self.damaged_frames[self.current_frame]
        else:
            current_image = self.frames[self.current_frame]


        screen.blit(current_image, (self.enemyX, self.enemyY))




    @staticmethod
    def currentSpeed():
        Enemy.enemyCurrentSpeed+=0.2
        if Enemy.enemyCurrentSpeed>=3.3:
            Enemy.enemyCurrentSpeed=3.3
    @staticmethod
    def currentEnemyBullSpeed():
        Enemy.currentEnemyBulletSpeed+=1.5
        if Enemy.currentEnemyBulletSpeed>=6:
            Enemy.currentEnemyBulletSpeed=6







