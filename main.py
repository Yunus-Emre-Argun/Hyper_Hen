import pygame
from bullet import Bullet
from chapter import ChapterOne, ChapterTwo
from gamelogic import GameLogic
from player import Player

# Başlangıç ayarları
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Invaders Clone")
clock = pygame.time.Clock()

player = Player()
bullet = Bullet()
gameLogic = GameLogic()
enemyBullet = Bullet()
chapterOne = ChapterOne()
chapterTwo = ChapterTwo()

enemyBulletTimer = 0
running = True

while running:
    clock.tick(60)  # 60 FPS
    screen.fill((0, 0, 0))  # Ekranı siyaha boya

    enemyBulletTimer += 1
    if enemyBulletTimer >= 60:
        enemyBullet.enemyBullet(chapterOne.enemy)
        enemyBulletTimer = 0

    enemyBullet.enemyMoveBullet()
    enemyBullet.draw(screen)

    # Olayları kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.playerBullet(player)

    # 🔥 Tuşları oku
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.moveLeft()
    elif keys[pygame.K_RIGHT]:
        player.moveRight()
    else:
        player.moving_left = False
        player.moving_right = False

    player.update_animation()

    # Mermi ve düşman mantığı
    player.rangeControl()
    bullet.moveBullet()
    bullet.bulletCrashEnemy(chapterOne.enemy)
    bullet.draw(screen)

    gameLogic.passControl(chapterOne)
    gameLogic.drawChapters(chapterOne, screen)

    enemyBullet.moveBullet()
    enemyBullet.enemyMoveBullet()
    enemyBullet.draw(screen)

    # Oyuncuyu çiz
    player.draw(screen)

    if bullet.bulletCrashEnemy(chapterOne.enemy):
        chapterOne.missionPass = True

    pygame.display.flip()

pygame.quit()
