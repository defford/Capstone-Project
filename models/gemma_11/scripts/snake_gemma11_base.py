import pygame
import random

# Initialize the game engine
pygame.init()

# Define game settings
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
FOOD_SIZE = 20

# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create the snake object
snake = pygame.Rect(WIDTH // 2, HEIGHT // 2, SNAKE_SIZE, SNAKE_SIZE)

# Create the food object
food = pygame.Rect(random.randint(0, WIDTH - FOOD_SIZE), random.randint(0, HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE)

# Define the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the snake position
    snake.x += 2 if event.key == pygame.K_RIGHT else -2
    snake.y += 2 if event.key == pygame.K_UP else -2

    # Check for collision with food
    if snake.colliderect(food):
        food = pygame.Rect(random.randint(0, WIDTH - FOOD_SIZE), random.randint(0, HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE)

    # Check for collision with the screen boundaries
    if snake.left < 0 or snake.right > WIDTH:
        running = False
    if snake.top < 0 or snake.bottom > HEIGHT:
        running = False

    # Draw the game screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 0), snake)
    pygame.draw.rect(screen, (255, 0, 0), food)
    pygame.display.update()

# Quit the game engine
pygame.quit()