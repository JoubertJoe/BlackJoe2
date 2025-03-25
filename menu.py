import pygame

pygame.init()

#tela de jogo
tela_x = 800
tela_y = 600

tela = pygame.display.set_mode((tela_x, tela_y))
pygame.display.set_caption('Menu')

def desenha_texto(texto, fonte, texto_col, x, y):
    img = fonte.render(texto, True, texto_col)
    tela.blit(img, (x,y))

#Loop de jogo
run = True
while run:
    tela.fill((52, 78, 91))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()