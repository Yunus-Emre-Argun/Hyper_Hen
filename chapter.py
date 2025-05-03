import pygame
import random
from enemy import Enemy

class ChapterOne:
    def __init__(self):
        # Enemy sınıfı artık c1.png ve c2.png kullanacak ve ölçeklendirilmiş olacak
        self.enemy = Enemy(random.randint(50, 750), random.randint(50, 200))
        self.missionPass = False

    def draw(self, screen):
        if self.enemy is not None:
            self.enemy.update() # Animasyonu ve hareketi güncelle
            self.enemy.drawEnemy(screen)

class ChapterTwo:
    def __init__(self):
        # Enemy sınıfı artık c1.png ve c2.png kullanacak ve ölçeklendirilmiş olacak
        self.enemy1 = Enemy(random.randint(50, 750), random.randint(50, 200))
        self.enemy2 = Enemy(random.randint(50, 750), random.randint(50, 200))
        self.missionPass = False

    def draw(self, screen):
        if self.enemy1 is not None:
            self.enemy1.update()
            self.enemy1.drawEnemy(screen)
        if self.enemy2 is not None:
            self.enemy2.update()
            self.enemy2.drawEnemy(screen)