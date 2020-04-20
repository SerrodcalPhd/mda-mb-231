import pygame
import numpy as np
import time
from random import randint, random

iterations = 100
migration = 0.25 # Depending on IR
mitosis = 0.1 # Depending on IR
f = 0.2

# Pygame: esquina superior izquierda el origen, tupla (columna, fila)
pygame.init()
width, height = 1000, 1000
screen = pygame.display.set_mode((height,width))

bg = 25, 25, 25
# Pintamos el fondo con el color elegido
screen.fill(bg)

# Numero de celdas (filas, columnas)
rows, cols = 34, 45
# Dimensiones de la celda
dimCW = width / cols  # Ancho -> columnas
dimCH = height / rows # Alto -> filas

# Estado de las celdas: Viva = 1; Muerta = 0
gameState = np.zeros((rows, cols)) # (filas, columnas)

# Rellenamos ambos margenes
for y in range(0, rows):
    for x in range(0, 11):
        gameState[y, x] = 1

for y in range(0, rows):
    for x in range(34, 45):
        gameState[y, x] = 1
#gameState[15,15] = 1

def neighborhood(position, grid, rows, cols):
    free = []
    x,y = position[0],position[1]
    if 0<=(x-1)<rows and 0<=y<cols and grid[x-1,y] == 0: #Left
        free.append((x-1,y))
    if 0<=(x+1)<rows and 0<=y<cols and grid[x+1,y] == 0: #Right
        free.append((x+1,y))
    if 0<=x<rows and 0<=(y-1)<cols and grid[x,y-1] == 0: #Down
        free.append((x,y-1))
    if 0<=x<rows and 0<=(y+1)<cols and grid[x,y+1] == 0: #Up
        free.append((x,y+1))
    if 0<=(x-1)<rows and 0<=(y-1)<cols and grid[x-1,y-1] == 0: #DownLeft
        free.append((x-1,y-1))
    if 0<=(x+1)<rows and 0<=(y-1)<cols and grid[x+1,y-1] == 0: #DownRight
        free.append((x+1,y-1))
    if 0<=(x-1)<rows and 0<=(y+1)<cols and grid[x-1,y+1] == 0: #UpLeft
        free.append((x-1,y+1))
    if 0<=(x+1)<rows and 0<=(y+1)<cols and grid[x+1,y+1] == 0: #UpRight
        free.append((x+1,y+1))
    return free

# Control de la ejecucion del juego
pauseExect = False

# Contador de iteraciones
cont = 0

# Bucle de ejecucion
while True and cont < iterations:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(f)

    # Registramos eventos de teclado y raton
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

    # Movimientos
    for x in range(rows): # Filas
        for y in range(cols): # Columnas

            if not pauseExect:
                if gameState[x, y] == 1:
                    neigh = neighborhood((x, y), newGameState, rows, cols)
                    if neigh:
                        next = neigh[randint(0, len(neigh)-1)]
                        if random() < migration: # Migracion
                            newGameState[x, y] = 0
                            newGameState[next] = 1
                        elif random() < mitosis: # Division celular
                            newGameState[next] = 1

    # Pintado
    for x in range(rows): # Filas
        for y in range(cols): # Columnas

            # Creamos el poligono de cada celda (columna, fila)
            poly = [((y)   * dimCW, (x)   * dimCH),
                    ((y+1) * dimCW, (x)   * dimCH),
                    ((y+1) * dimCW, (x+1) * dimCH),
                    ((y)   * dimCW, (x+1) * dimCH)]

            thickness = [((y+0.1) * dimCW, (x+0.1) * dimCH),
                         ((y+0.9) * dimCW, (x+0.1) * dimCH),
                         ((y+0.9) * dimCW, (x+0.9) * dimCH),
                         ((y+0.1) * dimCW, (x+0.9) * dimCH)]

            # Y dibujamos la celda para cada par de x e y
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                #pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
                pygame.draw.polygon(screen, (255, 255, 255), thickness, 0)

    # Actualizamos el estado del juego
    gameState = np.copy(newGameState)

    # Actualizamos la pantalla
    pygame.display.flip()

    # Actualizamos contador
    cont += 1

print("END")
time.sleep(9999)
