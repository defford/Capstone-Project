import pygame
import random

# Initialize Pygame
pygame.init()

# Set game settings
WIDTH, HEIGHT = 600, 800
SNAKE_SIZE = 20
FOOD_COUNT = 10

# Create game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Create game variables
snake = [[SNAKE_SIZE, SNAKE_SIZE], [SNAKE_SIZE, SNAKE_SIZE]]
direction = 'right'
food = [random.randint(0, WIDTH-SNAKE_SIZE), random.randint(0, HEIGHT-SNAKE_SIZE)]

# Game loop
running = True
clock = pygame.time.Clock()
score = 0

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    if direction == 'right':
        snake.append([snake[-1][0] + SNAKE_SIZE, snake[-1][1]])
    elif direction == 'left':
        snake.append([snake[-1][0] - SNAKE_SIZE, snake[-1][1]])
    elif direction == 'up':
        snake.append([snake[-1][0], snake[-1][1] - SNAKE_SIZE])
    elif direction == 'down':
        snake.append([snake[-1][0], snake[-1][1] + SNAKE_SIZE])

    # Remove head if it goes out of bounds
    if snake[-1][0] < 0 or snake[-1][0] >= WIDTH or snake[-1][1] < 0 or snake[-1][1] >= HEIGHT:
        snake = snake[:-1]

    # Check for collision with food
    if snake[-1] == food:
        food = [random.randint(0, WIDTH-SNAKE_SIZE), random.randint(0, HEIGHT-SNAKE_SIZE)]
        score += 1

    # Draw game elements
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 0), (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))
    for segment in snake:
        pygame.draw.rect(win, (255, 255, 0), (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.display.update()

    # Limit frame rate
    clock.tick(10)

# Quit Pygame
pygame.quit()