import pygame

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rastro de círculos")

corriendo = True
reloj = pygame.time.Clock()

# Rectángulo
x, y = 400, 300
ancho, alto = 50, 50
velocidad = 5

# Lista para almacenar el rastro de posiciones
rastro = []

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Detectar teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Limitar al área de la ventana
    x = max(0, min(800 - ancho, x))
    y = max(0, min(600 - alto, y))

    # Guardar posición actual en el rastro
    rastro.append((x + ancho // 2, y + alto // 2))  # Centro del rectángulo

    # Fondo
    ventana.fill((30, 30, 30))  # Fondo oscuro

    # Dibujar rastro
    for pos in rastro:
        pygame.draw.circle(ventana, (0, 255, 0), pos, 5)

    # Dibujar rectángulo
    pygame.draw.rect(ventana, (255, 0, 0), (x, y, ancho, alto))

    pygame.display.update()
    reloj.tick(60)  # Limitar a 60 FPS

pygame.quit()