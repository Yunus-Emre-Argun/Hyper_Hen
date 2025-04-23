import pygame
from bullet import Bullet
from player import Player

# Pygame başlangıcı
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Invaders Clone")
clock = pygame.time.Clock()

# Oyuncu ve mermi objeleri
player = Player()
bullet = Bullet()

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))  # Arka planı siyaha boya

    # Olaylar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Space tuşuna basıldığında mermi gönder
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.playerBullet(player)

    # Tuşlara basılı kontrol
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft()
    if keys[pygame.K_RIGHT]:
        player.moveRight()

    # Mermi hareket ettir ve çiz
    bullet.moveBullet()
    bullet.draw(screen)
    player.rangeControl()

    # Oyuncuyu çiz
    player.draw(screen)

    # Ekranı güncelle
    pygame.display.flip()

pygame.quit()
