from random import*
from pygame import*

window = display.set_mode((700,500))
display.set_caption("Space schuter")
background = transform.scale(image.load("images.jpeg"),(700,500))
game = True
finish = False
class GameSprite(sprite.Sprite):
   
    #конструктор класса
    def __init__(self,player_image,size_x,size_y,speed,x,y):
        #Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = speed

        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_(self):
        window.blit(self.image, (self.rect.x , self.rect.y ))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 310:   
             self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 310:   
             self.rect.y += self.speed   
font.init()
font1 = font.SysFont('Arial', 40)
lose1 = font1.render('PLAYER1 LOSE!',True,(180,0,0))
lose2 = font1.render('PLAYER2 LOSE!',True,(180,0,0))
wall1 = Player('ce80c5c3db6e9b7 (1) (1).png',27,190,8,50,50)
wall2 = Player('ce80c5c3db6e9b7 (1) (2).png',27,190,8,650,50)
ball = GameSprite('photo_2025-05-17_17-24-49.jpg',50,50,3,100,100)
speed_x = 2
speed_y = 2
while game:
    window.blit(background,(0,0))
    wall1.draw_()
    wall2.draw_()
    wall1.update_l()
    wall2.update_r()
    ball.draw_()
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(wall1,ball) or sprite.collide_rect(wall2,ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1,(350,250))
    if ball.rect.x > 650:
        finish = True
        window.blit(lose2,(350,250))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
