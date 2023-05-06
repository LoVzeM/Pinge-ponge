from pygame import *
from random import randint
mixer.init()
font.init()
mw = display.set_mode((700, 650))
display.set_caption('Ping')
BG = transform.scale(image.load('formula-1.jpg'), (700, 650))
win1_txt = font.SysFont('Bauhaus 93', 70).render('YOU WIN P1', True, (10, 200, 10))
win2_txt = font.SysFont('Bauhaus 93', 70).render('YOU WIN P2', True, (200, 10, 10))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, pic, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(pic), (w, h))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < 580:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed


P1 = Player(50, 50, 20, 70, 'red_white_stick.png', 5)
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        mw.blit(BG, (0, 0)) 
        P1.reset()
        P1.update()
        


    display.update()
    clock.tick(60)
