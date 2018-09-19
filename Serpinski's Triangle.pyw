from turtle import *
ht()
pencolor('purple')
Times = 7
Length = 600
Positions = []
PositionsNew = []
def SetUp():
    speed(1)
    pu()
    bk(350)
    rt(90)
    fd(300)
    lt(90)
    pd()

def MakeFractals(TIMES, LENGTH):
    speed(0)
    fd(LENGTH / 2)
    Positions.append((pos(), heading()))
    fd(LENGTH / 2)
    lt(120)
    fd(LENGTH)
    lt(120)
    fd(LENGTH)
    for i in range(TIMES):
        LENGTH /= 2
        for POS, DIRECTION in Positions:
            pu()
            goto(POS)
            pd()
            seth(DIRECTION)
            if (i + 2) % 2 == 0:
                lt(60)
                fd(LENGTH / 2)
                PositionsNew.append((pos(), heading()))
                fd(LENGTH / 2)
                lt(120)
                fd(LENGTH / 2)
                PositionsNew.append((pos(), heading()))
                fd(LENGTH / 2)
                lt(120)
                fd(LENGTH / 2)
                PositionsNew.append((pos(), heading()))
                fd(LENGTH / 2)
            else:
                rt(60)
                fd(LENGTH / 2)
                PositionsNew.append((pos(), heading()))
                fd(LENGTH / 2)
                rt(120)
                fd(LENGTH / 2)
                PositionsNew.append((pos(), heading()))
                fd(LENGTH / 2)
                rt(120)
                fd(LENGTH / 2)
                PositionsNew.append((pos(), heading()))
                fd(LENGTH / 2)
        for i in range(len(Positions)):
            Positions.pop(0)
        for THING in PositionsNew:
            Positions.append(THING)
        for i in range(len(PositionsNew)):
            PositionsNew.pop(0)
            
        

SetUp()
MakeFractals(Times, Length)
exitonclick()
