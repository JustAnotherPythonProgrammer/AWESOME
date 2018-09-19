import pygame, sys, random
from pygame.locals import *
pygame.init()

Black = (0, 0, 0)
Green = (0, 255, 0)
Red = (255, 0, 0)
Brown = (150, 75, 0)


class screen():
    def __init__(self):
        self.Display = pygame.display.set_mode((700, 500))
        pygame.display.set_caption('Snake!')
        self.Score = 0
        self.Clock = pygame.time.Clock()
        self.FPS = 1
        self.Font = pygame.font.SysFont('Impact', 20)
        self.Score_Text = 'Score: '
        self.StartGame_Text = 'Press Space To Begin...'
        self.GameOver_Text = 'Game Over'
        
    def Reset(self):
        self.Display.fill(Black)

    def Update(self):
        pygame.display.update()
        self.Clock.tick(self.FPS)


class snake(screen):
    def __init__(self, BodyColor, HeadColor):
        screen.__init__(self)
        self.BC = BodyColor
        self.HC = HeadColor
        self.Body = [[100, 100], [110, 100], [120, 100]]
        self.Direction = 'Right'

    def Draw(self):
        for i in range(len(self.Body) - 1):
            pygame.draw.rect(self.Display, self.BC, (self.Body[i][0], self.Body[i][1], 10, 10), 0)
        pygame.draw.rect(self.Display, self.HC, (self.Body[len(self.Body) - 1][0], self.Body[len(self.Body) - 1][1], 10, 10), 0)

    def Update(self):
        #[[100, 100], [110, 100], [120, 100]]
        for Index, _ in enumerate(self.Body):
            try:
                self.Body[Index] = self.Body[Index + 1]
            except IndexError:
                if self.Direction == 'Right':
                    self.Body[-1][0] += 10
                if self.Direction == 'Left':
                    self.Body[-1][0] -= 10
                if self.Direction == 'Up':
                    self.Body[-1][1] -= 10
                if self.Direction == 'Down':
                    self.Body[-1][1] += 10


class food(screen):
    def __init__(self, x, y, color):
        screen.__init__(self)
        self.X = x * 10
        self.Y = y * 10
        self.Color = color

    def Draw(self):
        pygame.draw.rect(self.Display, self.Color, (self.X, self.Y, 10, 10), 0)

            
class game():
    def __init__(self):
        pass

    def Terminate(self):
        pygame.quit()
        sys.exit()
            
    
def Main():
    Screen = screen()
    Snake = snake(Green, Brown)
    Food = food(random.randint(0, 71), random.randint(0, 51), Red)
    Game = game()
    while True:
        Screen.Reset()
        Snake.Draw()
        Snake.Update()
        Food.Draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                Game.Terminate()
        Screen.Update()


while __name__ == "__main__":
    Main()
