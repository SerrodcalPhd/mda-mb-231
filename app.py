import numpy as np
import plotly.graph_objects as go
from random import randint, random
from plotly.subplots import make_subplots

iterations = 200
rows = 34
cols = 45
n_cols_cells = 11
n_cells = (n_cols_cells * 2) * rows
p = 0.25
sampling = 10

grid = np.zeros((rows, cols), dtype=int)

cells = {}

column_evolution = {i:[] for i in range(cols)}

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

def plot_histogram(grid):
    # Axis = 0 to sum across the rows, so we'll get the sum per cols
    sum = np.sum(grid, axis = 0)
    fig = go.Figure([go.Bar(x=np.arange(45), y=sum)])
    fig.show()

def plot_column_evolution(all_data):
    titles = [f"Col {index}" for index in range(cols)]
    x = [index for index in range(0, iteration+1, sampling)] # Plus one to generate end limit
    fig = make_subplots(rows=15, cols=3, subplot_titles=titles)
    fig.add_trace(go.Scatter(x=x, y=all_data[0]), row=1, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[1]), row=1, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[2]), row=1, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[3]), row=2, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[4]), row=2, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[5]), row=2, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[6]), row=3, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[7]), row=3, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[8]), row=3, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[9]), row=4, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[10]), row=4, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[11]), row=4, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[12]), row=5, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[13]), row=5, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[14]), row=5, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[15]), row=6, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[16]), row=6, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[17]), row=6, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[18]), row=7, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[19]), row=7, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[20]), row=7, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[21]), row=8, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[22]), row=8, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[23]), row=8, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[24]), row=9, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[25]), row=9, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[26]), row=9, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[27]), row=10, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[28]), row=10, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[29]), row=10, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[30]), row=11, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[31]), row=11, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[32]), row=11, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[33]), row=12, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[34]), row=12, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[35]), row=12, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[36]), row=13, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[37]), row=13, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[38]), row=13, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[39]), row=14, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[40]), row=14, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[41]), row=14, col=3)
    fig.add_trace(go.Scatter(x=x, y=all_data[42]), row=15, col=1)
    fig.add_trace(go.Scatter(x=x, y=all_data[43]), row=15, col=2)
    fig.add_trace(go.Scatter(x=x, y=all_data[44]), row=15, col=3)
    fig.show()

def select_position_from_neighborhood(free):
    return free[randint(0, len(free)-1)]

for iteration in range(iterations):
    for position in cells:
        if random() < p:
            candidates_positions = neighborhood(position, cells, rows, cols)
            if candidates_positions:
                next_position = select_position_from_neighborhood(candidates_positions)
                cell = cells[position]
                del cells[position]
                grid[position] = 0
                cell.position = (next_position[0], next_position[1])
                cells[next_position] = cell
                grid[next_position] = 1
    if iteration % sampling == 0:
        sum = np.sum(grid, axis = 0)
        for i in range(cols):
            data = column_evolution[i]
            del column_evolution[i]
            data.append(sum[i])
            column_evolution[i] = data

plot_grid(cells)
#print(len(cells))
plot_histogram(grid)
plot_column_evolution(column_evolution)
