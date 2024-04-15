# Model: google/gemma-1.1-7b-it
# Gemma 7B 1.1 is the latest release in the Gemma family of lightweight models built by Google, trained using a novel RLHF method.
# https://huggingface.co/chat/models/google/gemma-1.1-7b-it

import pygame
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Window settings
WIDTH = 500
HEIGHT = 500
TITLE = 'Snake Game'

# Snake settings
START_SIZE = 20
SNAKE_SPEED = 5

# Food settings
FOOD_SIZE = 20

# Game variables
snake = [(x, y) for x, y in [(WIDTH / 2, HEIGHT / 2), (WIDTH / 2, HEIGHT / 2 + 20), (WIDTH / 2, HEIGHT / 2 + 40)]
food_pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
score = 0


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        dt = clock.tick(SNAKE_SPEED)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the screen
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, (food_pos[0], food_pos[1], FOOD_SIZE, FOOD_SIZE))
        for point in snake:
            pygame.draw.circle(screen, WHITE, point, 10)

        # Update the snake
        new_head = (snake[0][0] + SNAKE_SPEED, snake[0][1])
        snake.insert(0, new_head)
        snake.pop()

        # Check for collisions
        if snake[0] == food_pos:
            food_pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
            score += 1
        else:
            for point in snake[1:]:
                if snake[0] == point:
                    running = False

        # Display the score
        pygame.draw.text(screen, 'Score: {}'.format(score), (10, 20), (WHITE), 20)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()