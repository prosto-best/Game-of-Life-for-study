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


#живые клетки черным цветом. мертвые клетки - белым


class GameOfLife():

    def __init__(self, grid_size, squere_size):       
        self.grid_size = grid_size
        self.squere_size = squere_size
        self.window = Tk()
        self.c = Canvas(self.window, width=600, height=600, bg='black')

    def run(self):
        
        for i in range(self.grid_size): #ширина

            for j in range(self.grid_size): #длина
                self.c.create_rectangle(i * self.squere_size, j * self.squere_size, i * self.squere_size + self.squere_size, j * self.squere_size + self.squere_size, fill="white")
      
        self.rand()

    def rand(self):
        #a = 0
        #b = 0
        for i in range(self.grid_size):

            for j in range(self.grid_size):
                a = random.randint(0, 40)
                b = random.randint(0, 40)
                #создает эллипсы внутри фигуры, следовательно, если хочу получить круг, то описываемой фигурой будет квадрат
                self.c.create_oval(self.squere_size*a, self.squere_size*b, self.squere_size*a + self.squere_size, self.squere_size*b + self.squere_size, fill="black", outline="white")
        
        self.window.title("Game of life")
        self.c.pack()
        self.window.mainloop()
        
    
    

game  = GameOfLife(30, 20)
game.run()

