from typing import Any
from pygame import *
from random import *
from time import time as timer

class Gamesprite(sprite.Sprite):
    def __init__(self,spr_img,rect_x,rect_y,size_x,size_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(spr_img),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Gamesprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif key_pressed[K_DOWN] and self.rect.y < 650:
            self.rect.y += self.speed
    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif key_pressed[K_s] and self.rect.y < 650:
            self.rect.y += self.speed

win_width = 900
win_height = 700
window = display.set_mode((win_width,win_height))
display.set_caption("ping pong")
background = transform.scale(image.load("/Users/macbook/Desktop/source/floor.png"),(win_width,win_height))
fps = 60
clock = time.Clock()
finnish = False
game = True
player1 = Player("/Users/macbook/Desktop/source/Ping pong/redpaddle.png",775,0,125,200,10)
player2 = Player("/Users/macbook/Desktop/source/Ping pong/bluepaddle.png",0,0,125,200,10)
ball = Gamesprite("/Users/macbook/Desktop/source/Ping pong/ball.png",200,200,50,50,3)
speedx = 3
speedy = -3
font.init()
font2 = font.Font(None,36)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finnish != True:
        window.blit(background,(0,0))
        ball.rect.x += speedx
        ball.rect.y += speedy
        if ball.rect.y < 0:
            speedy *= -1
        elif ball.rect.y > 650:
            speedy *= -1
        if sprite.collide_rect(ball,player1) or sprite.collide_rect(ball,player2):
            speedx *= -1
        if ball.rect.x < 0:
            finnish = True
            lose = font2.render("Player2 loses",1,(255,255,255))
            window.blit(lose,(380,350))
        elif ball.rect.x > 900:
            finnish = True
            lose = font2.render("Player1 loses",1,(255,255,255))
            window.blit(lose,(380,350))
        ball.reset()
        player1.update()
        player1.reset()
        player2.update2()
        player2.reset()
        clock.tick()
        display.update()
    else:
        finnish = False
        time.delay(1000)
        ball.rect.x = 200
        ball.rect.y = 200
        speedx = 3
        speedy = -3