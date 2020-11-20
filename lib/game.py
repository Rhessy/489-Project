import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

disWidth = 600
disHeight = 400

dis = pygame.display.set_mode((disWidth, disHeight))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snakeBlock = 10
snakeSpeed = 15

fontStyle = pygame.font.SysFont("bahnschrift", 25)
scoreFont = pygame.font.SysFont("arial", 15)

def yourScore(score):
    value = scoreFont.render("Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

def ourSnake(snakeBlock, snakeList):
    for x in snakeList:
        pygame.draw.rect(dis, white, [x[0], x[1], snakeBlock, snakeBlock])

def message(msg, color):
    mesg = fontStyle.render(msg, True, color)
    dis.blit(mesg, [disWidth / 6, disHeight / 3])

def gameLoop():
    gameOver = False
    gameClose = False

    x1 = disWidth / 2
    y1 = disHeight / 2

    x1Change = 0
    y1Change = 0

    snakeList = []
    lengthOfSnake = 1

    foodx = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0
    foody = round(random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0

    while not gameOver:

        while gameClose == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", white)
            yourScore(lengthOfSnake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1Change = -snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_RIGHT:
                    x1Change = snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_UP:
                    y1Change = -snakeBlock
                    x1Change = 0
                elif event.key == pygame.K_DOWN:
                    y1Change = snakeBlock
                    x1Change = 0

        if x1 >= disWidth or x1 < 0 or y1 >= disHeight or y1 < 0:
            gameClose = True
        x1 += x1Change
        y1 += y1Change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snakeBlock, snakeBlock])
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)
        if len(snakeList) > lengthOfSnake:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True

        ourSnake(snakeBlock, snake_List)
        yourScore(lengthOfSnake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0
            foody = round(random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0
            lengthOfSnake += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()
