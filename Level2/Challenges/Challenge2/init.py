#============================================================
#PART 1: IMPORTING DEPENDENCIES AND ASSIGNING GLOBAL VARIABLES
from os import path
import pygame # Gives us our gaming functions
import textwrap

#============================================================
#PART 2: CREATING A FRAMEWORK OF GENERAL CLASSES AND METHODS

def load_file(fileName):
    """
    Returns the absolute path of a file
    """
    # This grabs the image files from your folder
    return pygame.image.load(path.join(path.dirname(__file__), fileName))

def display_text(screen, current_text):
    """
    Displays text to the screen
    """
    WRAPPED_TEXT = textwrap.wrap(current_text, 30)
    y = 230
    for i in range(len(WRAPPED_TEXT)):
        screen.blit(my_font.render(WRAPPED_TEXT[i], True, (0, 0, 0)), (230,y))
        y = y + 30

#============================================================
#PART 3: SETUP FOR THE CLASS INTRODUCTIONS GAME

"""
Initializes pygame, the font object, and the window's title
"""
pygame.init() # Initializes all the imported pygame modules
my_font = pygame.font.SysFont('Arial', 20) # Creates a font object from the system fonts
pygame.display.set_caption('Class Introductions') # Adds the title of the game

"""
Sets up the screen
"""
width = 600
height = 800
screen = pygame.display.set_mode((width,height))
running = True

def display(background, current_text, current_character):
    """
    Displays a character to the screen
    """
    screen.blit(background,(0,0))
    screen.blit(current_character, (0,0))
    display_text(screen, current_text)
    pygame.display.flip()
