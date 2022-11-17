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
bulletImg = pygame.transform.scale(pygame.image.load(os.path.join("Bullet","bullet.png")),(10,10))

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

#enemy animations
left_enemy = [pygame.image.load(os.path.join("Enemy", "L1E.png")),
        pygame.image.load(os.path.join("Enemy", "L2E.png")),
        pygame.image.load(os.path.join("Enemy", "L3E.png")),
        pygame.image.load(os.path.join("Enemy", "L4E.png")),
        pygame.image.load(os.path.join("Enemy", "L5E.png")),
        pygame.image.load(os.path.join("Enemy", "L6E.png")),
        pygame.image.load(os.path.join("Enemy", "L7E.png")),
        pygame.image.load(os.path.join("Enemy", "L8E.png")),
        pygame.image.load(os.path.join("Enemy", "L9P.png")),
        pygame.image.load(os.path.join("Enemy", "L10P.png")),
        pygame.image.load(os.path.join("Enemy", "L11P.png"))
        ]
right_enemy = [pygame.image.load(os.path.join("Enemy", "R1E.png")),
        pygame.image.load(os.path.join("Enemy", "R2E.png")),
        pygame.image.load(os.path.join("Enemy", "R3E.png")),
        pygame.image.load(os.path.join("Enemy", "R4E.png")),
        pygame.image.load(os.path.join("Enemy", "R5E.png")),
        pygame.image.load(os.path.join("Enemy", "R6E.png")),
        pygame.image.load(os.path.join("Enemy", "R7E.png")),
        pygame.image.load(os.path.join("Enemy", "R8E.png")),
        pygame.image.load(os.path.join("Enemy", "R9P.png")),
        pygame.image.load(os.path.join("Enemy", "R10P.png")),
        pygame.image.load(os.path.join("Enemy", "R11P.png"))
        ]


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
            pygame.draw.rect(win, (0, 255, 0), (140,0, self.health, 10))
            
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
        #Bullets
        self.bullets = []
        self.cool_down_count = 0
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
    
    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1
    def cooldown(self):
        if self.cool_down_count >= 20:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        self.hit()
        self.cooldown()
        if (userInput[pygame.K_z] and self.cool_down_count == 0):
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)
    
    
    def hit(self):
        for enemy in enemies:
            for bullet in self.bullets:
                if enemy.hitbox[0] < bullet.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < bullet.y < \
                        enemy.hitbox[1] + enemy.hitbox[3]:
                    enemy.health -= 5
                    player.bullets.remove(bullet)


#Bullet Class 
class Bullet:
    def __init__(self, x, y, direction):
        self.x = x + 15
        self.y = y + 25
        self.direction = direction

    def draw_bullet(self):
        win.blit(bulletImg,(self.x,self.y))

    def move(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15

    def off_screen(self):
        return not (self.x >=0 and self.x <= win_width)
#Enemy Class 
class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.stepIndex = 0
        #Enemy Health
        self.hitbox = (self.x, self.y, 64, 64)
        self.health = 30

    def step(self):
        if self.stepIndex >= 33:
            self.stepindex = 0

    def draw(self, win):
        self.hitbox = (self.x + 20, self.y + 10, 30, 45)
        pygame.draw.rect(win, (255, 0, 0), (self.x + 15, self.y, 30, 10))
        if self.health >= 0:
            pygame.draw.rect(win, (0, 255, 0), (self.x + 15, self.y, self.health, 10))
        self.step()
        win.blit(left_enemy[self.stepIndex // 10], (self.x, self.y))
        self.stepIndex += 1       
   
   
    def move(self):
        self.hit()
        self.x -= speed    
    def hit(self):
        if player.hitbox[0] < enemy.x + 32 < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < enemy.y + 32 < \
            player.hitbox[1] + player.hitbox[3]:
            if player.health > 0:
                player.health -= 1
                if player.health == 0 and player.lives > 0:
                    player.lives -= 1
                    player.health = 30
                elif player.health == 0 and player.lives == 0:
                    player.alive = False
    def off_screen(self):
        return not (self.x >= -50 and self.x <= win_width +50) 


    
#Game function
def draw_game():
    win.fill((0, 0, 0))
    win.blit(bg,(0,0))
    #Draw Player and Tower
    player.draw(win)
    towerGame.draw(win)
    #Draw Bullets
    for bullet in player.bullets:
        bullet.draw_bullet()
    #Draw Enemies
    for enemy in enemies:
        enemy.draw(win)
    #Gamer over argument
    if player.alive == False:
        textRect = text.get_rect()
        textRect.center = (win_width // 2, win_height //2)
    
    font = pygame.font.Font('freesansbold.ttf', 15)
    text1 = font.render('Tower Health: ' + str(towerGame.health), True,(255,255,255))
    win.blit(text1, [0,0])
    
    
    pygame.time.delay(30)
    pygame.display.update()

#Player and Tower Instance
player = Player(60, 415)
towerGame = Tower(15, 370)

#Enemies 
enemies = []
speed = 3
kills = 0

run = True
#Loop that runs the game and updates display
while run:

    #Quit game
    for event in pygame.event.get():...
    #input
    userInput = pygame.key.get_pressed()
    
    
    if event.type == pygame.QUIT:
        run = False 
    #shoot
    player.shoot()
    #movement
    player.move_player(userInput)
    player.playerJump(userInput)
    
    
    #enemies 
    if len(enemies) == 0:
        enemy = Enemy(450,400, speed)
        enemies.append(enemy)
        if speed <= 10:
            speed += 1
    for enemy in enemies:
        enemy.move()
        if enemy.off_screen() or enemy.health == 0:
            enemies.remove(enemy)
        if enemy.x < 50:
            enemies.remove(enemy)
        if enemy.health == 0:
            kills +=1


    draw_game()
    
    


