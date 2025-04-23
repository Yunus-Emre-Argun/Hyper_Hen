
class Bullet:
    def __init__(self):
        self.bullets = []

    def playerBullet(self, player):
        bullet_x = player.x + player.width // 2 - 2
        bullet_y = player.y
        self.bullets.append([bullet_x, bullet_y])

    def moveBullet(self):
        for bullet in self.bullets:
            bullet[1] -= 10


        self.bullets = [b for b in self.bullets if b[1] > 0]

    def draw(self, screen):
        import pygame
        for bullet in self.bullets:
            pygame.draw.rect(screen, (255, 255, 0), (bullet[0], bullet[1], 5, 10))
