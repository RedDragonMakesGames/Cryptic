from unittest import result
import pygame
import LevelManager
from pygame.locals import *
import sys

#Defines
XSIZE = 500
YSIZE = 800

#Function adapted from https://www.pygame.org/wiki/TextWrap to allow newline characters
# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            #If there's a newline character, go to a new line
            if(text[i] == '\n'):
                #Remove the character
                text = text[0 : i : ] + text[i + 1 : :]
                break
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text


class Framework:
    def __init__(self):
        #Set up drawing variables
        pygame.init()
        self.screen = pygame.display.set_mode((XSIZE, YSIZE))
        pygame.display.set_caption("Cryptic")

        self.clock = pygame.time.Clock()

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((10,10,10))
        if pygame.font:
            self.font = pygame.font.Font(None, 25)


        self.levelManager = LevelManager.LevelManager
        self.acceptingText = True

        #Variable for storing input from player
        self.inputText = ""
        self.text = ""

        #Variables for storing items for display
        self.promptText = ""
        self.resultText = ""
        #self.leftImage = nullcontext
        #self.rightImage = nullcontext
        #self.bottomImage = nullcontext

        self.step = 1
        self.running = True
        self.finished = False
        
        self.Run()

    def HandleInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
        
            if self.acceptingText:
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        if len(self.text)>0:
                            self.text = self.text[:-1]
                    elif event.key == K_RETURN:
                        self.inputText = self.text
                        self.HandleText()
                    else:
                        self.text += event.unicode
            else:
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.step += 1
                        self.resultText = ""
                        self.acceptingText = True
                        if self.step == 7:
                            self.running = False
                            self.step = 6
   
    def Draw(self):
        self.promptText = self.levelManager.GetPropmtText(self.step)

        #Clear screen
        self.screen.blit(self.background, (0,0))
        promptSpace = pygame.Rect(10,10, XSIZE - 20, 300)
        drawText(self.screen, self.promptText, (200,200,200), promptSpace, self.font, True)

        leftImg = self.levelManager.GetLeftImage(self.step)
        midImg = self.levelManager.GetMiddleImage(self.step)
        rightImg = self.levelManager.GetRightImage(self.step)

        self.screen.blit(leftImg, (50,320))
        self.screen.blit(midImg, (200,320))
        self.screen.blit(rightImg, (350,320))

        inputSpace = pygame.Rect(10, 450, XSIZE - 20, 30)
        drawText(self.screen, self.text, (255,10,10), inputSpace, self.font, True)

        resultSpace = pygame.Rect(10, 500, XSIZE - 20, 300)
        drawText(self.screen, self.resultText, (200,200,200), resultSpace, self.font, True)

        pygame.display.flip()
        

    def HandleText(self):
        self.text = ""
        nextStep, self.resultText = self.levelManager.GetResult(self.step, self.inputText)
        if nextStep:
            self.acceptingText = False
            if self.step == 6:
                self.finished = True

    def Run(self):
        while (self.running):
            self.HandleInput()
            self.Draw()
            self.clock.tick(60)

game = Framework()