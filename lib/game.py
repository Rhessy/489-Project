import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

disWidth = 600
disHeight = 400

class Snake:
    def __init__(self):
        self.dis = pygame.display.set_mode((disWidth, disHeight))
        pygame.display.set_caption('Snake Game')

        self.clock = pygame.time.Clock()

        self.snakeBlock = 10
        self.snakeSpeed = 15

        self.fontStyle = pygame.font.SysFont("bahnschrift", 25)
        self.scoreFont = pygame.font.SysFont("arial", 15)

    def yourScore(self, score):
        value = self.scoreFont.render("Score: " + str(score), True, white)
        self.dis.blit(value, [0, 0])

    def ourSnake(self, snakeBlock, snakeList):
        for x in snakeList:
            pygame.draw.rect(self.dis, white, [x[0], x[1], snakeBlock, snakeBlock])

    def message(self, msg, color):
        mesg = self.fontStyle.render(msg, True, color)
        self.dis.blit(mesg, [disWidth / 6, disHeight / 3])

    def drawBorder(self):
        for x in range(0, 600, 10):
            pygame.draw.rect(self.dis, white, [x, 20, 10, 10])
            pygame.draw.rect(self.dis, white, [x, 390, 10, 10])

        for x in range(20, 400, 10):
            pygame.draw.rect(self.dis, white, [0, x, 10, 10])
            pygame.draw.rect(self.dis, white, [590, x, 10, 10])

    def gameLoop(self):
        gameOver = False
        gameClose = False

        x1 = disWidth / 2
        y1 = disHeight / 2

        x1Change = 0
        y1Change = 0

        snakeList = []
        lengthOfSnake = 1

        foodx = round(random.randrange(20, disWidth - self.snakeBlock - 20) / 10.0) * 10.0
        foody = round(random.randrange(40, disHeight - self.snakeBlock - 20) / 10.0) * 10.0

        while not gameOver:

            while gameClose == True:
                self.dis.fill(black)
                self.drawBorder()
                self.message("You Lost! Press C-Play Again or Q-Quit", white)
                self.yourScore(lengthOfSnake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameOver = True
                            gameClose = False
                        if event.key == pygame.K_c:
                            self.gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1Change = -self.snakeBlock
                        y1Change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1Change = self.snakeBlock
                        y1Change = 0
                    elif event.key == pygame.K_UP:
                        y1Change = -self.snakeBlock
                        x1Change = 0
                    elif event.key == pygame.K_DOWN:
                        y1Change = self.snakeBlock
                        x1Change = 0

            if x1 >= disWidth-10 or x1 < 10 or y1 >= disHeight-10 or y1 < 30:
                gameClose = True
            x1 += x1Change
            y1 += y1Change
            self.dis.fill(black)
            self.drawBorder()
            pygame.draw.rect(self.dis, green, [foodx, foody, self.snakeBlock, self.snakeBlock])
            snakeHead = []
            snakeHead.append(x1)
            snakeHead.append(y1)
            snakeList.append(snakeHead)
            if len(snakeList) > lengthOfSnake:
                del snakeList[0]

            for x in snakeList[:-1]:
                if x == snakeHead:
                    gameClose = True

            self.ourSnake(self.snakeBlock, snakeList)
            self.yourScore(lengthOfSnake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, disWidth - self.snakeBlock) / 10.0) * 10.0
                foody = round(random.randrange(0, disHeight - self.snakeBlock) / 10.0) * 10.0
                lengthOfSnake += 1

            self.clock.tick(self.snakeSpeed)

        pygame.quit()
        quit()
