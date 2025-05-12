import pygame
import boyut as c
from yildiz import Yildiz
from planet import Planet
import random


class AP(pygame.sprite.Sprite):
    def __init__(self):
        super(AP, self).__init__()
        self.image = pygame.Surface(c.DISPLAY_SIZE)
        self.color = (0, 0, 15)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()
        self.star_timer = random.randrange(1, 10)
        self.planet_timer = random.randrange(60,120)
        self.max_planets = 4
        self.current_num_planets = 0


    def update(self):
        self.planets.update()
        for planet in self.planets:
            if planet.rect.y > c.DISPLAY_HEIGHT:
                self.planets.remove(planet)
                self.current_num_planets -= 1
        if self.planet_timer <= 0:
            if self.current_num_planets >= self.max_planets:
                pass
            else:
                new_planet = Planet()
                self.planets.add(new_planet)
                self.current_num_planets += 1
                self.planet_timer = random.randrange(60,120)
        self.stars.update()

        for star in self.stars:  # temizle
            if star.rect.y >= c.DISPLAY_HEIGHT:
                self.stars.remove(star)

        if self.star_timer == 0:
            new_star = Yildiz()
            self.stars.add(new_star)
            self.star_timer = random.randrange(1, 10)

        self.image.fill(self.color)
        self.planets.draw(self.image)
        self.stars.draw(self.image)
        self.planet_timer -= 1 
        self.star_timer -= 1
