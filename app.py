import numpy as np
#import matplotlib.pyplot as plt
import plotly.graph_objects as go

rows = 34
cols = 45
n_cols_cells = 11
n_cells = (n_cols_cells * 2) * rows

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
        x = x,
        y = y,
        mode='markers',
        marker=dict(
            color=ir,
            colorscale='Viridis',
            line_width=1
        )
    ))

    fig.show()

plot_grid(cells)
