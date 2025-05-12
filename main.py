import pygame
import random
from bullet import Bullet
from player import Player
from enemy import Enemy
from arkaplan import AP
from score import Score
from alert_box import AlertBox
import boyut as c

# Oyun başlatma işlemleri
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(c.DISPLAY_SIZE)
pygame.display.set_caption("SPACE GAME")
clock = pygame.time.Clock()

# Nesne oluşturma
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

# Düşman yaratma fonksiyonu
def create_enemies():
    enemies = []
    for _ in range(random.randint(4, 15)):
        enemies.append(Enemy())
    return enemies

# İlk düşman dalgası
enemies = create_enemies()

# Değişkenler
enemyBulletTimer = 0
running = True

# Ana Oyun Döngüsü
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    enemyBulletTimer += 1

    # Oyun olaylarını yakala
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Eğer karakter canlı ise ateş etmeye devam et
            if event.key == pygame.K_SPACE and player.is_alive:
                bullet.playerBullet(player)

    # Hareket Kontrolü (Canlıysa hareket edebilir)
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

    # Arka plan ve alert box güncellemeleri
    ap_group.update()
    ap_group.draw(screen)
    alert_box_group.update()

    # Mermi hareketi
    bullet.moveBullet()
    for enemy in enemies[:]:
        if bullet.bulletCrashEnemy(enemy):
            score.update_score(enemy.score_value)
            if enemy.hp <= 0:
                enemies.remove(enemy)

    # Eğer karakter ölmüşse, düşman hareketi ve ateşi durur
    if player.is_alive:
        for enemy in enemies:
            enemy.moveEnemy()
            enemy.enemyRangeControl()
            enemy.moveBullets()
            enemy.draw(screen)
            bullet.enemyMoveBullet()
            bullet.enemyBulletCrashPlayer(enemy, player, bullet)

            
            # Düşman mermilerini ekrana çiz
            for bul in enemy.enemy_bullets:
                screen.blit(bullet.image2, (bul[0], bul[1]))

            # Düşmanların ateş etme hızı ayarı (60 -> 120, 2 kat yavaşlatıldı)
            if enemyBulletTimer >= 120:
                for enemy in random.sample(enemies, min(5, len(enemies))):
                    enemy.enemyBullet()
                enemyBulletTimer = 0  

        bullet.draw(screen)

    # Eğer karakter canlıysa, çiz ve can göstergesini göster
    if player.is_alive:
        player.draw(screen)
        player.draw_health(screen)

    # Skor göstergesini çiz
    score_group.draw(screen)

    # Eğer düşman sayısı5 veya daha az kaldıysa, yeni dalga yarat
    if len(enemies) <= 5:
        enemies = create_enemies()

    # Karakter öldüyse, oyun bitti mesajı göster
    if not player.is_alive:
        alert_box = AlertBox("GAME OVER")
        alert_box_group.add(alert_box)

    # Uyarı mesajı güncellenir
    alert_box_group.draw(screen)

    # Ekranı güncelle
    pygame.display.update()

pygame.quit()
