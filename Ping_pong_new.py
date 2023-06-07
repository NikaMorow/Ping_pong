from pygame import *
import random

window = display.set_mode((700, 500))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("kviddich2.jpg"), (700, 500))

clock = time.Clock()

FPS = 60

finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.rect = Rect(player_x, player_y, size_x, size_y)
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

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed

speed_x = 1
speed_y = 1

player1 = Player("metlaa.jpg", 0, 100, 8, 85, 160)
player2 = Player("metlaa.jpg", 620, 200, 8, 85, 160)
ball = Ball("kvoffle.png", 180, 100, 0, 44, 44)

font.init()
font = font.SysFont("Arial", 36)

game = True

defend1 = font.render("HAHA! PLAYER 1 LOSER!", True, (255, 0, 0))
defend2 = font.render("HAHA! PLAYER 2 LOSER!", True, (255, 0, 0))

while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if finish != True:
            
        player1.reset()
        player1.update_p2()
        player2.reset()
        player2.update_p1()
        ball.reset()
        ball.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1

    if ball.rect.x > 600:
        finish = True
        window.blit(defend2, (200, 250))

    if ball.rect.x < 50:
        finish = True
        window.blit(defend1, (200, 250))

    clock.tick(FPS)
    display.update()