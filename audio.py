
import pygame




class Audio:
    def __init__(self):
        self.laserSound=pygame.mixer.Sound("assets/sounds/laser-104024.mp3")
        self.laserSound.set_volume(0.3)
        self.chickenGetHit=pygame.mixer.Sound("assets/sounds/chicken5a(die).mp3")
        self.chickenGetHit.set_volume(0.3)
        pygame.mixer.music.load("assets/sounds/8bit-spaceshooter.mp3")


