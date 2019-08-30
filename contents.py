import pygame
from random import randint

# FUNÇÕES
def aligned_random(): # maçã alinhada com a cobrinha
    x = randint(0, 59)
    y = randint(0, 59)
    return (x * 10) , (y * 10) # múltiplos de 10

def eat(pos_snake, pos_apple): # colisão da cobra com a maçã
    return (pos_snake[0] == pos_apple[0]) and (pos_snake[1] == pos_apple[1])

def collision(snake_current, snake_new): # colisão da cobra com ela mesma
    if snake_current == snake_new:
        print('GAME OVER!')

# COBRA
snake = [(250, 250), (260, 250), (270, 250)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 230, 230))
snake_pos = 0

# MAÇÃ
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 64))
apple_pos = aligned_random() # posição da maçã na tela

# GAME OVER
pygame.font.init()
font = pygame.font.SysFont('Arial', 30)
text = font.render('GAME OVER', (255, 255, 255))