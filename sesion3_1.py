import pygame
import random

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cuadrado aventurero")

corriendo = True

# Propiedades del cuadrado
x, y = 300, 300
lado = 80
velocidad_x = 3
velocidad_y = 3
color_cuadrado = (255, 0, 0)  # Color inicial (Rojo)

def nuevo_color():
    return (
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255)
    )

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Mover cuadrado
    x += velocidad_x
    y += velocidad_y

    # Revisar colisiones con los bordes y cambiar color
    if x <= 0:
        x = 0
        velocidad_x *= -1
        color_cuadrado = nuevo_color()

    if x + lado >= 800:
        x = 800 - lado
        velocidad_x *= -1
        color_cuadrado = nuevo_color()

    if y <= 0:
        y = 0
        velocidad_y *= -1
        color_cuadrado = nuevo_color()

    if y + lado >= 600:
        y = 600 - lado
        velocidad_y *= -1
        color_cuadrado = nuevo_color()

    ventana.fill((240, 240, 240))  # Fondo claro

    pygame.draw.rect(ventana, color_cuadrado, (x, y, lado, lado))

    pygame.display.update()

pygame.quit()