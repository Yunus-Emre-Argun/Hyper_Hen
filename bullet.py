
class Bullet:
    def __init__(self):
        self.bullets = []
        self.bulletX=0
        self.bulletY=0

    def playerBullet(self, player):
        bulletX = player.playerX +10
        bulletY = player.playerY
        self.bullets.append([bulletX, bulletY])

    def moveBullet(self):
        for bullet in self.bullets:
            bullet[1] -= 10



    def enemyMoveBullet(self):

        for bullet in self.bullets:
            bullet[1] += 10


        self.bullets = [b for b in self.bullets if b[1] <= 800]


    def draw(self, screen):
        import pygame
        for bullet in self.bullets:
            pygame.draw.rect(screen, (255, 255, 0), (bullet[0], bullet[1], 5, 10))

    def enemyBullet(self, enemy):

        bulletX = enemy.enemyX + enemy.width+5
        bulletY = enemy.enemyY + enemy.height
        self.bullets.append([bulletX, bulletY])

