from operator import truediv
import pygame
import os

pygame.init()

win_width = 500
win_height = 500

win = pygame.display.set_mode((win_width,win_height))
bg_image = pygame.image.load("bg.png")
pygame.display.set_caption("Tower Defense")
bg = pygame.transform.scale(bg_image, (500,500))


#standing image for no movement
stationary = pygame.image.load(os.path.join("Hero","standing.png"))
tower= pygame.image.load(os.path.join("Tower","Tower.png"))
bullet = pygame.transform.scale(pygame.image.load(os.path.join("Bullet","bullet.png")),(10,10))

left = [pygame.image.load(os.path.join("Hero","L1.png")),
pygame.image.load(os.path.join("Hero","L2.png")),
pygame.image.load(os.path.join("Hero","L3.png")),
pygame.image.load(os.path.join("Hero","L4.png")),
pygame.image.load(os.path.join("Hero","L5.png")),
pygame.image.load(os.path.join("Hero","L6.png")),
pygame.image.load(os.path.join("Hero","L7.png")),
pygame.image.load(os.path.join("Hero","L8.png")),
pygame.image.load(os.path.join("Hero","L9.png")),]

#Right Facing
right = [pygame.image.load(os.path.join("Hero","R1.png")),
pygame.image.load(os.path.join("Hero","R2.png")),
pygame.image.load(os.path.join("Hero","R3.png")),
pygame.image.load(os.path.join("Hero","R4.png")),
pygame.image.load(os.path.join("Hero","R5.png")),
pygame.image.load(os.path.join("Hero","R6.png")),
pygame.image.load(os.path.join("Hero","R7.png")),
pygame.image.load(os.path.join("Hero","R8.png")),
pygame.image.load(os.path.join("Hero","R9.png")),]    
#variables for specif


#Tower Class
class Tower:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        #Tower Health
        self.hitbox = (self.x, self.y, 64, 64)
        self.health = 200
        self.lives = 1
        self.alive = True 
        self.stationary = True
    def draw(self, win):
        self.hitbox = (self.x + 15, self.y + 15,  30, 40)
        if self.stationary:
            win.blit(tower, (self.x, self.y))
        if self.health >= 0:
            pygame.draw.rect(win, (0, 255, 0), (125,0, self.health, 10))
            
#Player Class
class Player:
    def __init__(self,x,y):
     #walk
        self.x = x
        self.y = y
        self.velx = 10
        self.vely = 6
        self.face_right = True
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        #Jump 
        self.jump = False
        #health
        self.hitbox = (self.x, self.y, 64, 64)
        self.health = 30
        self.lives = 1
        self.alive = True 




    def move_player(self, userInput):
        if userInput[pygame.K_RIGHT]:
            self.x += self.velx
            self.face_right = True
            self.face_left = False 
        elif userInput[pygame.K_LEFT]:
            self.x -= self.velx
            self.face_right = False
            self.face_left = True 
        else:
            self.stepIndex = 0
            self.face_left = False
            self.face_right = False
            


    def draw(self, win):
        self.hitbox = (self.x + 15, self.y + 15,  30, 40)
        pygame.draw.rect(win, (255, 0, 0), (self.x + 15, self.y, 30, 10))
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.health >= 0:
            pygame.draw.rect(win, (0, 255, 0), (self.x + 15, self.y, self.health, 10))
        if self.face_left:
            win.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex +=1
        elif self.face_right:
            win.blit(right[self.stepIndex],(self.x,self.y))
            self.stepIndex += 1
        else:
            win.blit(stationary,(self.x,self.y))
    
    
    def playerJump (self, userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vely*4
            self.vely -=1
        if self.vely < -6:
            self.jump = False 
            self.vely = 6


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x 
        self.y = y 
        self.direction = direction

    def draw_bullet(self):
        win.blit(bullet,(self.x,self.y))

    def move(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15

    def off_screen(self):
        return not (self.x >=0 and self.x <= win_width)
    

#Game function
def draw_game():
    win.fill((0, 0, 0))
    win.blit(bg,(0,0))
    player.draw(win)
    towerGame.draw(win)
    pygame.time.delay(30)
    pygame.display.update()
    font = pygame.font.Font('freesansbold.ttf', 32)
    text1 = font.render('Tower Health:' + str(towerGame.health), True,(0,0,0))
    win.blit(text1, (150,20))
player = Player(60, 415)
towerGame = Tower(15, 370)

run = True
#Loop that runs the game and updates display
while run:

    #Quit game
    for event in pygame.event.get():...
    #input
    userInput = pygame.key.get_pressed()
    
    
    if event.type == pygame.QUIT:
        run = False 

    #movement
    player.move_player(userInput)
    player.playerJump(userInput)



    draw_game()
    
    


