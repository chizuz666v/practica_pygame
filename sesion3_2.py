import pygame
import math

pygame.init()
ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Rectángulo Circular")

corriendo = True

# Propiedades del rectángulo
lado_x = 50
lado_y = 30

# Centro de la trayectoria circular
centro_x = 200
centro_y = 150
radio = 100

# Ángulo inicial
angulo = 0
velocidad_angular = 0.02  # Controla la velocidad de rotación

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((240, 240, 240))  # Fondo gris claro

    # Calcular posición usando trigonometría
    x = centro_x + int(radio * math.cos(angulo)) - lado_x // 2
    y = centro_y + int(radio * math.sin(angulo)) - lado_y // 2

    # Dibujar el rectángulo
    pygame.draw.rect(ventana, (255, 0, 0), (x, y, lado_x, lado_y))

    # Actualizar pantalla
    pygame.display.update()

    # Incrementar ángulo
    angulo += velocidad_angular

pygame.quit()