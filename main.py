import pygame
from player import Player
from bullet import Bullet
from chapter import ChapterOne, ChapterTwo # Chapter sınıflarını import et

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Invaders Clone")
clock = pygame.time.Clock()

player = Player()
bullet = Bullet()

# Bölümleri oluştur
chapterOne = ChapterOne()
chapterTwo = ChapterTwo()
aktif_bolum = 1 # Başlangıç bölümü

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.playerBullet(player)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft()
    elif keys[pygame.K_RIGHT]:
        player.moveRight()
    else:
        player.moving_left = False
        player.moving_right = False

    player.update_animation()
    bullet.moveBullet()
    player.rangeControl()
    bullet.draw(screen)
    player.draw(screen)

    # Aktif bölümü çiz
    if aktif_bolum == 1:
        chapterOne.draw(screen)
    elif aktif_bolum == 2:
        chapterTwo.draw(screen)

    pygame.display.flip()

pygame.quit()   