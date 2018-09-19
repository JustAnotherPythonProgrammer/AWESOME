from turtle import *
speed(1)
pencolor('light blue')
fillcolor('light blue')
Positions = []
PositionsNew = []
TrianglePositions = []
ht()
def SetUp():
    pu()
    lt(90)
    bk(150)
    rt(90)
    bk(100)
    lt(60)
    pd()
    speed(0)

def MakeLine(LENGTH):
    for i in range(len(Positions)):
        Positions.pop(0)
    for i in range(len(PositionsNew)):
        PositionsNew.pop(0)
    PositionsNew.append((pos(), heading()))
    fd(LENGTH)
    TrianglePositions.append((pos(), heading()))
    bk(LENGTH)
    for i in range(6):
        for POS, DIRECTION in Positions:
            pu()
            goto(POS)
            seth(DIRECTION)
            pd()
            fd(LENGTH)
            lt(60)
            PositionsNew.append((pos(), heading()))
            begin_fill()
            fd(LENGTH)
            rt(120)
            PositionsNew.append((pos(), heading()))
            fd(LENGTH)
            end_fill()
            lt(60)
            PositionsNew.append((pos(), heading()))
        for i in range(len(Positions) - 1):
            Positions.pop(1)
        for Thing in PositionsNew:
            Positions.append(Thing)
        LENGTH /= 3


def MakeSnowFlake():
    for i in range(3):
        MakeLine(300)
        pu()
        goto(TrianglePositions[0][0])
        seth(TrianglePositions[0][1])
        TrianglePositions.pop(0)
        pd()
        rt(120)
    begin_fill()
    seth(60)
    fd(300)
    rt(120)
    fd(300)
    rt(120)
    fd(300)
    end_fill()
SetUp()
MakeSnowFlake()
exitonclick()
