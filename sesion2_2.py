import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Círculos Concéntricos")

corriendo = True

# Centro de los círculos
centro = (300, 300)

# Colores para que se vean bien (puedes cambiarlos)
colores = [
    (255, 0, 0),      # Rojo
    (0, 255, 0),      # Verde
    (0, 0, 255),      # Azul
    (255, 255, 0),    # Amarillo
    (255, 0, 255)     # Magenta
]

# Radios pedidos
radios = [20, 40, 60, 80, 100]

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))  # Fondo blanco para mejor contraste

    # Dibujar círculos
    for i in range(len(radios)):
        pygame.draw.circle(ventana, colores[i], centro, radios[i], 3)

    pygame.display.update()

pygame.quit()