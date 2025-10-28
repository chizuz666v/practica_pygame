import pygame

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Casa PYGAME")

corriendo = True

# Color inicial de la casa
color_casa = (255, 0, 0)  # Rojo

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                color_casa = (255, 0, 0)  # Cambia a rojo
            if evento.key == pygame.K_b:
                color_casa = (0, 0, 255)  # Cambia a azul

    ventana.fill((200, 200, 200))  # Fondo gris clarito

    # DIBUJAR CASA

    # Cuadrado principal
    pygame.draw.rect(ventana, color_casa, (300, 300, 200, 200))

    # Techo (triángulo)
    pygame.draw.polygon(
        ventana,
        color_casa,
        [(280, 300), (520, 300), (400, 180)]
    )

    # Ventana circular
    pygame.draw.circle(ventana, (255, 255, 255), (400, 380), 30)
    pygame.draw.circle(ventana, (0, 0, 0), (400, 380), 30, 3)  # Contorno visible

    pygame.display.update()

pygame.quit()