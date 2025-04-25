import pygame
from bullet import Bullet
from chapter import ChapterOne

from player import Player


pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()




player = Player()
bullet = Bullet()

enemyBullet=Bullet()


chapterOne=ChapterOne()


def passControl():
    if chapterOne.missionPass is True:
        chapterOne.enemy=None

enemyBulletTimer = 0

running = True






while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    enemyBulletTimer += 1
    if enemyBulletTimer >= 60:
        enemyBullet.enemyBullet(chapterOne.enemy)
        enemyBulletTimer = 0

    enemyBullet.enemyMoveBullet()

    enemyBullet.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.playerBullet(player)

        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                bullet.playerBullet(player)
                bullet.draw(screen)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft()
    if keys[pygame.K_RIGHT]:
        player.moveRight()


    passControl()

    player.reduceHeal(enemyBullet)
    bullet.moveBullet()
    bullet.bulletCrashEnemy(chapterOne.enemy)
    bullet.draw(screen)
    player.rangeControl()
    chapterOne.enemy.moveEnemy()
    chapterOne.enemy.enemyRangeControl()
    chapterOne.enemy.drawEnemy(screen)
    enemyBullet.moveBullet()

    enemyBullet.enemyMoveBullet()
    enemyBullet.draw(screen)

    player.draw(screen)

    if bullet.bulletCrashEnemy(chapterOne.enemy):
        chapterOne.missionPass=True





    pygame.display.flip()

pygame.quit()
