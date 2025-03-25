import pygame
from pygame.draw_py import draw_line

pygame.init()

#tela de jogo
tela_x = 800
tela_y = 600

#Define cor
cor_texto = (255,255,255)

#variaveis de jogo
game_pause = False

tela = pygame.display.set_mode((tela_x, tela_y))
pygame.display.set_caption('Menu')


font = pygame.font.SysFont("arialblack", 40)


def desenha_texto(texto, font, cor_texto, x, y):
    img = font.render(texto, True, cor_texto)
    tela.blit(img, (x,y))

#Loop de jogo
run = True
while run:
    tela.fill((52, 78, 91))
    desenha_texto("Aperte espaço para pausar", font, cor_texto, 160, 250)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_pause = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()