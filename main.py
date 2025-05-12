import pygame
import random



from bullet import Bullet
from player import Player
from enemy import Enemy
from arkaplan import AP
import boyut as  c
from audio import Audio





pygame.init()
screen = pygame.display.set_mode(c.DISPLAY_SIZE)
pygame.display.set_caption("SPACE GAME")
clock = pygame.time.Clock()



ap = AP()
ap_group = pygame.sprite.Group()
ap_group.add(ap)



sound=Audio()

player = Player()
bullet = Bullet(player.x, player.y)
pygame.mixer.music.play(-1)

def create_enemies():
    enemies = []
    for _ in range(random.randint(4, 15 )):
        enemies.append(Enemy())
    return enemies


enemies = create_enemies()

enemyBulletTimer = 0
running = True


while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    enemyBulletTimer += 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.playerBullet(player)
                sound.laserSound.play()



    keys = pygame.key.get_pressed()
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

    bullet.moveBullet()
    for enemy in enemies[:]:
        if bullet.bulletCrashEnemy(enemy):
            sound.chickenGetHit.play()
            if enemy.hp <= 0:
                enemies.remove(enemy)
                player.score=player.score+5


    enemyCounter=len(enemies)

    if enemyCounter == 0:
        if player.health<5:
            player.health=player.health+1




    bullet.draw(screen)

    for enemy in enemies:
        enemy.moveEnemy()
        enemy.enemyRangeControl()
        enemy.moveBullets()
        enemy.draw(screen)
        bullet.enemyMoveBullet()
        bullet.enemyBulletCrashPlayer(enemy, player, bullet)




        if enemy is not None:
            for bul in enemy.enemy_bullets:
                screen.blit(bullet.image2, ((bul[0], bul[1])))


        if enemyBulletTimer >= 60:
            enemy.enemyBullet()




    if enemyBulletTimer >= 60:
        enemyBulletTimer = 0



    player.draw(screen)
    player.draw_health(screen)
    player.score_draw(screen)


    if len(enemies) == 0:
        enemies = create_enemies()

    pygame.display.update()

pygame.quit()
