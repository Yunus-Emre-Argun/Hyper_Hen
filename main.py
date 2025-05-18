import pygame
import random
from bullet import Bullet
from player import Player
from enemy import Enemy
from arkaplan import AP
from score import Score
from alert_box import AlertBox
from menu import Menu  # Menü sınıfını import ettik
import boyut as c
from audio import Audio

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(c.DISPLAY_SIZE)
pygame.display.set_caption("SPACE GAME")
clock = pygame.time.Clock()

# Oyun objeleri
score = Score()
ap = AP()
player = Player()
bullet = Bullet(player.x, player.y)

score_group = pygame.sprite.Group()
score_group.add(score)
ap_group = pygame.sprite.Group()
ap_group.add(ap)
alert_box_group = pygame.sprite.Group()

# Menü objesi ve durum değişkeni
menu = Menu()
in_menu = True  # Menü açıkken True, oyun başlamadan önce

def create_enemies():
    enemies = []
    for _ in range(random.randint(4, 15)):
        enemies.append(Enemy())
    return enemies

enemies = create_enemies()

enemyBulletTimer = 0
enemyReduceBulletTimer = 0
running = True

audio = Audio()


while running:
    clock.tick(60)


    if in_menu:
        menu.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif menu.handle_event(event) == "start":
                pygame.mixer.music.play(-1)
                in_menu = False  # Menüyü kapat, oyunu başlat
        continue  # Menü açıkken aşağıdaki oyun kodu çalışmasın

    # Menü kapalı, oyun kısmı başlasın
    screen.fill((0, 0, 0))
    enemyBulletTimer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.is_alive:
                audio.laserSound.play()
                bullet.playerBullet(player)


        if not player.is_alive:
            for alert in alert_box_group:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if alert.is_restart_clicked(event.pos):
                        # Oyun başına dönmek için objeleri sıfırla
                        score = Score()
                        ap = AP()
                        player = Player()
                        bullet = Bullet(player.x, player.y)
                        score_group = pygame.sprite.Group()
                        score_group.add(score)
                        ap_group = pygame.sprite.Group()
                        ap_group.add(ap)
                        alert_box_group.empty()
                        enemies = create_enemies()
                        enemyBulletTimer = 0
                        enemyReduceBulletTimer = 0
                        in_menu = False
                        pygame.mixer.music.stop()
                        pygame.mixer.music.play(-1)

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

    count = len(enemies)
    if player.is_alive:
        for enemy in enemies:
            enemy.moveEnemy()
            enemy.enemyRangeControl()
            enemy.draw(screen)

            bullet.enemyBulletCrashPlayer(enemy, player, bullet)

            for bul in bullet.enemy_bullets:
                screen.blit(bullet.image2, (bul[0], bul[1]))

        if enemyBulletTimer >= 120 - enemyReduceBulletTimer:
            if len(enemies) > 3:
                for enemy in random.sample(enemies, random.randint(2, max(2, int(count/2)))):
                    bullet.enemyBullet(enemy)
            else:
                for enemy in enemies:
                    bullet.enemyBullet(enemy)
            enemyBulletTimer = 0

        bullet.draw(screen)

    chickenCount = len(enemies)

    if chickenCount == 0 and player.is_alive and player.health < 5:
        player.health += 1

    if chickenCount == 0:
        Enemy.currentSpeed()
        Enemy.currentEnemyBullSpeed()
        enemyReduceBulletTimer += 3

    if enemyReduceBulletTimer >= 30:
        enemyReduceBulletTimer = 30

    if player.is_alive:
        player.draw(screen)
        player.draw_health(screen)

    score_group.draw(screen)
    bullet.enemymoveBullets()
    if len(enemies) == 0:
        enemies = create_enemies()

    # Oyun bittiğinde alert_box ekle (sadece 1 kere)
    if not player.is_alive and len(alert_box_group) == 0:
        alert_box = AlertBox("GAME OVER")
        alert_box_group.add(alert_box)

    for alert in alert_box_group:
        alert.draw(screen)

    pygame.display.update()

pygame.quit()
