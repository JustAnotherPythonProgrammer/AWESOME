import pygame, sys
from pygame.locals import *
from math import *
pygame.init()

Black  = (  0,   0,   0)
White  = (255, 255, 255)
Green  = (  0, 255,   0)
Purple = (255,   0, 255)
Cyan   = (  0, 255, 255)

class screen():
    def __init__(self, Width, Height, BGColor):
        self.Width = Width
        self.Height = Height
        self.BGColor = BGColor
        self.Display = pygame.display.set_mode((self.Width, self.Height))
        pygame.display.set_caption('Lissajous Curve Table')

    def Clear(self):
        self.Display.fill(self.BGColor)

    def Update(self):
        pygame.display.update()


class circle():
    def __init__(self, x, y, Radius, Color):
        self.x = x
        self.y = y
        self.Radius = Radius
        self.Color = Color

    def Draw(self, Value):
        if Value:
            pygame.draw.circle(Screen.Display, self.Color, (self.x, self.y), self.Radius, 2)


class line():
    def __init__(self, Dot, Direction, Color):
        self.Direction = Direction
        self.Dot = Dot
        self.x1 = 0
        self.y1 = 0
        self.Color = Color

    def Draw(self, Value):
        if self.Direction == 'Vertical':
            self.x1 = self.Dot.x
            self.y1 = 0
            self.x2 = self.Dot.x
            self.y2 = Screen.Height
        else:
            self.x1 = 0
            self.y1 = self.Dot.y
            self.x2 = Screen.Width
            self.y2 = self.Dot.y
        if Value:
            pygame.draw.line(Screen.Display, self.Color, (self.x1, self.y1), (self.x2, self.y2), 2)


class dot():
    def __init__(self, Circle, Line1, Line2, Type, Radius, Angle, Speed, Color):
        self.Circle = Circle
        self.Line1 = Line1
        self.Line2 = Line2
        self.Type = Type
        self.Radius = Radius
        self.Angle = Angle
        self.x = None
        self.y = None
        try:
            self.Speed = Speed * 0.003
        except: pass
        self.Color = Color

    def Draw(self, Value):
        if self.Type == 'Circle':
            self.x = self.Circle.x + (self.Circle.Radius * cos(self.Angle))
            self.y = self.Circle.y + (self.Circle.Radius * sin(self.Angle))
            self.Angle += self.Speed
        else:
            self.x = self.Line1.x1
            self.y = self.Line2.y1
        if Value:
            pygame.draw.circle(Screen.Display, self.Color, (int(self.x), int(self.y)), self.Radius)


class curve():
    def __init__(self, Dot, Color):
        self.Dot = Dot
        self.Color = Color
        self.FullPointList = []
        self.PartialPointList = []

    def UpdatePointList(self):
        self.FullPointList.append((int(self.Dot.x), int(self.Dot.y)))
        self.PartialPointList.append((int(self.Dot.x), int(self.Dot.y)))
        if len(self.PartialPointList) > 400:
            self.PartialPointList.pop(0)

    def Draw(self, Value):
        if Value:
            pygame.draw.lines(Screen.Display, self.Color, False, self.FullPointList, 3)
        else:
            pygame.draw.lines(Screen.Display, self.Color, False, self.PartialPointList, 3)

class simulation():
    def __init__(self):
        self.HorizontalCircles = []
        self.VerticalCircles   = []
        self.HorizontalLines   = []
        self.VerticalLines     = []
        self.CircleDots        = []
        self.LineDots          = []
        self.Curves            = []
        self.DrawCircles = True
        self.DrawLines   = True
        self.DrawDots    = True
        self.Trace       = True

    def Inputs(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_c:
                    if self.DrawCircles == True:
                        self.DrawCircles = False
                    else:
                        self.DrawCircles = True
                if event.key == K_l:
                    if self.DrawLines == True:
                        self.DrawLines = False
                    else:
                        self.DrawLines = True
                if event.key == K_d:
                    if self.DrawDots == True:
                        self.DrawDots = False
                    else:
                        self.DrawDots = True
                if event.key == K_SPACE:
                    if self.Trace == True:
                        self.Trace = False
                    else:
                        self.Trace = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def MakeCircles(self, Horizontal, Vertical, HorizontalRadius, VerticalRadius):
        for i in range(Horizontal):
            self.HorizontalCircles.append(circle(160 + (i * 109), 50, 50, White))
        for i in range(Vertical):
            self.VerticalCircles.append(circle(50, 160 + (i * 109), 50, White))

    def MakeCircleDots(self):
        for i in range(len(self.HorizontalCircles)):
            self.CircleDots.append(dot(self.HorizontalCircles[i], None, None, 'Circle', 5, 0, i + 1, Green))
        for i in range(len(self.VerticalCircles)):
            self.CircleDots.append(dot(self.VerticalCircles[i], None, None, 'Circle', 5, 0, i + 1, Green))

    def MakeLines(self):
        for i in range(len(self.HorizontalCircles)):
            self.VerticalLines.append(line(self.CircleDots[i], 'Vertical', Cyan))
        for i in range(len(self.VerticalCircles)):
            self.HorizontalLines.append(line(self.CircleDots[i + len(self.HorizontalCircles)], 'Horizontal', Cyan))

    def MakeLineDots(self):
        for Line in self.VerticalLines:
            for OtherLine in self.HorizontalLines:
                self.LineDots.append(dot(None, Line, OtherLine, 'Line', 5, None, None, Green))

    def MakeCurves(self):
        for Dot in self.LineDots:
            self.Curves.append(curve(Dot, Purple))

    def Clear(self, List):
        for Thing in range(len(List)):
            List.pop(0)

    def ClearAll(self):
        self.Clear(self.HorizontalCircles)
        self.Clear(self.VerticalCircles)
        self.Clear(self.HorizontalLines)
        self.Clear(self.VerticalLines)
        self.Clear(self.CircleDots)
        self.Clear(self.LineDots)
        self.Clear(self.Curves)

    def SetUp(self):
        self.MakeCircles(8, 5, 10, 10)
        self.MakeCircleDots()
        self.MakeLines()
        self.MakeLineDots()
        self.MakeCurves()

    def Draw(self):
        Screen.Clear()
        self.Inputs()
        for Circle in self.HorizontalCircles:
            Circle.Draw(self.DrawCircles)
        for Circle in self.VerticalCircles:
            Circle.Draw(self.DrawCircles)
        for Dot in self.CircleDots:
            Dot.Draw(self.DrawDots)
        for Line in self.HorizontalLines:
            Line.Draw(self.DrawLines)
        for Line in self.VerticalLines:
            Line.Draw(self.DrawLines)
        for Dot in self.LineDots:
            Dot.Draw(self.DrawDots)
        for Curve in self.Curves:
            Curve.UpdatePointList()
            try:
                Curve.Draw(self.Trace)
            except: pass
        if self.Trace:
            if self.CircleDots[0].Angle >= 8:
                self.ClearAll()
                self.SetUp()
        Screen.Update()


def Main():
    global Screen, Simulation
    Screen = screen(1000, 650, Black)
    Simulation = simulation()
    Simulation.SetUp()
    while True:
        Simulation.Draw()


if __name__ == "__main__":
    Main()
