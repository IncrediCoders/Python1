#============================================================
#PART 1: IMPORTING DEPENDENCIES AND ASSIGNING GLOBAL VARIABLES
import pygame
import random
import time
from os import path

#============================================================
#PART 2: CREATING A FRAMEWORK OF GENERAL CLASSES AND FUNCTIONS

def get_file(fileName):
    """Returns the absolute path of a file."""
    #This grabs your files from your folder.
    return path.join(path.dirname(__file__), fileName)

def read_file(fileName):
    """Read txt file into a list line by line and return it."""
    TRIVIA = []
    #This puts the txt file into the file variable
    file = open(get_file(fileName), 'r')
    for line in file:
        TRIVIA.append(line.rstrip())
    return TRIVIA

#============================================================
#PART 3: SETUP FOR THE CLASSROOM QUIZ GAME

"""Initialize Font Objects"""
#We pick our text style and size.
pygame.init()
myfont = pygame.font.SysFont('Arial', 35)
answer_1_text = myfont.render("                        ", True, (0, 0, 0))
answer_1_rect = answer_1_text.get_rect(topleft=(200,230))
answer_2_text = myfont.render("                         ", True, (0, 0, 0))
answer_2_rect = answer_2_text.get_rect(topleft=(200,300))
answer_3_text = myfont.render("                         ", True, (0, 0, 0))
answer_3_rect = answer_3_text.get_rect(topleft=(200,370))
start_click = myfont.render("Click here to start the game.", True, (0,0,0))
start_click_rect = start_click.get_rect(topleft=(200,230))
correct_text = myfont.render("That is correct.", True, (0,128,0))
incorrect_text = myfont.render("That is incorrect.", True, (255,0,0))

"""Set Window Size"""
#We set the window size for our game.
width = 960
height = 540
screen = pygame.display.set_mode((width,height))

"""Load Sprites"""
#We load the images and put them in variables.
background = pygame.image.load(get_file('Assets/Background.png'))
correct_a = pygame.image.load(get_file('Assets/CorrectAnswerA.png'))
correct_b = pygame.image.load(get_file('Assets/CorrectAnswerB.png'))
incorrect_a = pygame.image.load(get_file('Assets/IncorrectAnswerA.png'))
incorrect_b = pygame.image.load(get_file('Assets/IncorrectAnswerB.png'))
end_game = pygame.image.load(get_file('Assets/EndGame.png'))

def randomize_answers(answerChoices):
    #This randomly shuffles the answers so the player doesn't know which one is the correct answer.
    random.shuffle(answerChoices)
    return answerChoices

def display_question(question, answer_choices):
    #This code loads and displays the next question and Mrs. Codala's reaction.
    question_text = myfont.render(question, True, (0, 0, 0))
    question_rect = question_text.get_rect(topleft=(200,150))
    answer_1_text = myfont.render(answer_choices[0], True, (0, 0, 0))
    answer_1_rect = answer_1_text.get_rect(topleft=(200,230))
    answer_2_text = myfont.render(answer_choices[1], True, (0, 0, 0))
    answer_2_rect = answer_2_text.get_rect(topleft=(200,300))
    answer_3_text = myfont.render(answer_choices[2], True, (0, 0, 0))
    answer_3_rect = answer_3_text.get_rect(topleft=(200,370))
    screen.blit(background, (0,0))
    screen.blit(question_text, question_rect)
    screen.blit(answer_1_text, answer_1_rect)
    screen.blit(answer_2_text, answer_2_rect)
    screen.blit(answer_3_text, answer_3_rect)
    pygame.display.update()

def display_intro_screen():
    #This shows the intro text (so we only run it once, at the beginning).
    intro_text = myfont.render("Welcome to the Trivia Game!", True, (0,0,0))
    start_click = myfont.render("Click here to start.", True, (0,0,0))
    start_click_rect = start_click.get_rect(topleft=(200,230))
    screen.blit(background,(0,0))
    screen.blit(intro_text, (200,150))
    screen.blit(start_click,start_click_rect)
    pygame.display.update()

def display_end_screen():
    #This shows the image of Mrs. Codala telling you the game is done.
    codala = end_game
    screen.blit(background, (0,0))
    screen.blit(codala,(0,0))
    pygame.display.update()

def check_game_started():
    EVENTS = pygame.event.get()
    for event in EVENTS:
        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_click_rect.collidepoint(mouse_position):
                return True
    return False

