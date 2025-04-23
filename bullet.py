
class Bullet:
    def __init__(self):
        self.bullets = []
        self.bulletX=0
        self.bulletY=0
        self.weight=5
        self.height=10

    def playerBullet(self, player):
        bulletX = player.playerX +10
        bulletY = player.playerY
        self.bullets.append([bulletX, bulletY])

    def moveBullet(self):
        for bullet in self.bullets:
            bullet[1] -= 10

    def bulletCrashEnemy(self, enemy):
        import pygame
        for bullet in self.bullets:

            rect1 = pygame.Rect(bullet[0], bullet[1], 5, 10)


            rect2 = pygame.Rect(enemy.enemyX, enemy.enemyY, enemy.width, enemy.height)


            if rect1.colliderect(rect2):
                return True

        return False

    def enemyBulletCrashPlayer(self, player):
        import pygame
        for bullet in self.bullets:
            rect1=pygame.Rect(bullet[0],bullet[1],5,10)

            rect2=pygame.Rect(player.playerX,player.playerY,player.width,player.height)

            if rect1.colliderect(rect2):
                return True

        return False

    def enemyMoveBullet(self):

        for bullet in self.bullets:
            bullet[1] += 10


        self.bullets = [b for b in self.bullets if b[1] <= 800]


    def draw(self, screen):
        import pygame
        for bullet in self.bullets:
            pygame.draw.rect(screen, (255, 255, 0), (bullet[0], bullet[1], self.height, self.weight))

    def enemyBullet(self, enemy):

        bulletX = enemy.enemyX + enemy.width+5
        bulletY = enemy.enemyY + enemy.height
        self.bullets.append([bulletX, bulletY])

