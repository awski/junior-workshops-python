import pygame
import time
import random

pygame.init()

backgroundColor = (117, 126, 87)

fps = 15

screen_width = 800
screen_height = 600

player_size = 10

gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('pygame-workshops')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

def messageToScreen(msg, color):
    text  = font.render(msg, True, color)
    gameDisplay.blit(text, [screen_width/2,screen_height/2])

def snake(player_size, player_elements):
    for element in player_elements:
        pygame.draw.rect(gameDisplay, (0,0,0), [element[0],element[1],player_size,player_size])

def gameLoop():
    gameExit = False
    gameOver = False
    player_x = screen_width/2
    player_y = screen_height/2
    player_x_step = 0
    player_y_step = 0
    player_elements = []
    player_lenght = 1

    apple_x = round(random.randrange(0, screen_width - player_size)/10.0)*10.0
    apple_y = round(random.randrange(0, screen_height - player_size)/10.0)*10.0
    print apple_x," ",apple_y
    print player_x," ",player_y
    print  screen_height/2  + player_size/2

    while not gameExit:
        while gameOver:
            messageToScreen("Przegrales, wcisnij x aby zagrac ponownie, q aby wyjsc", (255,0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_x:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player_x_step == 0:
                    player_x_step = -player_size
                    player_y_step = 0
                elif event.key == pygame.K_RIGHT and player_x_step == 0:
                    player_x_step = player_size
                    player_y_step = 0
                elif event.key == pygame.K_UP and player_y_step == 0:
                    player_y_step = -player_size
                    player_x_step = 0
                elif event.key == pygame.K_DOWN and player_y_step == 0:
                    player_y_step = player_size
                    player_x_step = 0

        '''
        if player_x >= screen_width or player_x < 0 or player_y >= screen_height or player_y < 0:
            gameOver = True
        '''
        if player_x>= screen_width:
            player_x = 0
        if player_x == apple_x and player_y == apple_y:
            apple_x = round(random.randrange(0, screen_width - player_size)/10.0)*10.0
            apple_y = round(random.randrange(0, screen_height - player_size)/10.0)*10.0
            player_lenght += 1

        player_x += player_x_step
        player_y += player_y_step

        gameDisplay.fill(backgroundColor)

        pygame.draw.rect(gameDisplay, (255,0,0), [apple_x, apple_y, player_size, player_size])

        player_head = []
        player_head.append(player_x)
        player_head.append(player_y)
        player_elements.append(player_head)

        if len(player_elements) > player_lenght:
            del player_elements[0]

        for segment in player_elements[:-1]:
            if segment == player_head:
                gameOver = True

        snake(player_size, player_elements)
        #pygame.draw.rect(gameDisplay, (255,0,0), [400,300,32,32])
        #gameDisplay.fill((0,0,255), rect=[0,0,40,50])

        pygame.display.update()
        clock.tick(fps)

    messageToScreen("Byebye", (255,0,0))
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    quit()

gameLoop()
