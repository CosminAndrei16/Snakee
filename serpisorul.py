import pygame
import time
import random

# Inițializare pygame
pygame.init()

# Setări ecran
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Culori
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Setări snake
block_size = 10
speed = 15

clock = pygame.time.Clock()
font = pygame.font.SysFont("bahnschrift", 25)

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(win, green, [block[0], block[1], block_size, block_size])

def game_loop():
    game_over = False
    game_close = False

    x, y = width // 2, height // 2
    x_change, y_change = 0, 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:
        while game_close:
            win.fill(black)
            msg = font.render("Game Over! Press C to Play Again or Q to Quit", True, red)
            win.blit(msg, [width / 6, height / 3])
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        win.fill(black)
        pygame.draw.rect(win, red, [food_x, food_y, block_size, block_size])
        
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        
        draw_snake(block_size, snake_list)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(speed)
    
    pygame.quit()
    quit()

# Pornire joc
game_loop()
