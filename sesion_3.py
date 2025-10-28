import pygame

pygame.init()
ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mi primera ventana")

# Crear fuente del texto
fuente = pygame.font.Font(None, 50)  # None usa la fuente por defecto. 50 tamaño.

corriendo = True
contador_frames = 0

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_ESCAPE]:
        corriendo = False

    ventana.fill((135, 206, 250))

    # Renderizar texto del contador
    texto = fuente.render(f"Frames: {contador_frames}", True, (0, 0, 0))  # Color negro
    ventana.blit(texto, (20, 20))  # Posición en pantalla

    pygame.display.update()

    contador_frames += 1

    if contador_frames >= 300:
        corriendo = False

pygame.quit()