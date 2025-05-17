from random import*
from pygame import*

window = display.set_mode((700,500))
display.set_caption("Space schuter")
background = transform.scale(image.load("images.jpeg"),(700,500))
game = True

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
    def draw_wall(self):
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
wall1 = Player('ce80c5c3db6e9b7 (1) (1).png',27,190,8,50,50)
wall2 = Player('ce80c5c3db6e9b7 (1) (2).png',27,190,8,600,50)
while game:
    
    window.blit(background,(0,0))
    wall1.draw_()
    wall2.draw_()
    wall1.update_l()
    wall2.update_r()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
