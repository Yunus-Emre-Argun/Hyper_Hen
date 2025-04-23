import pygame
from bullet import Bullet
from enemy import Enemy
from player import Player
from chapter import Chapter

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()


player = Player()
bullet = Bullet()
enemy=Enemy()
enemyBullet=Bullet()

enemyBulletTimer = 0

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    enemyBulletTimer += 1
    if enemyBulletTimer >= 60:
        enemyBullet.enemyBullet(enemy)
        enemyBulletTimer = 0

    enemyBullet.enemyMoveBullet()
    enemyBullet.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.playerBullet(player)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft()
    if keys[pygame.K_RIGHT]:
        player.moveRight()
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_SPACE]:
            bullet.playerBullet(player)
            bullet.draw(screen)



    bullet.moveBullet()
    bullet.draw(screen)
    player.rangeControl()
    enemy.moveEnemy()
    enemy.enemyRangeControl()
    enemy.drawEnemy(screen)
    enemyBullet.moveBullet()

    enemyBullet.enemyMoveBullet()
    enemyBullet.draw(screen)

    player.draw(screen)


    pygame.display.flip()

pygame.quit()
