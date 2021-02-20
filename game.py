from tkinter import *
import random

GRID_SIZE =40 #Ширина и высота игрового поля
SQUARE_SIZE = 20 #Размер одной клетки на поле

window = Tk()
window.title("Game of life")
c = Canvas(window, width=800, height=800, bg='black')
#Первые два параметра координаты левого верхнего угла прямоугольника.
#Вторые два параметра координаты правого нижнего угла прямоугольника.
#c.create_rectangle(50,60,55,65,fill="white")
c.pack()

for i in range(GRID_SIZE):
    #c.create_rectangle(i * SQUARE_SIZE, i * SQUARE_SIZE, i * SQUARE_SIZE + SQUARE_SIZE, i * SQUARE_SIZE + SQUARE_SIZE, fill="white")
    for j in range(GRID_SIZE):
        c.create_rectangle(j * SQUARE_SIZE, j * SQUARE_SIZE, j * SQUARE_SIZE + SQUARE_SIZE, j * SQUARE_SIZE + SQUARE_SIZE, fill="white")
        #c.create_rectangle(j * SQUARE_SIZE + SQUARE_SIZE, j * SQUARE_SIZE + SQUARE_SIZE, j * SQUARE_SIZE, j * SQUARE_SIZE)


window.mainloop()