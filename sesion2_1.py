import pygame

pygame.init()
ventana = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tablero de Ajedrez")

corriendo = True

# Tamaño de cada cuadrado
lado = 100

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibujar tablero de ajedrez
    for fila in range(8):
        for col in range(8):
            # Alternar colores tipo ajedrez
            if (fila + col) % 2 == 0:
                color = (255, 255, 255)  # Blanco
            else:
                color = (0, 0, 0)  # Negro
            
            # Dibujar cada casilla
            pygame.draw.rect(ventana, color, (col * lado, fila * lado, lado, lado))

    pygame.display.update()

pygame.quit()