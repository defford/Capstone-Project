import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Define the snake and food
BLOCK_SIZE = 20
snake_body = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
food_position = (random.randint(0, WINDOW_WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                 random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
snake_direction = (0, -BLOCK_SIZE)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, BLOCK_SIZE):
                snake_direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -BLOCK_SIZE):
                snake_direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and snake_direction != (BLOCK_SIZE, 0):
                snake_direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-BLOCK_SIZE, 0):
                snake_direction = (BLOCK_SIZE, 0)

    # Move the snake
    new_head = (snake_body[-1][0] + snake_direction[0], snake_body[-1][1] + snake_direction[1])
    snake_body.append(new_head)
    if new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT:
        running = False
    if new_head in snake_body[:-1]:
        running = False
    if new_head == food_position:
        food_position = (random.randint(0, WINDOW_WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                         random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake_body.pop(0)

    # Clear the game window
    game_window.fill(WHITE)

    # Draw the snake and food
    for segment in snake_body:
        pygame.draw.rect(game_window, BLACK, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(game_window, RED, (food_position[0], food_position[1], BLOCK_SIZE, BLOCK_SIZE))

    # Update the display
    pygame.display.flip()
    clock.tick(10)

# Quit Pygame
pygame.quit()