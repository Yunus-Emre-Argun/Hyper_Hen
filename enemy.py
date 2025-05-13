import pygame
import random
import boyut as c

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Başlangıç pozisyonu rastgele belirleniyor
        self.enemyX = random.randrange(50, c.DISPLAY_WIDTH - 50)
        self.enemyY = random.randrange(50, 150)

        # Hareket yönü ve boyutlar
        self.enemyDirx = 2
        self.width = 50
        self.height = 50
        self.hp = 3
        self.score_value = 5  # Hasar aldığında gelecek puan miktarı
        
        # Animasyon çerçeveleri ve yükleme işlemi
        self.frames = []
        self.load_frames()
        
        # Hasar animasyonu
        self.damageDuration = 150
        self.damaged_frames = [self.toRed(frame.copy()) for frame in self.frames]
        
        # Animasyon durumu
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_speed = 100

        # Hasar kontrolü
        self.isDamaged = False
        self.damage_Time = 0

        # Mermi özellikleri
        self.enemy_bullet_speed = 5
        self.enemy_bullets = []

    # Çerçeveleri kırmızıya boyayan fonksiyon
    def toRed(self, image):
        red_image = image.copy()

        # Kırmızı ton ekle (her pikselin RGB değerlerini kırmızıya çeker ama alpha'yı korur)
        arr = pygame.surfarray.pixels3d(red_image)
        arr[:, :, 1] = arr[:, :, 1] // 3  # Yeşili azalt
        arr[:, :, 2] = arr[:, :, 2] // 3  # Maviyi azalt
        del arr  # Kilidi bırak (aksi halde başka işleme izin vermez)

        return red_image

    # Hasar aldığında flaş efekti başlatan fonksiyon
    def damageFlash(self, bullet):
        self.isDamaged = True
        self.damage_Time = pygame.time.get_ticks()

    # Çerçeveleri yükleyen fonksiyon
    def load_frames(self):
        for i in range(1, 3):
            filename = f"assets/c{i}.png"
            frame = pygame.image.load(filename).convert_alpha()
            frame = pygame.transform.scale(frame, (self.width, self.height))
            self.frames.append(frame)

    # Canı azaltan fonksiyon
    def reduce_health(self):
        if self.hp > 0:
            self.hp -= 1
        if self.hp == 0:
            self.destroy()

    # Düşmanın sağa sola hareketini sağlayan fonksiyon
    def moveEnemy(self):
        self.enemyX += self.enemyDirx

    # Düşman sağa sola çarpınca yön değiştiren fonksiyon
    def enemyRangeControl(self):
        if self.enemyX > c.DISPLAY_WIDTH - self.width or self.enemyX < 0:
            self.enemyDirx = -self.enemyDirx

    # Mermi çarpınca hasar almasını kontrol eden fonksiyon
    def get_hit(self, bullet):
        self.damageFlash(bullet)
        if self.hp <= 0:
            self.destroy()

    # Düşmanı yok eden fonksiyon
    def destroy(self):
        self.kill()

    # Düşmanın mermi ateşlemesini sağlayan fonksiyon
    def enemyBullet(self):
        bulletX = self.enemyX + self.width // 2
        bulletY = self.enemyY + self.height
        self.enemy_bullets.append([bulletX, bulletY])
        
        

    # Düşmanı ekrana çizen fonksiyon
    def draw(self, screen):
        now = pygame.time.get_ticks()

        # Animasyon güncelleniyor
        if now - self.last_update > self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = now

        # Hasar flaşı kontrolü
        if self.isDamaged:
            if now - self.damage_Time > self.damageDuration:
                self.isDamaged = False

        # Hasar almışsa kırmızı animasyon, değilse normal animasyon gösterilir
        if self.isDamaged:
            current_image = self.damaged_frames[self.current_frame]
        else:
            current_image = self.frames[self.current_frame]

        # Ekrana çizdirme işlemi
        screen.blit(current_image, (self.enemyX, self.enemyY))

    # Düşman mermilerinin hareketi
    def moveBullets(self):
        for bullet in self.enemy_bullets:
            bullet[1] += self.enemy_bullet_speed
        
        # Ekranın dışına çıkan mermileri temizle
        self.enemy_bullets = [b for b in self.enemy_bullets if b[1] < c.DISPLAY_HEIGHT]
