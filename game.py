# from random import randint
# from pprint import pprint
# import os
# import time

# world_size = 16
# populations = 256
# world = [[] for _ in range(world_size)]

# for i in range(world_size):
#     for j in range(world_size):
#         world[i].append(randint(0,1))

# new_world = world.copy()

# for _ in range(populations):
#     for x in range(world_size):
#         for y in range(world_size):
#             alives_in_area = 0
#             for i in (-1,0,1):
#                 for j in (-1,0,1):
#                     if i != 0 and j != 0:
#                         if world[(y - 1 + j + world_size) % world_size][(x - 1 + i + world_size) % world_size] == 1:
#                             alives_in_area += 1
#             if alives_in_area == 3 or alives_in_area ==2:
#                 new_world[x][y] = 1
#             else:
#                 new_world[x][y] = 0
#     time.sleep(0.25)
#     os.system('cls')
#     for i in range(world_size):
#         for j in range(world_size):
#             if new_world[i][j] == 1:
#                 print(f'\N{MEDIUM BLACK CIRCLE}', end='')
#             else:
#                 print(f'\N{MEDIUM WHITE CIRCLE}', end='')
#         print('')
#     world = new_world.copy()
import numpy as np
from tkinter import Tk, Canvas
from pprint import pprint

class World:
    width = 0
    height = 0 
    size = (width, height)
    alive_symbol = '\N{MEDIUM BLACK CIRCLE}'
    dead_symbol = '\N{MEDIUM WHITE CIRCLE}'
    states = 2
    cells = np.zeros(shape=size)
    iterations = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = np.random.randint(low=0, high=self.states, size=(self.width, self.height))

    def __repr__(self):
        cells_repr = ' ' +  str(self.cells).replace('[', '').replace(']', '')
        return cells_repr.replace('1', self.alive_symbol).replace('0', self.dead_symbol)

    def check_rule(self, x, y):
        alive_in_area = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i != 0 and j != 0:
                    if self.cells[(y - 1 + j + self.height) % self.height][(x - 1 + i + self.width) % self.width] == 1:
                        alive_in_area += 1
        return 1 if alive_in_area == 3 or alive_in_area == 2 else 0

    def evaluate(self, iteration=1):
        new_cells = np.zeros_like(self.cells)
        if iteration > 1:
            for _ in range(iteration):    
                for x in range(self.width):
                    for y in range(self.height):
                        new_cells[x][y] = self.check_rule(x, y)
                self.cells = new_cells.copy()
        del new_cells

    def get_data(self):
        """

        get_data[summary]
        Размер мира
        Текущее поколение
        Число живых клеток
        Число мертвых клеток
        """
        cells_total = self.width*self.height
        alives_total = np.count_nonzero(self.cells)
        dead_total = cells_total - alives_total
        alives_total_pere = alives_total/cells_total
        dead_total_pere = 1.0 - alives_total_pere
        data = [str(i) for i in (alives_total, dead_total, alives_total_pere, dead_total_pere, self.iterations)]
        return '\n'.join(data)

my_world = World(10, 10)
pprint(my_world)
my_world.evaluate()
pprint(my_world)
