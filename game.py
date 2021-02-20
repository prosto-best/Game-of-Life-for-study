from tkinter import *
import random

#GRID_SIZE =40 #Ширина и высота игрового поля
#SQUARE_SIZE = 20 #Размер одной клетки на поле


#window = Tk()
#window.title("Game of life")
#c = Canvas(window, width=800, height=800, bg='black')
#Первые два параметра координаты левого верхнего угла прямоугольника.
#Вторые два параметра координаты правого нижнего угла прямоугольника.
#c.pack()


#for i in range(GRID_SIZE): #ширина
    
#    for j in range(GRID_SIZE): #длина
#        c.create_rectangle(i * SQUARE_SIZE, j * SQUARE_SIZE, i * SQUARE_SIZE + SQUARE_SIZE, j * SQUARE_SIZE + SQUARE_SIZE, fill="white")

#def create_cells():



#window.mainloop()


class GameOfLife():
    grid_size = 40
    squere_size = 20
    window = Tk()
    c = Canvas(window, width=800, height=800, bg='black')
    
    
    
    def __init__(self, grid_size, squere_size):
        self.grid_size = grid_size
        self.squere_size = squere_size

    def run_game(self):
        for i in range(self.grid_size): #ширина

            for j in range(self.grid_size): #длина
                c.create_rectangle(i * self.grid_size, j * self.grid_size, i * self.grid_size + self.grid_size, j * self.grid_size + self.grid_size, fill="white")

        
        
    window.title("Game of life")
    c.pack()
    window.mainloop()


