from tkinter import *
import random
import numpy as np
import keyboard
#GRID_SIZE = 30 #Ширина и высота игрового поля
#SQUARE_SIZE = 20 #Размер одной клетки на поле
#живые клетки черным цветом. мертвые клетки - белым
#Я допустил кое-какую ошибку в разработке: я сначала создал рандомные кружки на поле, а потом по ним делал матрицу; можно было все сделать
#гораздо проще: сначала надо было создать матрицу с рандомными в ней единичками и ноликами и потом уже по ней создавать рисунок вывода =)


class GameOfLife():

    def __init__(self, grid_size, squere_size):       
        self.grid_size = grid_size
        self.squere_size = squere_size
        self.window = Tk()
        self.c = Canvas(self.window, width=600, height=600, bg='black')

    def run(self): #чертим сетку       
        for i in range(self.grid_size): #ширина

            for j in range(self.grid_size): #длина
                self.c.create_rectangle(i * self.squere_size, j * self.squere_size, i * self.squere_size + self.squere_size, j * self.squere_size + self.squere_size, fill="white")
        

        self.create_matrix()

    def create_matrix(self): #создаем нулевую матрицу, т.к еще не создали жителей(это в следующей функцие) с заданными значениями 
        arr = np.array([[0]*(self.grid_size)]*(self.grid_size))
        self.rand(arr)



    def rand(self, arr): #рандомно распологаем жителей в виде кружка
        for i in range(self.grid_size):

            for j in range(self.grid_size):
                a = random.randint(0, 29)
                b = random.randint(0, 29)
                #создает эллипсы внутри фигуры, следовательно, если хочу получить круг, то описываемой фигурой будет квадрат
                self.c.create_oval(self.squere_size*a, self.squere_size*b, self.squere_size*a + self.squere_size, self.squere_size*b + self.squere_size, fill="black", outline="white", tag="some-tag")
                arr[b][a] = 1


        print(arr)

        self.window.title("Game of life")
        self.c.pack()
        #self.window.mainloop()
        self.check(arr)

    ''' 
        По итогу этих 4-х функций программа создает сетку 30х30 квадратиков(каждый со стороной 20px), затем на этой сетке
        рандомно размещаются жители в виде кружочков, после этого создается матрица в виде этого же поля: единицы - живые,
        нули - мертвые.

    '''

    #В этой функции будем проверять конкретные условия, на основе которых клетка либо умирает, либо остается живой
    #Также нужно проверять: если у пустой клетке три соседа, то в ней зарождается жизнь
    #Нужно складывать цифры всех соседей(по вертикали, по горизонтали, по  двум диагоналям) с шагом в одну клетку какой 
    #то клетки в матрице и проверять их сумму,
    #если, к примеру, сумма равна 2 или 3 житель выживает и переходит в следующее поколение


    def check(self, arr):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
            #Здесь проверем матрицу не взяв во внимание углы, для отдельные условия
                if i > 0 and i < 29:
                    if j > 0 and j < 29:
                        #Условие выполняется если клетка мертва и рядом с ней, с шагом в одну клетку, три живые
                        if arr[i][j] == 0:
                            if (arr[i+1][j] + arr[i-1][j] + arr[i+1][j+1] + arr[i+1][j-1] + arr[i-1][j+1] + arr[i-1][j-1] + arr[i][j-1] + arr[i][j+1]) == 3:
                                arr[i][j] = 1

                        else:
                            if (arr[i+1][j] + arr[i-1][j] + arr[i+1][j+1] + arr[i+1][j-1] + arr[i-1][j+1] + arr[i-1][j-1] + arr[i][j-1] + arr[i][j+1]) == 2 or (arr[i+1][j] + arr[i-1][j] + arr[i+1][j+1] + arr[i+1][j-1] + arr[i-1][j+1] + arr[i-1][j-1] + arr[i][j-1] + arr[i][j+1]) == 3:
                                arr[i][j] = 1

                            else:
                                arr[i][j] = 0

                    else:
                        if arr[i][j] == 0:
                            #Левая боковая грань матрицы без самой первой и самой последеней ячейки
                            if j == 0:
                                if arr[i+1][j] + arr[i-1][j] + arr[i+1][j+1] + arr[i-1][j+1] + arr[i][j+1] == 3:
                                    arr[i][j] = 1

                            #Правая боковая грань матрицы без самой первой и самой последеней ячейки
                            elif j == 29:
                                if arr[i+1][j] + arr[i-1][j] + arr[i+1][j-1] + arr[i-1][j-1] + arr[i][j-1] == 3:
                                    arr[i][j] = 1

                        else:
                            #Левая боковая грань матрицы без самой первой и самой последеней ячейки
                            if j == 0:
                                if arr[i+1][j] + arr[i-1][j] + arr[i+1][j+1] + arr[i-1][j+1] + arr[i][j+1] == 2 or arr[i+1][j] + arr[i-1][j] + arr[i+1][j+1] + arr[i-1][j+1] + arr[i][j+1] == 3:
                                    arr[i][j] = 1

                                else:
                                    arr[i][j] = 0

                            #Правая боковая грань матрицы без самой первой и самой последеней ячейки
                            elif j == 29:
                                if arr[i+1][j] + arr[i-1][j] + arr[i+1][j-1] + arr[i-1][j-1] + arr[i][j-1] == 2 or arr[i+1][j] + arr[i-1][j] + arr[i+1][j-1] + arr[i-1][j-1] + arr[i][j-1] == 3:
                                    arr[i][j] = 1

                                else:
                                    arr[i][j] = 0
                            
                            

                else:
                    if arr[i][j] == 0:
                        #Верхняя грань не считая самой первой и самой последней ячейки
                        if (i == 0) and (j > 0) and (j < 29):
                            if arr[i][j-1] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j+1] == 3:
                                arr[i][j] = 1

                        #Нижняя грань не считая самой первой и самой последней ячейки
                        elif (i == 29) and (j > 0) and (j < 29):
                            if arr[i][j-1] + arr[i][j+1] + arr[i-1][j-1] + arr[i-1][j+1] + arr[i-1][j] == 3:
                                arr[i][j] = 1

                        #Здесь мы проверяем четыре угла матрицы на наличие нуля и применяем к ним инвидуальные условия проверки суммы соседей
                    
                        #Верхний левый угол матрицы
                        elif j == 0 and i == 0:
                            if arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1] == 3:
                                arr[i][j] = 1
                        #Верхний правый угол
                        elif j == 29 and i == 0:
                            if arr[i+1][j] + arr[i+1][j-1] + arr[i][j-1] == 3:
                                arr[i][j] = 1
                        #Нижний левый угол
                        elif j == 0 and i == 29:
                            if arr[i-1][j] + arr[i-1][j+1] + arr[i][j+1] == 3:
                                arr[i][j] = 1

                        #Нижний правый угол
                        elif j == 29 and i == 29:
                            if arr[i-1][j] + arr[i-1][j-1] + arr[i][j-1] == 3:
                                arr[i][j] = 1

                    
                    #Проверка условий когда клетка живая(т.е единичка в матрице)    
                    else:
                        #Верхняя грань не считая самой первой и самой последней ячейки
                        if (i == 0) and (j > 0) and (j < 29):
                            if arr[i][j-1] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j+1] == 2 or arr[i][j-1] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j+1] == 3:
                                arr[i][j] = 1

                            else:
                                arr[i][j] = 0

                        #Нижняя грань не считая самой первой и самой последней ячейки
                        elif (i == 29) and (j > 0) and (j < 29):
                            if arr[i][j-1] + arr[i][j+1] + arr[i-1][j-1] + arr[i-1][j+1] + arr[i-1][j] == 2 or arr[i][j-1] + arr[i][j+1] + arr[i-1][j-1] + arr[i-1][j+1] + arr[i-1][j] == 3:
                                arr[i][j] = 1

                            else:
                                arr[i][j] = 0

                        #Здесь мы проверяем четыре угла матрицы на наличие нуля и применяем к ним инвидуальные условия проверки суммы соседей                   
                        #Верхний левый угол матрицы
                        elif j == 0 and i == 0:
                            if arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1] == 2 or arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1] == 3:
                                arr[i][j] = 1

                            else:
                                arr[i][j] = 0
                        #Верхний правый угол
                        elif j == 29 and i == 0:
                            if arr[i+1][j] + arr[i+1][j-1] + arr[i][j-1] == 2 or arr[i+1][j] + arr[i+1][j-1] + arr[i][j-1] == 3:
                                arr[i][j] = 1

                            else:
                                arr[i][j] = 0
                        #Нижний левый угол
                        elif j == 0 and i == 29:
                            if arr[i-1][j] + arr[i-1][j+1] + arr[i][j+1] == 2 or arr[i-1][j] + arr[i-1][j+1] + arr[i][j+1] == 3:
                                arr[i][j] = 1

                            else:
                                arr[i][j] = 0

                        #Нижний правый угол
                        elif j == 29 and i == 29:
                            if arr[i-1][j] + arr[i-1][j-1] + arr[i][j-1] == 2 or arr[i-1][j] + arr[i-1][j-1] + arr[i][j-1] == 3:
                                arr[i][j] = 1

                            else:
                                arr[i][j] = 0

        print("New array: ")
        print(arr)
        self.create_new_generation(arr)

    
    def create_new_generation(self, arr):
        self.c.delete("some-tag")#Удаляем всех житиелей, чтобы спроецировать их по новой матрице

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                
                if arr[i][j] == 1:
                    self.c.create_oval(self.squere_size*j, self.squere_size*i, self.squere_size*j + self.squere_size, self.squere_size*i + self.squere_size, fill="black", outline="white")

                else:
                    continue

        self.c.pack()
        self.window.mainloop()
        self.check(arr)


    
  

game  = GameOfLife(30, 20)
game.run()

