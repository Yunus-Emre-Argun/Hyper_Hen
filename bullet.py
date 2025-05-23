import pygame
import boyut as c
from enemy import Enemy



class Bullet(pygame.sprite.Sprite):


    def __init__(self, x, y):
        super().__init__()


        self.bullets = []


        self.weight = 40
        self.height = 100


        self.enemy_bullets = []
        self.enemy_bullet_speed = 5
        self.enemy_bullet_weight = 20
        self.enemy_bullet_height = 30



        self.x = x
        self.y = y


        self.image = pygame.image.load("assets/raybullet.png")
        self.image = pygame.transform.scale(self.image, (self.weight, self.height))


        self.image2 = pygame.image.load("assets/egg.png")
        self.image2 = pygame.transform.scale(self.image2, (self.enemy_bullet_weight, self.enemy_bullet_height))


        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_speed = 100


        self.rect = self.image.get_rect()


    def playerBullet(self, player):
        bulletX = player.x + player.width // 2 - self.weight // 2
        bulletY = player.y
        self.bullets.append([bulletX, bulletY])


    def moveBullet(self):
        for bullet in self.bullets:
            bullet[1] -= 10


        self.bullets = [b for b in self.bullets if b[1] > -self.height]


    def enemyBullet(self,enemy):
        bulletX = enemy.enemyX + enemy.width // 2
        bulletY = enemy.enemyY + enemy.height
        self.enemy_bullets.append([bulletX, bulletY])

    def bulletCrashEnemy(self, enemy):
        for bullet in self.bullets:
            rect1 = pygame.Rect(bullet[0], bullet[1], self.weight, self.height)
            rect2 = pygame.Rect(enemy.enemyX, enemy.enemyY, enemy.width, enemy.height)
            if rect1.colliderect(rect2):
                try:
                    self.bullets.remove(bullet)
                except ValueError:
                    pass

                enemy.reduce_health()
                enemy.get_hit(bullet)
                return True
        return False


    def enemyBulletCrashPlayer(self, enemy, player, bullet):
        for b in bullet.enemy_bullets[:]:
            rect1 = pygame.Rect(b[0], b[1], bullet.enemy_bullet_weight, bullet.enemy_bullet_height)
            rect2 = pygame.Rect(player.x, player.y, player.width, player.height)

            if rect1.colliderect(rect2):
                
                #player piksel kontrolü için (temas uzaklığı)
                offset = (rect1.x - rect2.x, rect1.y - rect2.y)
                if player.mask.overlap(pygame.mask.Mask((rect1.width, rect1.height), fill=True), offset):
                    self.enemy_bullets.remove(b)
                    player.reduce_health()



    def enemymoveBullets(self):
        for bullet in self.enemy_bullets:
            bullet[1] += self.enemy_bullet_speed+Enemy.currentEnemyBulletSpeed


        self.enemy_bullets = [b for b in self.enemy_bullets if b[1] < c.DISPLAY_HEIGHT]


    def draw(self, screen):
        for bullet in self.bullets:
            screen.blit(self.image, (bullet[0], bullet[1]))
