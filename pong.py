import pygame

#setting the color
background_colour = (0,0,0)

screen = pygame.display.set_mode((980,800))

pygame.display.set_caption("Pong Game")

screen.fill(background_colour)

#Updates the Screen
pygame.display.flip()


#Class for Objects in Pong

class Paddle:
    def __init__():
        pass
    def draw():
        pass
    def move_left():
        pass
    def move_right():
        pass

class Ball:
    def __init__():
        pass
    def reset():
        pass
    def move():
        pass
    

running = True

while running:
    
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False