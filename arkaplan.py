import pygame 
import boyut as c
from yildiz import Yildiz
import random



class AP(pygame.sprite.Sprite):
    def __init__(self):
        super(AP, self).__init__()
        self.image = pygame.Surface(c.DISPLAY_SIZE)
        self.color = (0,0,15)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.timer = random.randrange(1,10)


    def update(self):
        self.stars.update()
        

        for star in self.stars:#temizle
            if star.rect.y >= c.DISPLAY_HEIGHT:
                self.stars.remove(star)
        
        if self.timer ==  0:
            new_star = Yildiz()
            self.stars.add(new_star)
            self.timer = random.randrange(1,10)
        
        self.image.fill(self.color)
        self.stars.draw(self.image)
        self.timer -= 1
