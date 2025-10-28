import pygame
pygame.init()
ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mi primera ventana")
corriendo = True
while corriendo:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((135, 206, 250))  # Color azul cielo (R, G, B)
    pygame.display.update()
pygame.quit()