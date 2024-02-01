import pygame
import sys
import random

class Paddle:
    def __init__(self, screen, color, width, height):
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.x = (self.screen.get_width() - self.width) // 2
        self.y = self.screen.get_height() - 50
        self.speed = 5

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x > self.screen.get_width() - self.width:
            self.x = self.screen.get_width() - self.width

class Ball:
    def __init__(self, screen, color, size, paddle):
        self.screen = screen
        self.color = color
        self.size = size
        self.paddle = paddle
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.screen.get_width() - self.size)
        self.y = 50
        self.speed_x = random.choice([-5, 5])
        self.speed_y = 5

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x <= 0 or self.x >= self.screen.get_width():
            self.speed_x = -self.speed_x

        # Bounce off ceiling
        if self.y <= 0:
            self.speed_y = -self.speed_y

        # Bounce off paddle
        if (
            self.y + self.size >= self.paddle.y
            and self.x >= self.paddle.x
            and self.x <= self.paddle.x + self.paddle.width
        ):
            self.speed_y = -self.speed_y

        # Reset if ball goes below the screen
        if self.y > self.screen.get_height():
            self.reset()

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Set up colors
black = (0, 0, 0)

# Create a paddle and a ball object
paddle = Paddle(screen, (0, 128, 255), 100, 20)
ball = Ball(screen, (255, 0, 0), 15, paddle)

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update paddle position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left()
    if keys[pygame.K_RIGHT]:
        paddle.move_right()

    # Update ball position
    ball.move()

    # Draw everything
    screen.fill(black)
    paddle.draw()
    ball.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
