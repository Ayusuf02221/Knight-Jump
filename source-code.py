import pygame
import os
import sys
import random
import math
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode([800, 480])
width = 800
height = 480
fps = 30
pause = False
Dead = False
pygame.mixer.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Knight Jump")
bg = pygame.image.load('Bg.jpg')
bg5 = pygame.image.load('Bg2.jpg')
bg1 = 0
bg2 = bg.get_width()
score = 0
pause = 0
Dead = 0
green = (0,200,0)
bright_green = (0,255,0)
black = (0,0,0)
bright_red = (255,0,0)
red = (200,0,0)

gameover = pygame.image.load('Game Over.png')
logos = pygame.image.load('logo.gif')
button1 = pygame.image.load('Buttons.png')
jumping = pygame.mixer.Sound("Jump.wav") # Sound for jump
attacke = pygame.mixer.Sound("attack.wav")# Sound for enemy attack
Rightw = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png')] #Sprite image for player
Leftw = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png')]#Sprite image for player
bloc1 = pygame.image.load('block1.png')# block image
sblock = pygame.image.load('starterblock.png')
damage = pygame.image.load('standing.png')
spike1 = pygame.image.load('spikes.png')
bloc2 = pygame.image.load('Block2.png')

class knight(pygame.sprite.Sprite):#Class for player
    def __init__(self, x, y, width, height): #Function is set to the x axis, y axis, width of image and height of image(not actual sprite image)
        self.x = x #Makes self = to x axis
        self.y = y #Makes self = to y axis
        self.width = width #Makes self = to width
        self.height = height #Makes self = to height
        self.speed1 = 3 #speed1 of sprite
        self.jump = False #Variable for Function
        self.jumpheight = 8# Value for height Jump
        self.right = False #Variable for right
        self.left = False # Variable for left
        self.attackr = False
        self.attackl = False
        self.dead = False
        self.sfx = False
        self.wc = 0 #Counts the steps taken by sprites
        self.s = True
    def gamewin(self, win):#Draws the sprite
        if not(self.s):
            if knight1.wc + 1 >= 9: #Number of images times by 3
                self.wc = 0
            if self.dead:
                win.blit(damage,(self.x, self.y + 30))
                self.wc = 0 
            elif self.left:
                win.blit(Leftw[self.wc//3], (self.x, self.y)) #draws left sprite images
                self.wc += 1
            elif self.right:
                win.blit(Rightw[self.wc//3], (self.x, self.y)) #draws right sprite image
                self.wc += 1
        else:
            if self.dead:
                win.blit(damage[0], (self.x, self.y + 30)) 
        self.hitbox = (self.x + 30, self.y + 80, 20, 5)# Draws hitbox for player
       # pygame.draw.rect(win, (255, 0, 0), (self.hitbox),2)   



        
class starterblock(object):
    global knight1
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit = (self.x, self.y, self.width, self.height)
        self.inAir = False
    def gamewin(self,win):
        self.collision()
        self.hit = (self.x, self.y, 220, 35)
        win.blit(sblock, (self.x, self.y))
        
    def collision(self):
        if knight1.hitbox[1] < self.hit[1] + self.hit[3] and knight1.hitbox[1] + knight1.hitbox[3] > self.hit[1]:
          if knight1.hitbox[0] + knight1.hitbox[2] > self.hit[0] and knight1.hitbox[0] < self.hit[0] + self.hit[2]:
              knight1.jump = False
              knight1.jumpcount = 0
              knight1.jumpheight = 8
              knight1.y = self.y - 85
              self.inAir = True
        if knight1.x + 30 > (self.x + self.width) and self.inAir == True:
            knight1.y = 410
            self.inAir = False
 

class grassblock(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit = (self.x, self.y, self.width, self.height)
        self.inAir = False
    def gamewin(self,win):
        self.collision()
        self.hit = (self.x, self.y, 220, 35)
        win.blit(bloc2, (self.x, self.y))
       # pygame.draw.rect(win, (255,0,0), self.hit, 2)
    def collision(self):
        if knight1.hitbox[1] < self.hit[1] + self.hit[3] and knight1.hitbox[1] + knight1.hitbox[3] > self.hit[1]:
          if knight1.hitbox[0] + knight1.hitbox[2] > self.hit[0] and knight1.hitbox[0] < self.hit[0] + self.hit[2]:
              knight1.jump = False
              knight1.jumpcount = 0
              knight1.jumpheight = 8
              knight1.y = self.y - 85
              self.inAir = True
        if knight1.x + 30 > (self.x + self.width) and self.inAir == True:
            knight1.y = 410
            self.inAir = False



                
class blocks(object):
    global knight1
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit = (self.x, self.y, self.width, self.height)
        self.inAir = False
    def gamewin(self,win):
        self.collision()
        self.hit = (self.x, self.y, 220, 35)
        win.blit(bloc1, (self.x, self.y))
        #pygame.draw.rect(win, (255,0,0), self.hit, 2)
    def collision(self):
        if knight1.hitbox[1] < self.hit[1] + self.hit[3] and knight1.hitbox[1] + knight1.hitbox[3] > self.hit[1]:
          if knight1.hitbox[0] + knight1.hitbox[2] > self.hit[0] and knight1.hitbox[0] < self.hit[0] + self.hit[2]:
              knight1.jump = False
              knight1.jumpcount = 0
              knight1.jumpheight = 8
              knight1.y = self.y - 85
              self.inAir = False
        if knight1.x + 30 > (self.x + self.width) and self.inAir == True:
            knight1.y = 410
            self.inAir = False






            
class spike(object):
    global knight1
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit = (self.x, self.y, self.width, self.height)
        self.inAir = False
    def gamewin(self,win):
        self.collision()
        self.hit = (self.x, self.y, 45, 35)
        win.blit(spike1, (self.x, self.y))
       # pygame.draw.rect(win, (255,0,0), self.hit, 2)
    def collision(self):
        if knight1.hitbox[1] < self.hit[1] + self.hit[3] and knight1.hitbox[1] + knight1.hitbox[3] > self.hit[1]:
          if knight1.hitbox[0] + knight1.hitbox[2] > self.hit[0] and knight1.hitbox[0] < self.hit[0] + self.hit[2]:
              knight1.jump = False
              knight1.jumpcount = 0
              knight1.jumpheight = 8
              knight1.y = self.y - 85
              self.inAir = True
              knight1.dead = True
              run = False
        if knight1.x + 30 > (self.x + self.width) and self.inAir == True:
            knight1.y = 380
            self.inAir = False



def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',75)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    run()
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "Play":
                unpause()
            if action == "Stop":
                pygame.quit()
                quit()
            elif action == "G":
                regamewin()
                
    else:
        pygame.draw.rect(win, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)



    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)


    
def unpause():
    global pause
    pause = False


    
def paused():
    myfont = pygame.font.SysFont("comicsansms",55)
    textsurface = myfont.render('Paused', False, (0, 0, 0))
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            button("Continue",500,290,120,50,green,bright_green,"Play")
            button("Quit",150,290,120,50,red,bright_red,"Stop")
            win.blit(textsurface,(300,180))
        pygame.display.update()
        clock.tick(15)


        
def Deadd():

    myfont = pygame.font.SysFont("comicsansms",55)
    textsurface = myfont.render("Game Over", False,(0,0,0))
    while Dead:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            button("Continue",500,290,120,50,green,bright_green,"G")
            button("Quit",150,290,120,50,red,bright_red,"Stop")
            win.blit(textsurface,(250,180)) 
        pygame.display.update()
        clock.tick(15)

        

        


        
def endScreen():
    global pause, score, speed, objects, Dead
    pause = 0
    Dead = 0
    speed = 1
    objects = []    

def regamewin():
    global wc
    win.blit(bg, (bg1,0))
    win.blit(bg, (bg2,0))
    for o in objects: #draws block
        o.gamewin(win)
    knight1.gamewin(win)#draws player
    text = font.render("Score: " + str(score), 1, (0,0,0))
    win.blit(text, (390, 10))
    starterbloc.gamewin(win)
    pygame.display.update()#updates display
    
pygame.time.set_timer(USEREVENT+1, 10)# seconds for to be generated
pygame.time.set_timer(USEREVENT+2, 3500)# distance between indavidual blocks

speed1 = 3
speed = 35 # speed of game
run = True
font = pygame.font.SysFont("comicsans", 30, True)

knight1 = knight(30,160,64,64)
blockx = blocks(400,380,220,35)
spikex = spike(300,380,44,23)
grassb = grassblock(400,380,180,39)
starterbloc = starterblock(30,220,140,16)
objects = []




while run:
    
    if Dead > 0: # If we have fallen we will increment pause
        Dead += 1
    if Dead > speed * 2:  # once the pause variable hits a certain number we will call the endScreen
        endScreen()
    if pause > 0: # If we have fallen we will increment pause
        pause += 1
    if pause > speed * 2:  # once the pause variable hits a certain number we will call the endScreen
        endScreen()
    clock.tick(speed)    
    for o in objects:
        o.x -= 2
        if o.x < -math.inf :#infinite amount of blocks created
            objects.pop(objects.index(objects))#randomly generated blocks
    bg1 -= 0.5 #speed of moving bg
    bg2 -= 0.5 #speed of moving bg
    if bg1 < bg.get_width() * -1: 
        bg1 = bg.get_width()
    if bg2 < bg.get_width() * -1:
        bg2 = bg.get_width()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Allows user to exit pygame
            run = False
            pygame.quit()
        if event.type == USEREVENT+1: #increases speed of bg 
            score += 1
            speed += 0.0005
        if event.type == USEREVENT+2:
            rand = random.randrange(0,3)
            if rand == 0:
                objects.append(blocks(810,400,220,35))
                objects.append(spike(900,380,100,35))
            elif rand == 1:
                objects.append(grassblock(810,310,220,45))
            elif rand == 2:
                objects.append(blocks(810,400,220,35))

            else:
                objects.append(grassblock(810,310,220,45))
                objects.append(spike(900,400,100,35))


    if knight1.dead == False:
        control = pygame.key.get_pressed() #Computer regonizes keys is being pressed
        if control[pygame.K_RIGHT] and knight1.x < 800 - knight1.width -  knight1.speed1:#If right key is pressed player moves right
            knight1.x += knight1.speed1
            knight1.right = True
            knight1.left = False
            knight1.s = False
        elif control[pygame.K_LEFT] and knight1.x > knight1.speed1: #If right key is pressed player moves left
            knight1.x -= knight1.speed1
            knight1.left = True
            knight1.right = False
        elif control[pygame.K_p]:
            pause = True
        else:
            knight1.wc = 0
    if knight1.dead == True:
         Dead = True
    if not(knight1.jump): #If right key is pressed player jump
        if control[pygame.K_UP]:
            jumping.play()
            knight1.jump = True
            knight1.left = False
            knight1.Right = False
    else:#Physics for Jumping
        if knight1.jumpheight >= -8: 
            jumplevel = 1
            if knight1.jumpheight < 0 and knight1.y < 390 :
                jumplevel = -1
            knight1.y -= (knight1.jumpheight **2) /2 * jumplevel
            knight1.jumpheight -= 1
        else:
            knight1.jump = False
            knight1.jumpheight = 8
    paused()
    Deadd()
    regamewin()

    


    


pygame.quit()


