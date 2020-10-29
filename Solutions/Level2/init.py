#============================================================
#PART 1: IMPORTING DEPENDENCIES AND ASSIGNING GLOBAL VARIABLES
from os import path
import pygame # Gives us our gaming functions
import textwrap

#============================================================
#PART 2: CREATING A FRAMEWORK OF GENERAL CLASSES AND FUNCTIONS

def load_file(fileName):
    """Returns the absolute path of a file"""
    #This grabs the image files from your folder.
    return pygame.image.load(path.join(path.dirname(__file__), fileName))

def display_text(screen, current_text):
    """Displays text to the screen"""
    WRAPPED_TEXT = textwrap.wrap(current_text, 30)
    y = 230
    for i in range(len(WRAPPED_TEXT)):
        screen.blit(myfont.render(WRAPPED_TEXT[i], True, (0, 0, 0)), (230,y))
        y = y + 30

#============================================================
#PART 3: SETUP FOR THE CLASS INTRODUCTIONS GAME

"""Initialize Font Object"""
#We pick our text style and size.
pygame.init()
myfont = pygame.font.SysFont('Arial', 20) #Change to 'Arial.ttf' if used for making exe file by Pyinstaller

"""Displays character to the screen"""
width = 600
height = 800
screen = pygame.display.set_mode((width,height))
running = True

def display(background, current_text, current_character):
    screen.blit(background,(0,0))
    screen.blit(current_character, (0,0))
    display_text(screen, current_text)
    pygame.display.flip()
