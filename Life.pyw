import pygame, sys, random
from pygame.locals import *
pygame.init()

Display = pygame.display.set_mode((700, 640))
pygame.display.set_caption('Game of Life')
pygame.key.set_repeat(500, 100)
Font = pygame.font.SysFont('Impact Regular', 40)

Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Purple = (255, 0, 255)

class Graph():
    def __init__(self):
        pass

    def Draw(Number_of_Rows, Number_of_Columns, Size_of_each_Block):
        global Rows, Columns, Size, Total
        x = 10
        y = 10
        Rows, Columns, Size = Number_of_Rows, Number_of_Columns, Size_of_each_Block
        Total = Rows * Columns
        for i in range(Rows + 1):
            pygame.draw.line(Display, Purple, (10, y), (Columns * Size + 10, y), 1)
            y += Size
        for i in range(Columns + 1):
            pygame.draw.line(Display, Purple, (x, 10), (x, Rows * Size + 10), 1)
            x += Size




class Matrix():
    def __init__(self):
        pass

    def Create(List):
        x = 0
        y = 0
        Counter = 1
        for i in range(Rows):
            List.append([])
        for i in range(Total):
            Number = random.randint(0, 100)
            if Number < 41:
                List[x].append(True)
            else:
                List[x].append(False)
            Counter += 1
            y += 1
            if y == Columns:
                y = 0
                x += 1

    def Clear(List):
        for i in range(len(List)):
            List.pop(0)

    def Draw(Color, List):
        x = 0
        y = 0
        for i in range(Total):
            y_coord = 10
            x_coord = 10
            if (List[x][y]) == True:
                for i in range(x):
                    y_coord += Size
                for i in range(y):
                    x_coord += Size
                pygame.draw.rect(Display, Color, (x_coord + 1, y_coord + 1, Size - 1, Size - 1))
            y += 1
            if y == Columns:
                y = 0
                x += 1


class Logic():
    def __init__(self):
        pass
    def Progress():
        global Matrix_list, NewMatrix_list
        x = 0
        y = 0
        Counter = 0
        for i in range(Total):
            Counter = 0
            #Top Left Corner
            if x - 1 < 0 and y - 1 < 0:
                if Matrix_list[x][y + 1] == True:
                    Counter += 1
                if Matrix_list[x + 1][y] == True:
                    Counter += 1
                if Matrix_list[x + 1][y + 1] == True:
                    Counter += 1
                if Matrix_list[x][y] == True:
                    if Counter == 2 or Counter == 3:
                        pass
                    else:
                        NewMatrix_list[x][y] = False
                else:
                    if Counter == 3:
                        NewMatrix_list[x][y] = True
            #Top Right Corner
            elif x - 1 < 0 and y + 1 == Columns:
                if Matrix_list[x][y - 1] == True:
                    Counter += 1
                if Matrix_list[x + 1][y - 1] == True:
                    Counter += 1
                if Matrix_list[x + 1][y] == True:
                    Counter += 1
                if Matrix_list[x][y] == True:
                    if Counter == 2 or Counter == 3:
                        pass
                    else:
                        NewMatrix_list[x][y] = False
                else:
                    if Counter == 3:
                        NewMatrix_list[x][y] = True
            #Bottom Left Corner
            elif x + 1 == Rows and y - 1 < 0:
                if Matrix_list[x - 1][y] == True:
                    Counter += 1
                if Matrix_list[x - 1][y + 1] == True:
                    Counter += 1
                if Matrix_list[x][y + 1] == True:
                    Counter += 1
                if Matrix_list[x][y] == True:
                    if Counter == 2 or Counter == 3:
                        pass
                    else:
                        NewMatrix_list[x][y] = False
                else:
                    if Counter == 3:
                        NewMatrix_list[x][y] = True
            #Bottom Right Corner
            elif x + 1 == Rows and y + 1 == Columns:
                if Matrix_list[x - 1][y - 1] == True:
                    Counter += 1
                if Matrix_list[x - 1][y] == True:
                    Counter += 1
                if Matrix_list[x][y - 1] == True:
                    Counter += 1
                if Matrix_list[x][y] ==  True:
                    if Counter == 2 or Counter == 3:
                        pass
                    else:
                        NewMatrix_list[x][y] = False
                else:
                    if Counter == 3:
                        NewMatrix_list[x][y] = True
            #Top Row NOT CORNERS
            elif x - 1 < 0 and y > 0:
                if Matrix_list[x][y - 1] == True:
                    Counter += 1
                if Matrix_list[x][y + 1] == True:
                    Counter += 1
                if Matrix_list[x + 1][y - 1] == True:
                    Counter += 1
                if Matrix_list[x + 1][y] == True:
                    Counter += 1
                if Matrix_list[x + 1][y + 1] == True:
                    Counter += 1
                if Matrix_list[x][y] == True:
                    if Counter == 2 or Counter == 3:
                        pass
                    else:
                        NewMatrix_list[x][y] = False
                else:
                    if Counter == 3:
                        NewMatrix_list[x][y] = True
            #Left Column NOT CORNERS
            elif x > 0 and y - 1 < 0:
                if Matrix_list[x - 1][y] == True:
                    Counter += 1
                if Matrix_list[x - 1][y + 1] == True:
                    Counter += 1
                if Matrix_list[x][y + 1] == True:
                    Counter += 1
                if Matrix_list[x + 1][y] == True:
                    Counter += 1
                if Matrix_list[x + 1][y + 1] == True:
                    Counter += 1
                if Matrix_list[x][y] == True:
                    if Counter == 2 or Counter == 3:
                        pass
                    else:
                        NewMatrix_list[x][y] = False
                else:
                    if Counter == 3:
                        NewMatrix_list[x][y] = True
            #Bottom Row NOT CORNERS
            elif x + 1 == Rows and y > 0:
                if Matrix_list[x - 1][y - 1] == True:
                    Counter += 1
                if Matrix_list[x - 1][y] == True:
                    Counter += 1
                if Matrix_list[x - 1][y + 1] == True:
                    Counter += 1
                if Matrix_list[x][y - 1] == True:
                    Counter += 1
                if Matrix_list[x][y + 1] == True:
                    Counter += 1
                if Matrix_list[x][y] == True:
                    if Counter == 2 or Counter == 3:
                        pass
                    else:
                        NewMatrix_list[x][y] = False
                else:
                    if Counter == 3:
                        NewMatrix_list[x][y] = True
            #Right Column NOT CORNERS
            elif x > 0 and y + 1 == Columns:
                if Matrix_list[x - 1][y - 1] == True:
                    Counter += 1
                if Matrix_list[x - 1][y] == True:
                    Counter += 1
                if Matrix_list[x][y - 1] == True:
                    Counter += 1
                if Matrix_list[x + 1][y - 1] == True:
                    Counter += 1
                if Matrix_list[x + 1][y] == True:
                    Counter += 1
                if Matrix_list[x][y] == True:
                    if Counter == 2 or Counter == 3:
                        pass
                    else:
                        NewMatrix_list[x][y] = False
                else:
                    if Counter == 3:
                        NewMatrix_list[x][y] = True

            #Every Other Block
            else:
                if Matrix_list[x - 1][y - 1] == True:
                    Counter += 1
                if Matrix_list[x - 1][y] == True:
                    Counter += 1
                if Matrix_list[x - 1][y + 1] == True:
                    Counter += 1
                if Matrix_list[x][y - 1] == True:
                    Counter += 1
                if Matrix_list[x][y + 1] == True:
                    Counter += 1
                if Matrix_list[x + 1][y - 1] == True:
                    Counter += 1
                if Matrix_list[x + 1][y] == True:
                    Counter += 1
                if Matrix_list[x + 1][y + 1] == True:
                    Counter += 1
                if Matrix_list[x][y] == True:
                    if Counter == 2 or Counter == 3:
                        pass
                    else:
                        NewMatrix_list[x][y] = False
                else:
                    if Counter == 3:
                        NewMatrix_list[x][y] = True
            y += 1
            if y == Columns:
                y = 0
                x += 1
        y = 0
        x = 0
        for i in range(Total):
            Matrix_list[x][y] = NewMatrix_list[x][y]
            y += 1
            if y == Columns:
                y = 0
                x += 1

def ShowGeneration(Color):
    FontSurface = Font.render('Generation = ' + str(Generation), True, Color)    
    Display.blit(FontSurface, (10, 600))
    
def Main():
    global Matrix_list, NewMatrix_list, Generation
    Matrix_list = []
    NewMatrix_list = []
    Graph.Draw(58, 68, 10)
    Matrix.Create(Matrix_list)
    Matrix.Create(NewMatrix_list)
    Generation = 0
    GraphOn = True
    Pause = True
    while True:
        Display.fill(Black)

        if GraphOn == True:
            Graph.Draw(58, 68, 10)

        Matrix.Draw(Green, NewMatrix_list)

        if Pause != True:
            Logic.Progress()
            Generation += 1

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_t:
                    if GraphOn == False:
                        GraphOn = True
                    else:
                        GraphOn = False
                if event.key == K_p:
                    if Pause == True:
                        Pause = False
                    else:
                        Pause = True
                if event.key == K_ESCAPE:
                    Matrix.Clear(Matrix_list)
                    Matrix.Clear(NewMatrix_list)
                    Matrix.Create(Matrix_list)
                    Matrix.Create(NewMatrix_list)
                    Generation = 0
                if event.key == K_SPACE:
                    Logic.Progress()
                    Generation += 1

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        ShowGeneration(Red)
        pygame.display.update()


if __name__ == '__main__':
    Main()
