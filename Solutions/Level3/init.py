#============================================================
#PART 1: IMPORTING DEPENDENCIES AND ASSIGNING GLOBAL VARIABLES
import pygame
import random
import time
from os import path

#============================================================
#PART 2: CREATING A FRAMEWORK OF GENERAL CLASSES AND FUNCTIONS

def get_file(fileName):
    """
    Returns the absolute path of a file
    """
    #This grabs your files from your folder
    return path.join(path.dirname(__file__), fileName)

def read_file(fileName):
    """
    Read txt file into a list line by line and return it
    """
    TRIVIA = []
    #This puts the txt file into the file variable
    file = open(get_file(fileName), 'r')
    for line in file:
        TRIVIA.append(line.rstrip())
    return TRIVIA

#============================================================
#PART 3: SETUP FOR THE CLASSROOM QUIZ GAME

"""
Initialize Font Objects
"""
#We pick our text style and size
pygame.init()
pygame.display.set_caption('Classroom Quiz') #To add the title of game
my_font = pygame.font.SysFont('Arial', 35) #Change to 'Arial.ttf' if used for making exe file by Pyinstaller
answer_1_text = my_font.render("                        ", True, (0,0,255))
answer_1_rect = answer_1_text.get_rect(topleft=(200,230))
answer_2_text = my_font.render("                         ", True, (0,0,255))
answer_2_rect = answer_2_text.get_rect(topleft=(200,300))
answer_3_text = my_font.render("                         ", True, (0,0,255))
answer_3_rect = answer_3_text.get_rect(topleft=(200,370))
start_click = my_font.render("Click here to start the game.", True, (0,0,255))
start_click_rect = start_click.get_rect(topleft=(200,230))
correct_text = my_font.render("That is correct.", True, (0,128,0))
incorrect_text = my_font.render("That is incorrect.", True, (255,0,0))

"""
Set Window Size
"""
#We set the window size for our game
width = 960
height = 540
screen = pygame.display.set_mode((width,height))

"""
Load Sprites
"""
#We load the images and put them in variables
background = pygame.image.load(get_file('Assets/Background.png'))
correct_a = pygame.image.load(get_file('Assets/CorrectAnswerA.png'))
correct_b = pygame.image.load(get_file('Assets/CorrectAnswerB.png'))
incorrect_a = pygame.image.load(get_file('Assets/IncorrectAnswerA.png'))
incorrect_b = pygame.image.load(get_file('Assets/IncorrectAnswerB.png'))
end_game = pygame.image.load(get_file('Assets/EndGame.png'))

def randomize_answers(input_list):
    #This randomly shuffles the answers so the player doesn't know which one is the correct answer
    random.shuffle(input_list)
    return input_list

def display_question(question, input_list):
    #This code loads and displays the next question and Mrs. Codala's reaction
    question_text = my_font.render(question, True, (0, 0, 0))
    question_rect = question_text.get_rect(topleft=(200,150))
    answer_1_text = my_font.render(input_list[0], True, (0,0,255))
    answer_1_rect = answer_1_text.get_rect(topleft=(200,230))
    answer_2_text = my_font.render(input_list[1], True, (0,0,255))
    answer_2_rect = answer_2_text.get_rect(topleft=(200,300))
    answer_3_text = my_font.render(input_list[2], True, (0,0,255))
    answer_3_rect = answer_3_text.get_rect(topleft=(200,370))
    screen.blit(background, (0,0))
    screen.blit(question_text, question_rect)
    screen.blit(answer_1_text, answer_1_rect)
    screen.blit(answer_2_text, answer_2_rect)
    screen.blit(answer_3_text, answer_3_rect)
    pygame.display.update()

def display_intro_screen():
    #This displays the intro screen until the player clicks the Close button or starts the game
    intro_text = my_font.render("Welcome to the Trivia Game!", True, (0,0,0))
    start_click = my_font.render("Click here to start.", True, (0,0,255))
    start_click_rect = start_click.get_rect(topleft=(200,230))
    screen.blit(background,(0,0))
    screen.blit(intro_text, (200,150))
    screen.blit(start_click,start_click_rect)
    pygame.display.update()
    intro = True 
    while intro:
        EVENTS = pygame.event.get() 
        for event in EVENTS:
            quit_game(event) #If the player clicks the Close button, it exits the game
        #If the player clicks "Click here to start the game.", the screen changes to the first question
        if check_game_started() == True:
            intro = False

def display_end_screen():
    #This shows the image of Mrs. Codala telling you the game is done
    codala = end_game
    screen.blit(background, (0,0))
    screen.blit(codala,(0,0))
    pygame.display.update()
    pygame.event.get()

def check_game_started():
    #This checks if the player clicks the text to start the game
    EVENTS = pygame.event.get()
    for event in EVENTS:
        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_click_rect.collidepoint(mouse_position):
                return True
    return False

def display_codala(input_image, text_type):
    #This displays the image of Mrs. Codala telling you if the choice is correct
    if text_type == "correct_text":
        screen.blit(correct_text,(300,0))
    if text_type == "incorrect_text":
        screen.blit(incorrect_text,(300,0))
    codala = input_image
    screen.blit(codala, (0,0))
    pygame.display.update()
    pygame.event.get()  #To fix display of image above for Mac
    time.sleep(3)

def move_to_next_question(input_list, question, line_number, input_list2):
    #This changes question and three choices from input list to next set of question and choices
    line_number = line_number+4
    question = input_list[line_number] #input_list is the content from txt file
    answer = input_list[line_number+1]
    wrong_choice_1 = input_list[line_number+2]
    wrong_choice_2 = input_list[line_number+3]
    input_list2 = [answer, wrong_choice_1, wrong_choice_2] #input_list2 is the new answer choices for display
    randomize_answers(input_list2)
    #Return new line number, next question, correct answer and answer choice list
    return line_number, question, answer, input_list2

def check_if_last_question(line_number, running_status, number_of_questions):
    #This checks if it's the last question and displays end screen if so
    if line_number >= (number_of_questions * 4)-4:
        display_end_screen()
        time.sleep(5)
        running_status = False
    return running_status

def quit_game(event):
    #This exits the game if the player clicks the Close button
    if event.type == pygame.QUIT: 
        pygame.quit()
        exit()
        