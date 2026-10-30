import pygame
import random

pygame.init()

SIZE = 700
HEIGHT = 520
GRID = 20

screen = pygame.display.set_mode((SIZE, HEIGHT))
clock = pygame.time.Clock()

snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)
new_dir = direction

button_size = 150

up_button = pygame.Rect(300, 830, button_size, button_size)
left_button = pygame.Rect(150, 980, button_size, button_size)
down_button = pygame.Rect(300, 1131, button_size, button_size)
right_button = pygame.Rect(451, 980, button_size, button_size)

def place_food():
    while True:
        pos = (
            random.randint(0, GRID - 1),
            random.randint(0, GRID - 1)
        )

        if pos not in snake:
            return pos

food = place_food()
score = 0
game_over = False
                

def draw():
    screen.fill((60, 60, 60))
    cell = SIZE // GRID

    
    for i in range(GRID + 1):
        pygame.draw.line(
            screen,
            (40, 40, 40),
            (i * cell, 0),
            (i * cell, SIZE)
        )

        pygame.draw.line(
            screen,
            (40, 40, 40),
            (0, i * cell),
            (SIZE, i * cell)
        )
                
    
    fx, fy = food

    pygame.draw.rect(
        screen,
        (255, 50, 50),
        (fx * cell + 2, fy * cell + 2, cell - 4, cell - 4)
    )

    
    for i, (sx, sy) in enumerate(snake):
        color = (0, 200, 0) if i == 0 else (0, 160, 0)

        pygame.draw.rect(
            screen,
            color,
            (sx * cell + 1, sy * cell + 1, cell - 2, cell - 2)
        )

    
    font = pygame.font.Font(None, 28)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 5))
    
    if game_over:
        big_font = pygame.font.Font(None, 48)

        go_text = big_font.render(
            "Game Over!",
            True,
            (255, 255, 0)
        )

        r = go_text.get_rect(
            center=(SIZE // 2, SIZE // 2)
        )

        screen.blit(go_text, r)
    
    button_color = (30, 20, 20)

    pygame.draw.rect(screen, button_color, up_button)
    pygame.draw.rect(screen, button_color, left_button)
    pygame.draw.rect(screen, button_color, down_button)
    pygame.draw.rect(screen, button_color, right_button)

    font = pygame.font.Font(None, 50)

    up_text = font.render("^", True, (255, 255, 255))
    left_text = font.render("<", True, (255, 255, 255, 255))
    down_text = font.render("v", True, (255, 255, 255, 255))
    right_text = font.render(">", True, (255, 255, 255, 255))

    screen.blit(
        up_text,
        up_text.get_rect(center=up_button.center)
    )

    screen.blit(
        left_text,
        left_text.get_rect(center=left_button.center)
    )

    screen.blit(
        down_text,
        down_text.get_rect(center=down_button.center)
    )

    screen.blit(
        right_text,
        right_text.get_rect(center=right_button.center)
    )

    pygame.display.flip()


running = True
move_timer = 0

while running:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
       
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            if not game_over:

                if up_button.collidepoint(event.pos):
                    want = (0, -1)

                elif down_button.collidepoint(event.pos):
                    want = (0, 1)

                elif left_button.collidepoint(event.pos):
                    want = (-1, 0)

                elif right_button.collidepoint(event.pos):
                    want = (1, 0)

                else:
                    want = direction
                
                if (
                    want[0] != -direction[0]
                    or want[1] != -direction[1]
                ):
                    new_dir = want
            
            else:
                snake = [(5, 5), (4, 5), (3, 5)]
                direction = (1, 0)
                new_dir = direction
                score = 0
                game_over = False
                move_timer = 0

                food = place_food()

    if not game_over:

        move_timer += 1

        if move_timer >= 3:

            move_timer = 0

            direction = new_dir

            head = snake[0]

            new_head = (
                (head[0] + direction[0]) % GRID,
                (head[1] + direction[1]) % GRID
            )
            
            if new_head in snake:
                game_over = True

            else:
                snake.insert(0, new_head)
                           
                if new_head == food:
                    score += 10
                    food = place_food()                    

                else:
                    snake.pop()

    draw()

    clock.tick(8)


pygame.quit()