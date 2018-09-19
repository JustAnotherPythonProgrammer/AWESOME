#! python3.6
from turtle import *
import random
ht()
LENGTH = 150
ANGLE = 30
BRANCHES = 11
REDUCTION = 0.8
Positions = []
PositionsNew = []
speed(0)
def SetUp():
    pu()
    lt(90)
    bk(320)
    pd()

def MakeTree(Length, Angle, Branches):
    fd(Length)
    Length = (Length * REDUCTION)
    Positions.append((pos(), heading()))
    for i in range(Branches - 1):
        for POS, DIR in Positions:
            pu()
            goto(POS)
            seth(DIR)
            pd()
            lt(Angle)
            fd(Length)
            PositionsNew.append((pos(), heading()))
            bk(Length)
            rt(Angle * 2)
            fd(Length)
            PositionsNew.append((pos(), heading()))
        for i in range(len(Positions)):
            Positions.pop(0)
        for THING in PositionsNew:
            Positions.append(THING)
        for i in range(len(PositionsNew)):
            PositionsNew.pop(0)
        Length = (Length * REDUCTION)

        
    



SetUp()
MakeTree(LENGTH, ANGLE, BRANCHES)
ht()
exitonclick()
