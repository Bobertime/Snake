import pygame
import random
import sys

# Размеры окна в пикселях
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

CELL_SIZE = 20

# Размеры сетки в ячейках
WIDTH = int(WINDOW_WIDTH / CELL_SIZE)
HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)

# Цвета
BG_COLOR = (0, 0, 0)
GRID_COLOR = (40, 40, 40)
APPLE_COLOR = (255, 0, 0)
APPLE_OUTER_COLOR = (155, 0, 0)
SNAKE_COLOR = (0, 255, 0)
SNAKE_OUTER_COLOR = (0, 155, 0)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0

FPS = 15

r = pygame.Rect(20, 20, 20, 20)


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    global FPS_CLOCK
    global DISPLAY

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Wormy')

    while True:
        # Мы всегда будем начинать игру с начала. После проигрыша сразу
        # начинается следующая.
        run_game()


def run_game():
    apple = Cell(20, 20)
    snake = [Cell(3 * CELL_SIZE, 10 * CELL_SIZE),
             Cell(4 * CELL_SIZE, 10 * CELL_SIZE),
             Cell(5 * CELL_SIZE, 10 * CELL_SIZE)]

    direction = RIGHT
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not direction == LEFT:
                    snake[-1].x -= CELL_SIZE
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and not direction == RIGHT:
                    snake[-1].x += CELL_SIZE
                    direction = RIGHT
                elif event.key == pygame.K_UP and not direction == UP:
                    snake[-1].y -= CELL_SIZE
                    direction = UP
                elif event.key == pygame.K_DOWN and not direction == DOWN:
                    snake[-1].y += CELL_SIZE
                    direction = DOWN

        if snake_hit_edge(snake[-1]):
            return

        # TODO(8.1): если змейка задела свой хвост, завершить игру.
        #  Для проверки восппользуйтесь функцией snake_hit_self.

        if snake_hit_apple(snake[-1], apple):
            snake = snake_grow(snake)
            apple = new_apple()

        snake = move_snake(snake, direction)
        draw_frame(snake, apple)
        FPS_CLOCK.tick(FPS)


def draw_frame(snake, apple):
    DISPLAY.fill(BG_COLOR)
    draw_grid()
    draw_snake(snake)
    draw_apple(apple)
    pygame.display.update()


def draw_grid():
    for i in range(WIDTH):
        pygame.draw.line(DISPLAY, GRID_COLOR, (CELL_SIZE * i, 0), (CELL_SIZE * i, WINDOW_HEIGHT), 2)
    for g in range(HEIGHT):
        pygame.draw.line(DISPLAY, GRID_COLOR, (0, CELL_SIZE * g), (WINDOW_WIDTH, CELL_SIZE * g), 2)


def draw_apple(apple):
    draw_cell(apple, SNAKE_OUTER_COLOR, APPLE_COLOR)


def draw_snake(snake):
    for cell in snake:
        draw_cell(cell, SNAKE_OUTER_COLOR, SNAKE_COLOR)


def draw_cell(cell, outer_color, inner_color):
    pygame.draw.rect(DISPLAY, outer_color, pygame.Rect(cell.x, cell.y, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(DISPLAY, inner_color, pygame.Rect(cell.x + 2, cell.y + 2, CELL_SIZE - 4, CELL_SIZE - 4))


def move_snake(snake, direction):
    snake.pop(0)
    snake.append(Cell(snake[-1].x, snake[-1].y))
    if direction == RIGHT:
        snake[-1].x += CELL_SIZE
    elif direction == LEFT:
        snake[-1].x -= CELL_SIZE
    elif direction == UP:
        snake[-1].y -= CELL_SIZE
    elif direction == DOWN:
        snake[-1].y += CELL_SIZE
    return snake


def snake_hit_edge(snake_head):
    return snake_head.x < 0 or snake_head.y < 0 or snake_head.x > WINDOW_WIDTH \
           or snake_head.y > WINDOW_HEIGHT


def snake_hit_apple(snake_head, apple):
    return snake_head.x == apple.x and snake_head.y == apple.y


def snake_grow(snake):
    snake.append(Cell(snake[0].x, snake[0].y))
    return snake


def new_apple():
    return Cell(random.randint(0, WIDTH) * CELL_SIZE,
                random.randint(0, HEIGHT) * CELL_SIZE)


def get_direction(snake, direction):
    # TODO(7.3): функция возвращает направление движения
    #  в зависимости от нажатой клавиши:
    #  * pygame.K_LEFT
    #  * pygame.K_RIGHT
    #  * pygame.K_UP
    #  * pygame.K_DOWN
    #  Если нажата клавиша противоположного направления движения,
    #  то не менять направление.
    ...


def snake_hit_self():
    # TODO(8.2): функция возвращает True, если голова змеи
    #  пересеклась хотя бы с одним блоком хвоста.
    ...


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
