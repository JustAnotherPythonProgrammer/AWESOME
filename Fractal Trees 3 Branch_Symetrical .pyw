#! python3.6
from turtle import *
import random
ht()
LENGTH = 200
ANGLE = 35
BRANCHES = 8
REDUCTION = 0.6
Positions = []
PositionsNew = []
speed(0)
def SetUp():
    pu()
    lt(90)
    bk(315)
    pd()

def MakeTree(Length, Angle, Branches):
    Colors = ['red', 'orange', 'yellow', 'green']
    WIDTH = 9
    width(WIDTH)
    pencolor('brown')
    fd(Length)
    Length = (Length * REDUCTION)
    Positions.append((pos(), heading()))
    for i in range(Branches - 1):
        for POS, DIR in Positions:
            if i == 6:
                COLOR = random.randint(0, 3)
                pencolor(Colors[COLOR])
            pu()
            goto(POS)
            seth(DIR)
            pd()
            lt(Angle)
            fd(Length)
            PositionsNew.append((pos(), heading()))
            bk(Length)
            rt(Angle)
            fd(Length + (Length * (1 - REDUCTION)))
            PositionsNew.append((pos(), heading()))
            bk(Length + (Length * (1 - REDUCTION)))
            rt(Angle)
            fd(Length)
            PositionsNew.append((pos(), heading()))
        for i in range(len(Positions)):
            Positions.pop(0)
        for THING in PositionsNew:
            Positions.append(THING)
        for i in range(len(PositionsNew)):
            PositionsNew.pop(0)
        Length = (Length * REDUCTION)
        WIDTH -= 1
        width(WIDTH)
            

        
    



SetUp()
MakeTree(LENGTH, ANGLE, BRANCHES)
exitonclick()
