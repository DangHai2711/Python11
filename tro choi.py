import pygame
from random import randrange


def eat(c1, c2):
    return c1[0] == c2[0] and c1[1] == c2[1]


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
SCREEN = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Jogo da Cobrinha')
icon = pygame.image.load('dragon.jpg')
pygame.display.set_icon(icon)

snake = [(230, 250), (240, 250), (250, 250)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))
current_direction = RIGHT

apple_position = (randrange(0, 500, 10), randrange(0, 500, 10))
apple_skin = pygame.image.load('dragon.jpg').convert_alpha()

score = 0

clock = pygame.time.Clock()
game_over = False

while not game_over:
    clock.tick(10)
    SCREEN.fill((0, 0, 0))

    for x in range(0, 500, 10):
        pygame.draw.line(SCREEN, (40, 40, 40), (x, 0), (x, 600))

    for y in range(0, 500, 10):
        pygame.draw.line(SCREEN, (40, 40, 40), (0, y), (600, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and current_direction != DOWN:
                current_direction = UP
            if event.key == pygame.K_RIGHT and current_direction != LEFT:
                current_direction = RIGHT
            if event.key == pygame.K_DOWN and current_direction != UP:
                current_direction = DOWN
            if event.key == pygame.K_LEFT and current_direction != RIGHT:
                current_direction = LEFT

        if current_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if current_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if current_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if current_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

        if eat(snake[0], apple_position):
            apple_position = (randrange(0, 500, 10), randrange(0, 500, 10))
            snake.append((0, 0))
            score += 10

        if snake[0][0] == 500 or snake[0][1] == 500 or snake[0][0] < 0 or snake[0][1] < 0:
            game_over = True

    SCREEN.blit(apple_skin, apple_position)

    for position in snake:
        SCREEN.blit(snake_skin, position)

    pygame.display.update()