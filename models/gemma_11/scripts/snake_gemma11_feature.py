import pygame
import random

# Initialize the game engine
pygame.init()

# Define game settings
SNAKE_SIZE = 20
BOARD_SIZE = 20
SPEED = 200
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

# Create the game board
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Create the snake
snake = [(10, 10), (11, 10), (12, 10)]

# Create the food
food_pos = generate_food_position()

# Game loop
running = True
while running:

    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update snake position
    snake.append(snake[-1])
    snake.pop(0)

    # Handle eating food
    if snake[-1] == food_pos:
        food_pos = generate_food_position()

    # Update board
    for row, row_list in enumerate(board):
        for col, col_val in enumerate(row_list):
            if (col, row) in snake:
                board[row][col] = 1

    # Draw the game board
    screen = pygame.display.set_mode((BOARD_SIZE * SNAKE_SIZE, BOARD_SIZE * SNAKE_SIZE))
    for row, row_list in enumerate(board):
        for col, col_val in enumerate(row_list):
            if col_val == 1:
                pygame.draw.rect(screen, SNAKE_COLOR, (col * SNAKE_SIZE, row * SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE))

    # Draw the food
    pygame.draw.rect(screen, FOOD_COLOR, (food_pos[0] * SNAKE_SIZE, food_pos[1] * SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE))

    # Display the game board
    pygame.display.update()

    # Limit the frame rate
    pygame.time.delay(SPEED // 100)

# Quit the game engine
pygame.quit()