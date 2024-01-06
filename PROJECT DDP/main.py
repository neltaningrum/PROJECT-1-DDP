import pygame
import sys
import random

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, segment)

def draw_food(food):
    pygame.draw.rect(screen, RED, food)

def show_game_over_screen():
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over! Mau main lagi? (y/n)", True, (255, 0, 0))
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False

def main():
    clock = pygame.time.Clock()

    while True:
        # Inisialisasi permainan
        snake = [pygame.Rect(100, 100, CELL_SIZE, CELL_SIZE)]
        direction = (CELL_SIZE, 0)
        food = pygame.Rect(random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                           random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                           CELL_SIZE, CELL_SIZE)

        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                        direction = (0, -CELL_SIZE)
                    elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                        direction = (0, CELL_SIZE)
                    elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                        direction = (-CELL_SIZE, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                        direction = (CELL_SIZE, 0)

            new_head_x = snake[0].x + direction[0]
            new_head_y = snake[0].y + direction[1]
            new_head = pygame.Rect(new_head_x, new_head_y, CELL_SIZE, CELL_SIZE)
            snake.insert(0, new_head)

            if snake[0].colliderect(food):
                food.x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
                food.y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            else:
                snake.pop()

            if any(segment.colliderect(new_head) for segment in snake[1:]):
                game_over = True

            if not (0 <= new_head.x < WIDTH and 0 <= new_head.y < HEIGHT):
                game_over = True

            screen.fill(WHITE)
            draw_snake(snake)
            draw_food(food)

            pygame.display.flip()
            clock.tick(FPS)

        play_again = show_game_over_screen()
        if not play_again:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    CELL_SIZE = 20
    FPS = 10
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    main()