import pygame
from pygame.locals import *
from contents import *

pygame.init()
window = pygame.display.set_mode((600, 600)) # tela
pygame.display.set_caption(' Snake Game by Mar') # título da janela

# DIREÇÕES
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

my_direction = LEFT # DIREÇÃO INICIAL QUE A COBRA VAI SE MEXER

clock = pygame.time.Clock() # LIMITANDO O FPS DA COBRA (VELOCIDADE)

while True:
    pygame.display.update()
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() # SAIR

# LIDAR COM EVENTO DE MOVER AS TECLAS
    if event.type == KEYDOWN:
        if event.key == K_UP:
            my_direction = UP
        if event.key == K_RIGHT:
            my_direction = RIGHT
        if event.key == K_DOWN:
            my_direction = DOWN
        if event.key == K_LEFT:
            my_direction = LEFT

    if eat(snake[0], apple_pos):
        apple_pos = aligned_random()
        snake.append((0, 0))

# MEXENDO A CABEÇA DA COBRA
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10) # x e y
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
# MEXENDO O RESTO DO CORPO DA COBRA
    for i in range(len(snake) - 1, 0, -1): # laço para decremento
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    window.fill((0, 0, 0))
    window.blit(apple, apple_pos)

    for pos in snake:
        window.blit(snake_skin, pos)
    
    for pos in range(0, len(snake)):
        if snake[pos] == snake_pos[pos]
