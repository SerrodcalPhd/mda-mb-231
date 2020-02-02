import numpy as np
import plotly.graph_objects as go
from random import randint, random

iterations = 1000
rows = 34
cols = 45
n_cols_cells = 11
n_cells = (n_cols_cells * 2) * rows
p = 0.5

grid = np.zeros((rows, cols), dtype=int)

cells = {}

class Cell:

    def __init__(self, position, ir):
        self.position = position
        self.ir = ir

def generate_region(col_origin, col_limit, row_origin=0, row_limit=rows):
    for i in range(row_origin, row_limit):
        for j in range(col_origin, col_limit):
            position = (i,j)
            cells[position] = Cell(position, 0)
            grid[position] = 1

generate_region(0,11)
generate_region(34,45)

def neighborhood(position, cells, rows, cols):
    free = []
    x,y = position[0],position[1]
    if 0<=(x-1)<rows and 0<=y<cols and (not (x-1,y) in cells): #Left
        free.append((x-1,y))
    if 0<=(x+1)<rows and 0<=y<cols and (not (x+1,y) in cells): #Right
        free.append((x+1,y))
    if 0<=x<rows and 0<=(y-1)<cols and (not (x,y-1) in cells): #Down
        free.append((x,y-1))
    if 0<=x<rows and 0<=(y+1)<cols and (not (x,y+1) in cells): #Up
        free.append((x,y+1))
    if 0<=(x-1)<rows and 0<=(y-1)<cols and (not (x-1,y-1) in cells): #DownLeft
        free.append((x-1,y-1))
    if 0<=(x+1)<rows and 0<=(y-1)<cols and (not (x+1,y-1) in cells): #DownRight
        free.append((x+1,y-1))
    if 0<=(x-1)<rows and 0<=(y+1)<cols and (not (x-1,y+1) in cells): #UpLeft
        free.append((x-1,y+1))
    if 0<=(x+1)<rows and 0<=(y+1)<cols and (not (x+1,y+1) in cells): #UpRight
        free.append((x+1,y+1))
    return free

#free = neighborhood((18,34), cells, rows, cols)
#print(free)

def plot_grid(cells):
    x = []
    y = []
    ir = []
    for pos in cells:
        cell = cells[pos]
        x.append(cell.position[0])
        y.append(cell.position[1])
        ir.append(cell.ir)

    fig = go.Figure(data=go.Scattergl(
        x = y, #cols
        y = x, #rows
        mode='markers',
        marker=dict(
            color=ir,
            colorscale='Viridis',
            line_width=1,
            showscale=True
        )
    ))

    fig.show()

#plot_grid(cells)

def select_position_from_neighborhood(free):
    return free[randint(0, len(free)-1)]

for iteration in range(iterations):
    if random() < p:
        for position in cells:
            candidates_positions = neighborhood(position, cells, rows, cols)
            if candidates_positions:
                next_position = select_position_from_neighborhood(candidates_positions)
                cell = cells[position]
                del cells[position]
                cell.position = (next_position[0], next_position[1])
                cells[next_position] = cell

plot_grid(cells)
print(len(cells))
