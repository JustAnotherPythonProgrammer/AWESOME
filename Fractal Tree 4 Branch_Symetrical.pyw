from turtle import *

Positions = []
PositionsNew = []
Times = 6
Length = 100

def SetUp():
    pu()
    lt(90)
    bk(315)
    pd()
    ht()
    speed(0)
    
def MakeTree(TIMES, LENGTH):
    fd(LENGTH)
    Positions.append((pos(), heading()))
    for i in range(TIMES):
        for POS, DIRECTION in Positions:
            pu()
            goto(POS)
            seth(DIRECTION)
            pd()
            lt(27 + (27 / 2))
            fd(LENGTH)
            PositionsNew.append((pos(), heading()))
            bk(LENGTH)
            rt(27)
            fd(LENGTH + (LENGTH * 0.25))
            lt(15)
            fd(LENGTH + (LENGTH * 0.25))
            PositionsNew.append((pos(), heading()))
            bk(LENGTH + (LENGTH * 0.25))
            rt(15)
            bk(LENGTH + (LENGTH * 0.25))
            rt(27)
            fd(LENGTH + (LENGTH * 0.25))
            rt(15)
            fd(LENGTH + (LENGTH * 0.25))
            PositionsNew.append((pos(), heading()))
            bk(LENGTH + (LENGTH * 0.25))
            lt(15)
            bk(LENGTH + (LENGTH * 0.25))
            rt(27)
            fd(LENGTH)
            PositionsNew.append((pos(), heading()))
        for i in range(len(Positions)):
            Positions.pop(0)
        for THING in PositionsNew:
            Positions.append(THING)
        for i in range(len(PositionsNew)):
            PositionsNew.pop(0)
        LENGTH *= 0.5




SetUp()
MakeTree(Times, Length)
exitonclick()
