import pygame
import random
from bullet import Bullet
from player import Player
from enemy import Enemy
from arkaplan import AP
from score import Score
from alert_box import AlertBox
import boyut as c
from audio import Audio

# Oyun başlatma işlemleri
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(c.DISPLAY_SIZE)
pygame.display.set_caption("SPACE GAME")
clock = pygame.time.Clock()


score = Score()
ap = AP()
player = Player()
bullet = Bullet(player.x, player.y)

# Sprite Grupları
score_group = pygame.sprite.Group()
score_group.add(score)
ap_group = pygame.sprite.Group()
ap_group.add(ap)
alert_box_group = pygame.sprite.Group()


def create_enemies():
    enemies = []
    for _ in range(random.randint(4, 15)):
        enemies.append(Enemy())
    return enemies


enemies = create_enemies()

enemyBulletTimer = 0
running = True

audio=Audio()

pygame.mixer.music.play(-1)

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    enemyBulletTimer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and player.is_alive:
                audio.laserSound.play()
                bullet.playerBullet(player)

    keys = pygame.key.get_pressed()
    if player.is_alive:
        if keys[pygame.K_LEFT]:
            player.moveLeft()
        elif keys[pygame.K_RIGHT]:
            player.moveRight()
        else:
            player.moving_left = False
            player.moving_right = False

        player.update_animation()
        player.rangeControl()

    ap_group.update()
    ap_group.draw(screen)
    alert_box_group.update()

    bullet.moveBullet()
    for enemy in enemies[:]:
        if bullet.bulletCrashEnemy(enemy):

            audio.chickenGetHit.play()
            if enemy.hp <= 0:
                enemies.remove(enemy)
                score.update_score(enemy.score_value)

    if player.is_alive:
        for enemy in enemies:
            enemy.moveEnemy()
            enemy.enemyRangeControl()
            enemy.moveBullets()
            enemy.draw(screen)
            bullet.enemyMoveBullet()
            bullet.enemyBulletCrashPlayer(enemy, player, bullet)

            for bul in enemy.enemy_bullets:
                screen.blit(bullet.image2, (bul[0], bul[1]))

            if enemyBulletTimer >= 120:
                for enemy in random.sample(enemies, min(6, len(enemies))):
                    enemy.enemyBullet()

                enemyBulletTimer = 0

        bullet.draw(screen)

    chickenCount = len(enemies)


    if chickenCount == 0 and player.is_alive and player.health < 5:
        player.health = player.health + 1
        Enemy.currentSpeed()
        Enemy.currentEnemyBullSpeed()







    if player.is_alive:
        player.draw(screen)
        player.draw_health(screen)


    score_group.draw(screen)

    if len(enemies) == 0:
        enemies = create_enemies()

    if not player.is_alive:
        alert_box = AlertBox("GAME OVER")
        alert_box_group.add(alert_box)


    alert_box_group.draw(screen)

    # Ekranı güncelle
    pygame.display.update()

pygame.quit()






