import pygame
from pygame.locals import *
import random
import time

pygame.init()

WIN_Height = 800
WIN_Width = 1200
BG_color = (150, 100, 100)
Block = 40        

class Snake:
    def __init__(self, parent_surface, length):
        self.body = pygame.image.load("resources/snake.png").convert()
        self.x = [9*Block]
        self.y = [9*Block]
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
        for i in range(self.length-1, 0, -1):
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
        self.direction = 'up'
        self.body_update()

    def move_down(self):
        self.direction = 'down'
        self.body_update()

    def move_left(self):
        self.direction = 'left'
        self.body_update()
        
    def move_right(self):
        self.direction = 'right'
        self.body_update()
    
    def increase_length(self, length):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    


    
class Apple:
    def __init__(self, parent_surface):
        self.parent_surface = parent_surface
        self.image = pygame.image.load("resources/apple.png").convert()
        self.x = Block * 14 
        self.y = Block * 9


    def place(self):
        self.parent_surface.blit(self.image, (self.x, self.y))
        pygame.display.update()
    
    def move(self):
        self.x = random.randint(0, WIN_Width//Block - 1)*Block
        self.y = random.randint(0, WIN_Height//Block -1)*Block




class Game:
    def __init__(self):    
        self.surface = pygame.display.set_mode((WIN_Width, WIN_Height))
        self.surface.fill(BG_color)
        pygame.display.set_caption("Snake with Python")
        self.snake = Snake(self.surface, 1)
        self.snake.body_update()
        self.apple = Apple(self.surface)
        self.apple.place()
        self.game_status = True

    def is_collision(self, x1, x2, y1, y2):
        if x1 >= x2 and x1 < x2 + Block:
            if y1 >= y2 and y1 < y2 + Block:
                return True
        return False

    def score(self):
        self.font = pygame.font.SysFont('calibri', 28)
        self.points = self.font.render(f"Score: {self.snake.length}", True, (200,200,200))
        self.surface.blit(self.points,(100,100))
        pygame.display.update()
                

    def run(self):

        self.apple.place()
        self.snake.walk()

        if self.is_collision(self.snake.x[0], self.apple.x, self.snake.y[0], self.apple.y):
            self.snake.increase_length(self.snake.length)
            self.apple.move()
        self.apple.place()

        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.x[i], self.snake.y[0], self.snake.y[i]):
                raise "End Game"

    def game_over_screen(self):
        self.game_status = False
        self.font_one = pygame.font.SysFont('calibri', 40)
        self.font_two = pygame.font.SysFont("calibri", 30)

        self.surface.fill(BG_color)
        self.end_score = self.font_one.render(f"Final Score: {self.snake.length}", True, (200,200,200))
        self.surface.blit(self.end_score,(400,400))
        self.end_message = self.font_two.render("Game Over. Try Again? (Press R)", True,  (200,200,200))
        self.surface.blit(self.end_message,(400,500))
        pygame.display.update()
    
    def reset(self):
        game=Game()
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)
        self.game_status = True

    def play(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_r:
                        self.reset()
                        pause = False
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                            
                        elif event.key == K_DOWN:
                            self.snake.move_down()
                            
                        elif event.key == K_RIGHT:
                            self.snake.move_right()
                        
                        elif event.key == K_LEFT:
                            self.snake.move_left()
                        elif event.key == K_r:
                            self.reset()
                            print("reset")
           
            try:
                if pause == False:
                    self.run()
            except Exception as e:
                self.game_over_screen()
                pause = True
            if self.game_status == True:       
                self.score()
            time.sleep(0.15)
        


game = Game()
game.play()


#class Snake:
    #def __init__(self, sc)


