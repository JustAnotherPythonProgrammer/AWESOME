import pygame, sys, random, copy
from pygame.locals import *
pygame.init()
pygame.joystick.init()

Black = (  0,   0,   0)
Green = (  0, 255,   0)
Red   = (255,   0,   0)
Brown = (150,  75,   0)
Cyan  = (  0, 255, 255)

class screen():
    def __init__(self):
        self.Clock = pygame.time.Clock()
        self.FPS = 1
        self.Display = pygame.display.set_mode((700, 500))
        pygame.display.set_caption('Snake!')

    def Clear(self):
        self.Display.fill(Black)

    def UpdateFPS(self, Score):
        if Score:
            self.FPS = Score

    def Update(self):
        pygame.display.update()
        self.UpdateFPS(Game.Score)
        self.Clock.tick(self.FPS)


class snake():
    def __init__(self, BodyColor, HeadColor):
        self.BC = BodyColor
        self.HC = HeadColor
        self.Body = [[100, 100], [110, 100], [120, 100]]
        self.CHANGING_Body = []
        self.Direction = 'Right'
        self.CURRENT_Direction = 'Right'
        self.Dead = False

    def ChangeDirection(self, KEY):
        if KEY == K_UP:
            if self.CURRENT_Direction != 'Down':
                self.Direction = 'Up'
                self.CURRENT_Direction = 'Up'
        if KEY == K_DOWN:
            if self.CURRENT_Direction != 'Up':
                self.Direction = 'Down'
                self.CURRENT_Direction = 'Down'
        if KEY == K_LEFT:
            if self.CURRENT_Direction != 'Right':
                self.Direction = 'Left'
                self.CURRENT_Direction = 'Left'
        if KEY == K_RIGHT:
            if self.CURRENT_Direction != 'Left':
                self.Direction = 'Right'
                self.CURRENT_Direction = 'Right'

    def CopyAndClear(self, Body1, Body2):
        for i in range(len(Body2)):
            Body2.pop(0)
        for i in Body1:
            Body2.append(i)
        for i in range(len(Body1)):
            Body1.pop(0)

    def Draw(self):
        for i in range(len(self.Body) - 1):
            pygame.draw.rect(Screen.Display, self.BC, (self.Body[i][0], self.Body[i][1], 10, 10), 0)
        pygame.draw.rect(Screen.Display, self.HC, (self.Body[-1][0], self.Body[-1][1], 10, 10), 0)

    def Update(self, Value):
        if not Value:
            for index, _ in enumerate(self.Body):
                try:
                    self.CHANGING_Body.append(self.Body[index + 1])
                except IndexError:
                    if self.Direction == 'Right':
                        self.CHANGING_Body.append([self.Body[-1][0] + 10, self.Body[-1][1]])
                    if self.Direction == 'Left':
                        self.CHANGING_Body.append([self.Body[-1][0] - 10, self.Body[-1][1]])
                    if self.Direction == 'Up':
                        self.CHANGING_Body.append([self.Body[-1][0], self.Body[-1][1] - 10])
                    if self.Direction == 'Down':
                        self.CHANGING_Body.append([self.Body[-1][0], self.Body[-1][1] + 10])

            self.CopyAndClear(self.CHANGING_Body, self.Body)

    def Grow(self):
        self.CHANGING_Body = copy.deepcopy(self.Body)
        self.TEMPORARY = copy.deepcopy(self.CHANGING_Body[-1])
        self.CHANGING_Body.insert(-1, self.TEMPORARY)
        if self.Direction == 'Right':
            self.CHANGING_Body[-1][0] += 10
        if self.Direction == 'Left':
            self.CHANGING_Body[-1][0] -= 10
        if self.Direction == 'Up':
            self.CHANGING_Body[-1][1] -= 10
        if self.Direction == 'Down':
            self.CHANGING_Body[-1][1] += 10
        self.CopyAndClear(self.CHANGING_Body, self.Body)

    def IsDead(self):
        if Snake.Body[-1] in Snake.Body[:-1] or self.Body[-1][0] < 0  or self.Body[-1][0] > 690 or self.Body[-1][1] < 0 or self.Body[-1][1] > 490:
            self.Dead = True


class food():
    def __init__(self, color):
        self.GenerateLocation()
        self.Color = color

    def Draw(self):
        pygame.draw.rect(Screen.Display, self.Color, (self.x, self.y, 10, 10), 0)

    def Collision(self):
        global Food
        if Snake.Body[-1][0] == self.x and Snake.Body[-1][1] == self.y:
            self.GenerateLocation()
            Snake.Grow()
            Game.UpdateScore(1, Cyan)
            Screen.UpdateFPS(Game.Score)
            return True
        return False

    def GenerateLocation(self):
        while True:
            self.x = (random.randint(0, 69) * 10)
            self.y = (random.randint(0, 49) * 10)
            if [self.x, self.y] in Snake.Body:
                continue
            break


class controller():
    def __init__(self):
        self.Device = pygame.joystick.Joystick()
        self.Device.init()

    def Input(self):
        self.LeftStickHorizontal = '{:>6.3f}'.format(self.device.get_axis(0))
        self.LeftStickVertical   = '{:>6.3f}'.format(self.device.get_axis(1))
        self.LeftStickHorizontal, self.LeftStickVertical = float(self.LeftStickHorizontal), float(self.LeftStickVertical)
        if float(self.LeftStickHorizontal) == -1:
            Snake.ChangeDirection(K_LEFT)
        if float(self.LeftStickHorizontal) == 1:
            Snake.ChangeDirection(K_RIGHT)
        if float(self.LeftStickVertical) == -1:
            Snake.ChangeDirection(K_UP)
        if float(self.LeftStickVertical) == 1:
            Snake.ChangeDirection(K_DOWN)


class game():
    def __init__(self):
        self.Score = 0
        self.Score_Font = pygame.font.SysFont('Impact', 20)
        self.GameOver_Font = pygame.font.SysFont('Impact', 100)
        self.Start_Font = pygame.font.SysFont('Impact', 50)
        self.Score_Text = 'Score: '
        self.StartGame_Text = 'Press Space To Begin...'
        self.GameOver_Text = 'Game Over'
        self.Score_Text_Location = (10, 10)
        self.GameOver_Text_Location = (150, 150)
        self.StartGame_Text_Location = (150, 150)
        self.ScoreColor = Cyan
        self.Start = False

    def Terminate(self):
        pygame.quit()
        sys.exit()

    def Inputs(self, Type):
        for event in pygame.event.get():
            if Type == 'GAME':
                if event.type == KEYDOWN:
                        Snake.ChangeDirection(event.key)
                if event.type == QUIT:
                    self.Terminate()
            if Type == 'BEGIN':
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.Start = True
                if event.type == QUIT:
                    self.Terminate()

    def UpdateScore(self, Value, Color):
        self.Score += Value
        self.Score_Text = self.Score_Text[:7] + str(self.Score)
        self.SURFACE_Score_Text = self.Score_Font.render(self.Score_Text, True, Color)

    def DisplayScore(self):
        Screen.Display.blit(self.SURFACE_Score_Text, self.Score_Text_Location)

    def GameOver(self, Value):
        if Value:
            Screen.Clear()
            self.GameOver_Surface = self.GameOver_Font.render(self.GameOver_Text, True, Red)
            self.Score_Font = self.Start_Font
            self.Score_Text_Location = (275, 275)
            self.UpdateScore(0, Red)
            Screen.Display.blit(self.GameOver_Surface, self.GameOver_Text_Location)
            self.DisplayScore()

    def Begin(self, Value):
        if not Value:
            Screen.Clear()
            self.Start_Surface = self.Start_Font.render(self.StartGame_Text, True, Green)
            Screen.Display.blit(self.Start_Surface, self.StartGame_Text_Location)
        return Value


def Main():
    global Snake, Food, Game, Screen
    Screen = screen()
    Snake = snake(Green, Brown)
    Food = food(Red)
    Game = game()
    Game.UpdateScore(0, Cyan)
    Screen.UpdateFPS(Game.Score)
    try:
        Controller = controller()
    except:
        pass

    Screen.FPS = 0
    while True:
        if Game.Begin(Game.Start):
            break
        Game.Inputs('BEGIN')
        Screen.Update()
    Screen.FPS = 10

    while True:
        Screen.Clear()
        Food.Draw()
        Game.Inputs('GAME')
        try:
            Controller.Input()
        except:
            pass
        Snake.Update(Food.Collision())
        Snake.Draw()
        Snake.IsDead()
        Game.DisplayScore()
        Game.GameOver(Snake.Dead)
        Screen.Update()


if __name__ == "__main__":
    Main()
