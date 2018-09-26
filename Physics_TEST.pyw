#! python3.2
import pygame, sys
from pygame.locals import *
pygame.init()


class simulation():
    def __init__(self):
        pass
    def Terminate(self):
        pygame.quit()
        sys.exit()

        
class screen():
    def __init__(self):
        self.Display = pygame.display.set_mode((400, 400))
        pygame.display.set_caption('Physics')

    def Update(self, VALUE):
        self.Display.fill((0, 0, 0))
        if VALUE:
            Ball.Update()
        else:
            Ball.Draw()
        Clock.tick(FPS)
        pygame.display.update()
        

class ball():
    def __init__(self, radius, velocity, gravity, falling_increase, Y):
        self.Radius = radius
        self.START_Velocity = velocity
        self.Velocity = velocity
        self.Gravity = gravity
        self.y = Y
        self.FallingIncrease = falling_increase
        self.Falling = 1

    def Draw(self):
        pygame.draw.circle(Screen.Display, (0, 255, 255), (200, int(self.y)), self.Radius, 0)
        
    def Update(self):
        self.y -= self.Velocity
        self.Velocity *= self.Gravity
        self.y += self.START_Velocity - self.Velocity + self.Falling
        self.Falling *= self.FallingIncrease
        print(self.Falling)
        self.Draw()
        if self.y >= 375:
            self.Velocity = 0
            self.y = 375 - self.START_Velocity
            self.Falling = 0
            Jump = False

        
def Main():
    global Simulation, Screen, Ball, Clock, FPS, Jump
    Simulation = simulation()
    Screen = screen()
    Ball = ball(25, 10, 0.98, 1.03, 375)
    Clock = pygame.time.Clock()
    FPS = 60
    Jump = False
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    Jump = True
                    Ball.Velocity = 10
                    Ball.Falling = 1
            if event.type == QUIT:
                Simulation.Terminate()
        Screen.Update(Jump)


if __name__ == "__main__":
    Main()
