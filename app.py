import pygame
from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP
import random
import time

from pygame.constants import KEYDOWN, QUIT
pygame.init()

WIN_Height = 800
WIN_Width = 1000
BG_color = (150, 100, 100)
Block = 40        

class Snake:
    def __init__(self, parent_surface, length):
        self.body = pygame.image.load("resources/snake.png").convert()
        self.x = [WIN_Width//2]*length
        self.y = [WIN_Height//2]*length
        self.parent_surface = parent_surface
        self.direction = 'right'
        self.length = length


    def body_update(self):
        self.parent_surface.fill(BG_color)
        for i in range(self.length):
            self.parent_surface.blit(self.body, (self.x[i],self.y[i]))
        pygame.display.update()
        #self.screen.blit(apple, (x_apple, y_apple))
    

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'up':
                self.y[0] -= Block

        elif self.direction == 'down':
                self.y[0] += Block

        elif self.direction == 'right':
                self.x[0] += Block

        elif self.direction == 'left':
                self.x[0] -= Block
            
        self.body_update()


    def move_up(self):
        self.y[0] -= Block
        self.direction = 'up'
        self.body_update()

    def move_down(self):
        self.y[0] += Block
        self.direction = 'down'
        self.body_update()

    def move_left(self):
        self.x[0] -= Block
        self.direction = 'left'
        self.body_update()
        
    def move_right(self):
        self.x[0] += Block
        self.direction = 'right'
        self.body_update()


    
class Apple:
    def __init__(self, parent_surface):
        self.parent_surface = parent_surface
        self.image = pygame.image.load("resources/apple.png").convert()
        self.x = Block * 3 #random.randint(0, WIN_Width)
        self.y = Block * 3 #random.randint(0, WIN_Height)


    def place(self):
        self.parent_surface.blit(self.image, (self.x, self.y))
        pygame.display.update()



class Game:
    def __init__(self):    
        self.surface = pygame.display.set_mode((WIN_Width, WIN_Height))
        self.surface.fill(BG_color)
        pygame.display.set_caption("Snake with Python")
        self.snake = Snake(self.surface, 2)
        self.snake.body_update()
        self.apple = Apple(self.surface)
        self.apple.place()


    def play(self):
        running = True

        while running:
            for event in pygame.event.get():
                self.apple

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    
                    elif event.key == K_DOWN:
                        self.snake.move_down()
                    
                    elif event.key == K_RIGHT:
                        self.snake.move_right()
                
                    elif event.key == K_LEFT:
                        self.snake.move_left()
            
            self.snake.walk()
            self.apple.place()
            time.sleep(0.1)
        


game = Game()
game.play()

#time.sleep(5)

#class Snake:
    #def __init__(self, sc)