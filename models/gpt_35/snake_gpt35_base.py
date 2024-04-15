import pygame
import time
import random

pygame.init()

# Set display dimensions
display_width = 1200
display_height = 600

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set snake and apple size
block_size = 20

# Set game speed
speed = 45

# Set font for displaying messages
font_style = pygame.font.SysFont(None, 50)

# Set display surface
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock for controlling game speed
clock = pygame.time.Clock()

# Function to display messages
def message(msg, color):
    rendered_msg = font_style.render(msg, True, color)
    game_display.blit(rendered_msg, [display_width / 16, display_height / 3])

# Function to draw the snake
def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], block_size, block_size])

# Function to display the score
def score(score):
    text = font_style.render("Score: " + str(score), True, black)
    game_display.blit(text, [0, 0])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initialize snake position and movement
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Initial position of the apple
    apple_x = round(random.randrange(0, display_width - block_size) / float(block_size)) * block_size
    apple_y = round(random.randrange(0, display_height - block_size) / float(block_size)) * block_size

    while not game_over:

        while game_close:
            game_display.fill(white)
            message("You Lost! Press C to Play Again or Q to Quit", red)
            score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [apple_x, apple_y, block_size, block_size])
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(block_size, snake_list)
        score(snake_length - 1)
        pygame.display.update()

        if lead_x == apple_x and lead_y == apple_y:
            apple_x = round(random.randrange(0, display_width - block_size) / float(block_size)) * block_size
            apple_y = round(random.randrange(0, display_height - block_size) / float(block_size)) * block_size
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

game_loop()
