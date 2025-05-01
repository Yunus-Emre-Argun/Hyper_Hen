import pygame
import random

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        self.bullets = []
        self.weight = 5
        self.height = 10
        self.enemy_bullets = []
        self.enemy_bullet_speed = 5
        self.enemy_bullet_weight = 5
        self.enemy_bullet_height = 15

    def playerBullet(self, player):
        bulletX = player.x + player.width // 2 - self.weight // 2
        bulletY = player.y
        self.bullets.append([bulletX, bulletY])

    def moveBullet(self):
        for bullet in self.bullets:
            bullet[1] -= 10
        self.bullets = [b for b in self.bullets if b[1] > -self.height]

    def bulletCrashEnemy(self, enemy):
        import pygame
        if enemy is None:
            return False
        for bullet in self.bullets:
            rect1 = pygame.Rect(bullet[0], bullet[1], self.weight, self.height)
            rect2 = pygame.Rect(enemy.enemyX, enemy.enemyY, enemy.width, enemy.height)
            if rect1.colliderect(rect2):
                try:
                    self.bullets.remove(bullet)
                except ValueError:
                    pass
                return True
        return False

    def enemyBulletCrashPlayer(self, player):
        import pygame
        for bullet in self.enemy_bullets:
            rect1 = pygame.Rect(bullet[0], bullet[1], self.enemy_bullet_weight, self.enemy_bullet_height)
            rect2 = pygame.Rect(player.x, player.y, player.width, player.height)
            if rect1.colliderect(rect2):
                try:
                    self.enemy_bullets.remove(bullet)
                except ValueError:
                    pass
                return True
        return False

    def enemyMoveBullet(self):
        for bullet in self.enemy_bullets:
            bullet[1] += self.enemy_bullet_speed
        self.enemy_bullets = [b for b in self.enemy_bullets if b[1] < 800]

    def draw(self, screen):
        import pygame
        for bullet in self.bullets:
            pygame.draw.rect(screen, (255, 255, 0), (bullet[0], bullet[1], self.weight, self.height))
        for bullet in self.enemy_bullets:
            pygame.draw.rect(screen, (255, 0, 0), (bullet[0], bullet[1], self.enemy_bullet_weight, self.enemy_bullet_height))

    def enemyBullet(self, enemy):
        if enemy is not None:
            bulletX = enemy.enemyX + enemy.width // 2 - self.enemy_bullet_weight // 2
            bulletY = enemy.enemyY + enemy.height
            self.enemy_bullets.append([bulletX, bulletY])