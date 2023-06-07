from pygame import *
import random

window = display.set_mode((700, 500))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("kviddich2.jpg"), (700, 500))

# mixer.init()
# mixer.music.load("space.ogg")
# mixer.music.play()

clock = time.Clock()

FPS = 60

finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_p1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        
        if keys_pressed[K_DOWN] and self.rect.y < 340:
            self.rect.y += self.speed 

    def update_p2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        
        if keys_pressed[K_s] and self.rect.y < 340:
            self.rect.y += self.speed 


# lost = 0

# class Enemy(GameSprite):
#     def update(self):
#         global lost
#         self.rect.y += self.speed
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = random.randint(100, 600)
#             lost = lost + 1

# class Asteroid(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = random.randint(100, 600)

player1 = Player("metlaa.jpg", 0, 100, 8, 85, 160)
player2 = Player("metlaa.jpg", 620, 100, 8, 85, 160)

# font.init()
# font1 = font.SysFont("Arial", 36)
# font2 = font.SysFont("Arial", 44)
# font3 = font.SysFont("Arial", 56)

# enemies = sprite.Group()

# for i in range(5):
#     enemy = Enemy("ufo.png", random.randint(100, 600), 0, random.randint(1, 2), 64, 64)
#     enemies.add(enemy)

# asteroids = sprite.Group()

# for i in range(3):
#     asteroid = Asteroid("asteroid.png", random.randint(100, 600), 0, random.randint(1, 2), 60, 60)
#     asteroids.add(asteroid)

game = True

# amount = 0

# win = font2.render("YOU ARE THE CHAMPION, MY FRIEND!", True, (0, 255, 0))
# defend = font3.render("HAHA! LOSER", True, (255, 0, 0))



while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 player.fire()

    if finish != True:
            
        player1.reset()
        player1.update_p1()
        player2.reset()
        player2.update_p2()
#         enemy.reset()
#         enemy.update()
#         enemies.draw(window)
#         enemies.update()
#         bullets.draw(window)
#         bullets.update()
#         asteroid.update()
#         asteroid.reset()

#         sprites_list = sprite.groupcollide(enemies, bullets, True, True)
        
#         for i in sprites_list:
#             amount += 1
#             enemy = Enemy("ufo.png", random.randint(100, 600), 0, random.randint(1, 2), 64, 64)
#             enemies.add(enemy)

#         text_lose = font1.render("Пропущено: " + str(lost), 1, (255, 255, 255))
#         window.blit(text_lose, (4, 60))

#         text_win = font1.render("Счёт: " + str(amount), 1, (255, 255, 255))
#         window.blit(text_win, (4, 20))

#         if amount >= 10:
#             finish = True
#             window.blit(win, (50, 250))

#         if lost >= 4 or sprite.collide_rect(player, enemy) or sprite.collide_rect(player, asteroid):
#             finish = True
#             window.blit(defend, (200, 250))

    clock.tick(FPS)
    display.update()