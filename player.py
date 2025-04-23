
class Player:
    def __init__(self):
        self.playerX = 400
        self.playerY = 700
        self.width = 50
        self.height = 50
        self.speed = 5
        self.playerDirx=4

    def moveRight(self):
        self.playerX+=self.playerDirx


    def moveLeft(self):

        self.playerX-=self.playerDirx

    def rangeControl(self):
        if self.playerX>750:
            self.playerX=750

        if self.playerX<0:
            self.playerX=0

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, (0, 255, 0), (self.playerX, self.playerY, self.width, self.height))