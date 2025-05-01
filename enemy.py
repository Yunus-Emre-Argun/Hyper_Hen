import pygame 


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.enemyX=50
        self.enemyY=50
        self.enemyDirx=4
        self.width=50
        self.height=50
        self.speed=5
        self.hp=3


    def moveEnemy(self):
        self.enemyX+=self.enemyDirx

    def enemyRangeControl(self):
        if self.enemyX > 750:
            self.enemyDirx = -self.enemyDirx

        if self.enemyX<0:
            self.enemyDirx=-self.enemyDirx





    def get_hit(self):
        self.hp-=1
        if self.hp <=0:
            self.destroy


    def destroy(self):
        self.kill()


    def drawEnemy(self,screen):
        import pygame
        pygame.draw.rect((screen),(255,0,0),(self.enemyX,self.enemyY,self.width,self.height))
