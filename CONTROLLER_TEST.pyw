#! python3.2
import pygame, sys, random, math, pygame.gfxdraw
from pygame.locals import *
pygame.init()
pygame.joystick.init()
pygame.key.set_repeat(250, 100)
Clock = pygame.time.Clock()
FPS = 10


class screen():
    def __init__(self):
        self.Display = pygame.display.set_mode((600, 500))
        pygame.display.set_caption('Controller Test')
    def Update(self):
        self.Display.fill((0, 0, 0))
        Player.Draw()
        Food.Draw()
        Food.Collision()
        pygame.display.update()
        Clock.tick(FPS)

class player():
    def __init__(self, X, Y, Color):
        self.x = X
        self.y = Y
        self.color = Color
        
    def Update(self, KEY):
        if KEY == K_UP:
            self.y -= 10
        elif KEY == K_DOWN:
            self.y += 10
        elif KEY == K_LEFT:
            self.x -= 10
        elif KEY == K_RIGHT:
            self.x += 10
        else:
            pass
    def Draw(self):
        pygame.draw.rect(Screen.Display, self.color, (self.x, self.y, 10, 10), 0)

class food():
    def __init__(self, X, Y, Color):
        self.x = X
        self.y = Y
        self.color = Color
        
    def Collision(self):
        if Player.x == self.x and Player.y == self.y:
            self.x = random.randint(0, 59) * 10
            self.y = random.randint(0, 49) * 10
    def Draw(self):
        pygame.draw.rect(Screen.Display, self.color, (self.x, self.y, 10, 10), 0)



def Main():
    global Screen, Player, Food
    Screen = screen()
    Player = player(10, 10, (0, 255, 0))
    Food = food(100, 100, (255, 215, 0))
    try:
        XBOX = pygame.joystick.Joystick(0)
        XBOX.init()
    except:
        XBOX = None
    while True:
        if XBOX != None:
            Axis_0_value = '{:>6.3f}'.format(XBOX.get_axis(0))
            Axis_1_value = '{:>6.3f}'.format(XBOX.get_axis(1))
            if float(Axis_0_value) == -1:
                Player.x -= 10
            if float(Axis_0_value) == 1:
                Player.x += 10
            if float(Axis_1_value) == -1:
                Player.y -= 10
            if float(Axis_1_value) == 1:
                Player.y += 10
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                Player.Update(event.key)
                if event.key == K_ESCAPE:
                    Player.x = 10
                    Player.y = 10
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        Screen.Update()

if __name__ == "__main__":
    Main()
