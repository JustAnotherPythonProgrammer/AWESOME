#! python3.2
import pygame, random, sys, datetime
from pygame.locals import *
pygame.init()

Display = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Sudoku Solver')
Font = pygame.font.SysFont('Impact Regular', 40)
Blue = (0, 0, 255)
White = (255, 255, 255)
Black = (0, 0, 0)
File = open('C:\\Users\\Sachin\\Desktop\\Programming\\Python\\Program Related Stuff\\Sudoku Solver Files\\Sudoku_Input.txt', 'r')


def Update():
    Display.fill(White)
    DrawBoard()
    DrawNumbers(Matrix)
    pygame.display.update()

def DrawBoard():
    x = 50
    y = 20
    Counter = 0
    _ = 0
    for i in range(10):
        if Counter == 3:
            pygame.draw.line(Display, Black, (x, y), (500, y), 5)
            Counter = 0
        else:
            pygame.draw.line(Display, Black, (x, y), (500, y))
        y += 50
        _ += 1
        if _ > 8:
            pass
        else:
            Counter += 1
    Counter = 0
    _ = 0
    for i in range(10):
        if Counter == 3:
            pygame.draw.line(Display, Black, (x, 20), (x, 470), 5)
            Counter = 0
        else:
            pygame.draw.line(Display, Black, (x, 20), (x, 470))
        x += 50
        _ += 1
        if _ > 8:
            pass
        else:
            Counter += 1


def FillGraph():
    global Matrix, Font
    Matrix = []
    for Row in File:
        Matrix.append(Row.split())
            

def DrawNumbers(MATRIX):
    y = 30
    for ROW in range(0, 9):
        x = 65
        for THING in range(0, 9):
            if (ROW, THING) in Blanks:
                if MATRIX[ROW][THING] == '0':
                    FontSurface = Font.render('', True, Blue)
                else:
                    FontSurface = Font.render(MATRIX[ROW][THING], True, Blue)
            else:
                if MATRIX[ROW][THING] == '0':
                    FontSurface = Font.render('', True, Black)
                else:
                    FontSurface = Font.render(MATRIX[ROW][THING], True, Black)
            Display.blit(FontSurface, (x, y))
            x += 50
        y += 50

def FindBlanks():
    global Blanks
    Blanks = []
    for ROW, _ in enumerate(Matrix):
        for COLUMN, _ in enumerate(Matrix[ROW]):
            if _ == '0':
                Blanks.append((ROW, COLUMN))

def Solve():
    global NoSolution, Time
    Numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    Solved = False

    def Check():
        global MatrixStraights
        Valid = True
        MatrixStraights = [[Matrix[0][0], Matrix[1][0], Matrix[2][0], Matrix[3][0], Matrix[4][0], Matrix[5][0], Matrix[6][0], Matrix[7][0], Matrix[8][0]],
                           [Matrix[0][1], Matrix[1][1], Matrix[2][1], Matrix[3][1], Matrix[4][1], Matrix[5][1], Matrix[6][1], Matrix[7][1], Matrix[8][1]],
                           [Matrix[0][2], Matrix[1][2], Matrix[2][2], Matrix[3][2], Matrix[4][2], Matrix[5][2], Matrix[6][2], Matrix[7][2], Matrix[8][2]],
                           [Matrix[0][3], Matrix[1][3], Matrix[2][3], Matrix[3][3], Matrix[4][3], Matrix[5][3], Matrix[6][3], Matrix[7][3], Matrix[8][3]],
                           [Matrix[0][4], Matrix[1][4], Matrix[2][4], Matrix[3][4], Matrix[4][4], Matrix[5][4], Matrix[6][4], Matrix[7][4], Matrix[8][4]],
                           [Matrix[0][5], Matrix[1][5], Matrix[2][5], Matrix[3][5], Matrix[4][5], Matrix[5][5], Matrix[6][5], Matrix[7][5], Matrix[8][5]],
                           [Matrix[0][6], Matrix[1][6], Matrix[2][6], Matrix[3][6], Matrix[4][6], Matrix[5][6], Matrix[6][6], Matrix[7][6], Matrix[8][6]],
                           [Matrix[0][7], Matrix[1][7], Matrix[2][7], Matrix[3][7], Matrix[4][7], Matrix[5][7], Matrix[6][7], Matrix[7][7], Matrix[8][7]],
                           [Matrix[0][8], Matrix[1][8], Matrix[2][8], Matrix[3][8], Matrix[4][8], Matrix[5][8], Matrix[6][8], Matrix[7][8], Matrix[8][8]],
                           Matrix[0],
                           Matrix[1],
                           Matrix[2],
                           Matrix[3],
                           Matrix[4],
                           Matrix[5],
                           Matrix[6],
                           Matrix[7],
                           Matrix[8],
                           [Matrix[0][0], Matrix[0][1], Matrix[0][2], Matrix[1][0], Matrix[1][1], Matrix[1][2], Matrix[2][0], Matrix[2][1], Matrix[2][2]],
                           [Matrix[0][3], Matrix[0][4], Matrix[0][5], Matrix[1][3], Matrix[1][4], Matrix[1][5], Matrix[2][3], Matrix[2][4], Matrix[2][5]],
                           [Matrix[0][6], Matrix[0][7], Matrix[0][8], Matrix[1][6], Matrix[1][7], Matrix[1][8], Matrix[2][6], Matrix[2][7], Matrix[2][8]],
                           [Matrix[3][0], Matrix[3][1], Matrix[3][2], Matrix[4][0], Matrix[4][1], Matrix[4][2], Matrix[5][0], Matrix[5][1], Matrix[5][2]],
                           [Matrix[3][3], Matrix[3][4], Matrix[3][5], Matrix[4][3], Matrix[4][4], Matrix[4][5], Matrix[5][3], Matrix[5][4], Matrix[5][5]],
                           [Matrix[3][6], Matrix[3][7], Matrix[3][8], Matrix[4][6], Matrix[4][7], Matrix[4][8], Matrix[5][6], Matrix[5][7], Matrix[5][8]],
                           [Matrix[6][0], Matrix[6][1], Matrix[6][2], Matrix[7][0], Matrix[7][1], Matrix[7][2], Matrix[8][0], Matrix[8][1], Matrix[8][2]],
                           [Matrix[6][3], Matrix[6][4], Matrix[6][5], Matrix[7][3], Matrix[7][4], Matrix[7][5], Matrix[8][3], Matrix[8][4], Matrix[8][5]],
                           [Matrix[6][6], Matrix[6][7], Matrix[6][8], Matrix[7][6], Matrix[7][7], Matrix[7][8], Matrix[8][6], Matrix[8][7], Matrix[8][8]]]
        for ROW in MatrixStraights:
            for THING in Numbers:
                SomeThing = ROW.count(THING)
                if SomeThing > 1:
                    return False
        return True
        
    if len(Blanks) == 0:
        if Check() == False:
            NoSolution = True
            Solved = True
        else:
            Solved = True
            
            
    _Position = 0
    _Number = 0
    EXIT = False
    NoSolution = False
    Start = datetime.datetime.now()
    while Solved == False:
        try:
            _x, _y = Blanks[_Position]
            Matrix[_x][_y] = Numbers[_Number]    
        except IndexError:
            Solved = True
        if Check() == False:
            _Number += 1     
            if _Number == 9:
                if _Position - 1 < 0:
                    NoSolution = True
                else:
                    Matrix[_x][_y] = '0'
                    _x, _y = Blanks[_Position - 1]
                    CURRENT = Matrix[_x][_y]
                    if CURRENT == '9':
                        Matrix[_x][_y] = '0'
                        _Position -= 1
                        _x, _y = Blanks[_Position - 1]
                        CURRENT = Matrix[_x][_y]
                    if CURRENT == '9':
                        Matrix[_x][_y] = '0'
                        _Position -= 1
                        _x, _y = Blanks[_Position - 1]
                        CURRENT = Matrix[_x][_y]   
                    for INDEX, NUMBER in enumerate(Numbers):
                        if NUMBER == CURRENT:
                            _Number = INDEX + 1
                    Matrix[_x][_y] = Numbers[_Number]
                    EXIT = False
                    while EXIT == False:
                        if Check() == False:
                            _Number += 1
                            if _Number == 9:
                                _Position -= 1
                                _Number -= 1
                                EXIT = True
                            else:
                                Matrix[_x][_y] = Numbers[_Number]
                        else:
                            EXIT = True
                            _Number = 0
        else:
            _Number = 0
            _Position += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        Update()
    End = datetime.datetime.now()
    StartSeconds = ((Start.hour * 60 * 60) + (Start.minute * 60) + Start.second + (Start.microsecond / 1000000))
    EndSeconds = ((End.hour * 60 * 60) + (End.minute * 60) + End.second + (End.microsecond / 1000000))
    Total = EndSeconds - StartSeconds
    if Total > 60:
        _ = Total // 60
        Total = (_, (Total - (_ * 60)))
        Time = str(Total[0]) + ' minutes and ' + str(Total[1]) + ' seconds'
    else:
        Time = str(Total) + ' seconds'

    
            
            
def Main():
    FirstTime = True
    FillGraph()
    FindBlanks()
    TimeSurface = Font.render(' ', True, Black)
    while True:
        Display.fill(White)
        DrawBoard()
        if FirstTime == True:
            MessageSurface = Font.render('Press space to start', True, Black)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if FirstTime == True:
                        Solve()
                        FirstTime = False
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if FirstTime == False:
            if NoSolution == True:
                MessageSurface = Font.render('No Solution', True, Black)
            else:
                MessageSurface = Font.render('Solved in', True, Black)
                TimeSurface = Font.render(Time, True, Black)
        Display.blit(MessageSurface, (525, 150))
        Display.blit(TimeSurface, (525, 180))
        DrawNumbers(Matrix)
        pygame.display.update()

if __name__ == "__main__":
    Main()
