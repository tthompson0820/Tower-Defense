from operator import truediv
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Tower Defense")

x = 250
y = 250
# Coordinates for drawn circle.
radius = 15
#radius of drawn circle
vel_x = 10
vel_y = 10
jump = False 

run =True
#Loop that runs the game and updates display
while run:
    win.fill((0,0,0))


    pygame.draw.circle(win, (255,255,255), (int(x), int(y)), radius)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    userInput = pygame.key.get_pressed()
    #Movement
    if userInput[pygame.K_LEFT] and x > 0:
        x -= vel_x
    if userInput [pygame.K_RIGHT]and x < 500: 
        x += vel_x

    if jump is False and userInput[pygame.K_SPACE]:
        jump = True

    if jump is True:
        y -= vel_y*4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    pygame.time.delay(10)
    pygame.display.update()


