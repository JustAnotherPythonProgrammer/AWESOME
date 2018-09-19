#!python3.2
#Imports and Initialization
import pygame, sys, random
from pygame.locals import *
pygame.init()






"""    Variables    """
#Window
Display = pygame.display.set_mode((700, 500))
pygame.display.set_caption('BLEH!')
#Colors
Black = (0, 0, 0)
Teal = (0, 255, 255)
Purple = (255, 0, 255)
Red = (255, 0, 0)
#Clock
Clock = pygame.time.Clock()
FPS = 300
#Text
Font1 = pygame.font.SysFont('Fixedsys Regular', 30, False, False)
Font2 = pygame.font.SysFont('Fixedsys Regular', 50, False, False)






"""    Functions    """
def Update():
    pygame.display.update()



def Collide(_GameOver):
    if not _GameOver:
        if SPRITE.X == WALL.X:
            if SPRITE.Y + 15 >= WALL.Y:
                return True
            else:
                SCORE.SCORE += 1
                SpeedUp()


                
def Jump():
    global FirstTime, JUMPING
    if FirstTime == True:
        if SPRITE.Y >= 400:
            SPRITE.Y -= 1
        else:
            FirstTime = False
    else:
        if SPRITE.Y < 475:
            SPRITE.Y += 1
        else:
            JUMPING = False
            FirstTime = True




def Duck():
    pass



def SpeedUp():
    global FPS
    FPS = (((SCORE.SCORE / 5) * 50) + 300)



def Game_Over(GAMEOVER):
    if GAMEOVER:
        Display.fill(Black)
        MESSAGE1 = Font2.render('Game Over',  True, Red, Black)
        MESSAGE2 = Font1.render('Score: ' + str(SCORE.SCORE), True, Red, Black)
        MESSAGE3 = Font1.render('Press Space to play again.', True, Red, Black)
        Display.blit(MESSAGE1, (250, 200))
        Display.blit(MESSAGE2, (300, 250))
        Display.blit(MESSAGE3, (215, 300))







        
"""    Classes    """
class DISPLAY():
    def __init__(self):
        self.BG_COLOR = Black
        self.FLOOR_COLOR = Teal
    def CREATE(self):
        pygame.draw.rect(Display, self.FLOOR_COLOR, (0, 490, 700, 10), 0)
        SPRITE.Draw()
        WALL.Draw()



        
class Wall():
    def __init__(self):
        self.COLOR = Teal
        self.HEIGHT = (random.randint(1, 5) * 10)
        self.X = 701
        self.Y = (490 - self.HEIGHT)
    def Draw(self):
        pygame.draw.rect(Display, self.COLOR, (self.X, self.Y, 10, self.HEIGHT), 0)




class Character():
    def __init__(self):
        self.COLOR = Purple
        self.X = 20
        self.Y = 475    
    def Draw(self):
        pygame.draw.rect(Display, self.COLOR, (self.X, self.Y, 15, 15), 0)



            
class Score():
    def __init__(self):
        self.COLOR = Teal
        self.SCORE = 0
    def Show(self):
        MESSAGE = 'Score: ' + str(self.SCORE)
        MESSAGE = Font1.render(MESSAGE, True, self.COLOR, Black)
        Display.blit(MESSAGE, (10, 10))
           









"""    MAIN    """
def Main():
    global SPRITE, WALL, SCORE, FirstTime, JUMPING, FPS
    SCREEN = DISPLAY()
    SPRITE = Character()
    WALL = Wall()
    SCORE = Score()
    JUMPING = False
    FirstTime = True
    GameOver = False
    while True:
        Display.fill(SCREEN.BG_COLOR)
        SCREEN.CREATE()
        SPRITE.Draw()
        SCORE.Show()
        Game_Over(GameOver)
        if WALL.X > -1:
            WALL.X -= 1
        else:
            WALL = Wall()
        if JUMPING == True:
            Jump()
        COLLISION = Collide(GameOver)
        if COLLISION == True:
            GameOver = True
            FinalScore = SCORE.SCORE
        for event in pygame.event.get():
            if JUMPING != True:
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        JUMPING = True
                        if GameOver == True:
                            SCORE.SCORE = 0
                            FPS = 300
                            GameOver = False
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        Update()
        Clock.tick(FPS)





if __name__ == "__main__":
    Main()
        
