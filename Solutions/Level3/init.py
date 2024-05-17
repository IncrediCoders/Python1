#============================================================
#PART 1: IMPORTING DEPENDENCIES AND ASSIGNING GLOBAL VARIABLES
import sys
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
    # This grabs your files from your folder
    return path.join(path.dirname(__file__), fileName)

def read_file(fileName):
    """
    Reads txt file into a list line by line and return it
    """
    TRIVIA = []
    # This puts the txt file into the file variable
    file = open(get_file(fileName), 'r')
    for line in file:
        TRIVIA.append(line.rstrip())
    return TRIVIA

#============================================================
#PART 3: SETUP FOR THE CLASSROOM QUIZ GAME
"""
Draws border around our answer rects so user can see exactly where to click
"""
def draw_border(rect):
    border_width = 2
    padding = 10
    pygame.draw.rect(screen, pygame.Color("Purple4"), (rect.left - padding/2, rect.top - padding/2, 600, rect.height + padding), width = border_width, border_radius = 0,border_top_left_radius=3, border_top_right_radius=3, border_bottom_left_radius=3, border_bottom_right_radius=3)
"""
Initializes Font Objects
"""
# Picks our text style and size
pygame.init()
pygame.display.set_caption('Classroom Quiz') # Adds the title of game
my_font = pygame.font.SysFont('Arial', 35)

answer_1_text = my_font.render("                        ", True, (0,0,255))
answer_1_rect = answer_1_text.get_rect(topleft=(200,230))
answer_1_rect.width = 600
answer_2_text = my_font.render("                         ", True, (0,0,255))
answer_2_rect = answer_2_text.get_rect(topleft=(200,300))
answer_2_rect.width = 600
answer_3_text = my_font.render("                         ", True, (0,0,255))
answer_3_rect = answer_3_text.get_rect(topleft=(200,370))
answer_3_rect.width = 600
start_click = my_font.render("Click here to start the game.", True, (0,0,255))
start_click_rect = start_click.get_rect(topleft=(200,230))
start_click_rect.width = 400
correct_text = my_font.render("That is correct.", True, (0,128,0))
incorrect_text = my_font.render("That is incorrect.", True, (255,0,0))

"""
Sets Window Size
"""
# Sets the window size for our game
width = 960
height = 540
screen = pygame.display.set_mode((width,height))

"""
Loads the sprites
"""
# Loads the images and puts them in the variables
background = pygame.image.load(get_file('Assets/Background.png'))
correct_a = pygame.image.load(get_file('Assets/CorrectAnswerA.png'))
correct_b = pygame.image.load(get_file('Assets/CorrectAnswerB.png'))
incorrect_a = pygame.image.load(get_file('Assets/IncorrectAnswerA.png'))
incorrect_b = pygame.image.load(get_file('Assets/IncorrectAnswerB.png'))
end_game = pygame.image.load(get_file('Assets/EndGame.png'))

def randomize_answers(input_list):
    """
    Randomizes the answer choices
    """
    # Randomly shuffles the answers so the player doesn't know which one is the correct answer
    random.shuffle(input_list)
    return input_list

def display_question(question, input_list):
    """
    Loads the questions and the answers
    """
    question_wrap =""
    wrapped = False
    #Wrap text for these questions
    question_wrap = ""
    wrapped = False
    #Wrap text for these questions
    if(question == "What is SB Turtle's favorite programming language?"):
        question = "What is SB Turtle's favorite programming"
        question_wrap = "language?"
        wrapped = True
    elif(question == "According to SideWinder, who has good taste?"):
        question = "According to SideWinder, who has good"
        question_wrap = "taste?"
        wrapped = True
    elif(question == "Who is one of Java Lynn's favorite actors?"):
        question = "Who is one of Java Lynn's favorite"
        question_wrap = "actors?"
        wrapped = True
    elif(question == "Who is one of Jitter Bug's favorite actors?"):
        question = "Who is one of Jitter Bug's favorite"
        question_wrap = "actors?"
        wrapped = True
    elif(question == "What is Quackintosh's favorite art called?"):
        question = "What is Quackintosh's favorite art"
        question_wrap = "called?"
        wrapped = True

    # Loads and displays the new question and the according answer choices
    question_text = my_font.render(question, True, (0, 0, 0))
    if wrapped:
        question_rect = question_text.get_rect(topleft=(200,130))
    else:
        question_rect = question_text.get_rect(topleft=(200,150))
    question_text_wrap = my_font.render(question_wrap, True, (0, 0, 0))
    question_wrap_rect = question_text_wrap.get_rect(topleft=(200,165))
    
    answer_1_text = my_font.render(input_list[0], True, (0,0,255))
    answer_1_rect = answer_1_text.get_rect(topleft=(200,230))

    
    answer_2_text = my_font.render(input_list[1], True, (0,0,255))
    answer_2_rect = answer_2_text.get_rect(topleft=(200,300))

    answer_3_text = my_font.render(input_list[2], True, (0,0,255))
    answer_3_rect = answer_3_text.get_rect(topleft=(200,370))


    screen.blit(background, (0,0))
    screen.blit(question_text, question_rect)
    screen.blit(question_text_wrap, question_wrap_rect)
    screen.blit(answer_1_text, answer_1_rect)
    draw_border(answer_1_rect)
    screen.blit(answer_2_text, answer_2_rect)
    draw_border(answer_2_rect)
    screen.blit(answer_3_text, answer_3_rect)
    draw_border(answer_3_rect)
    pygame.display.update()

def display_intro_screen():
    """
    Loads the intro screen
    """
    # Displays the intro screen until the player clicks the Close button or starts the game
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
            quit_game(event) # If the player clicks the Close button, it exits the game
        # If the player clicks "Click here to start the game.", the screen changes to the first question
        if check_game_started():
            intro = False

def display_challenge1_end_screen():
    codala = end_game
    screen.blit(background, (0,0))
    screen.blit(codala,(0,0))
    pygame.display.update()
    pygame.event.get()
    time.sleep(3)

def display_end_screen():
    """
    Loads the end screen
    """
    # Shows the image of Mrs. Codala telling you the game is done
    codala = end_game
    screen.blit(background, (0,0))
    screen.blit(codala,(0,0))
    pygame.display.update()
    pygame.event.get()
    running = True
    while running:
        EVENTS = pygame.event.get()
        for event in EVENTS:
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

def check_game_started():
    """
    Checks if the player clicks the text to start the game
    """
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == pygame.MOUSEBUTTONDOWN:
                return True
    return False

def display_codala(input_image, text_type):
    """
    Displays the image of Mrs. Codala telling you if the choice is correct
    """
    if text_type == "correct_text":
        screen.blit(correct_text,(300,0))
    if text_type == "incorrect_text":
        screen.blit(incorrect_text,(300,0))
    codala = input_image
    screen.blit(codala, (0,0))
    pygame.display.update()
    pygame.event.get()  # To fix display of image above for Mac
    time.sleep(3)

def move_to_next_question(input_list, question, line_number, input_list2):
    """
    Changes the current set of question and choices from input list to the next set
    """
    line_number = line_number+4
    question = input_list[line_number] # input_list is the content from txt file
    answer = input_list[line_number+1]
    wrong_choice_1 = input_list[line_number+2]
    wrong_choice_2 = input_list[line_number+3]
    input_list2 = [answer, wrong_choice_1, wrong_choice_2] # input_list2 is the new answer choices for display
    randomize_answers(input_list2)
    # Return new line number, next question, correct answer and answer choice list
    return line_number, question, answer, input_list2

def check_if_last_question(line_number, running_status, number_of_questions):
    """
    Checks if it's the last question and displays end screen if so
    """
    if line_number >= (number_of_questions * 4)-4:
        running_status = False
    return running_status

def quit_game(event):
    """
    Exits the game if the player clicks the Close button
    """
    if event.type == pygame.QUIT:
        sys.exit()
        