import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Frame rate
FPS = 10
clock = pygame.time.Clock()

# Snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 10
snake_dir = 'RIGHT'

# Food settings
food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

# Score
score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (WIDTH / 10, 15)
    else:
        score_rect.midtop = (WIDTH / 2, HEIGHT / 1.25)
    screen.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 4)
    screen.fill(BLACK)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != 'DOWN':
                snake_dir = 'UP'
            elif event.key == pygame.K_DOWN and snake_dir != 'UP':
                snake_dir = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_dir != 'RIGHT':
                snake_dir = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_dir != 'LEFT':
                snake_dir = 'RIGHT'
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update snake position
    if snake_dir == 'UP':
        snake_pos[1] -= 10
    elif snake_dir == 'DOWN':
        snake_pos[1] += 10
    elif snake_dir == 'LEFT':
        snake_pos[0] -= 10
    elif snake_dir == 'RIGHT':
        snake_pos[0] += 10

    # Snake body mechanics
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    # Food spawn
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
    food_spawn = True

    # Background and snake drawing
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    show_score(1, WHITE, 'consolas', 20)
    pygame.display.update()
    clock.tick(FPS)
