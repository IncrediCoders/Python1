from init import *

#We pull each line of text from the file into a list.
TRIVIA = []
file = open(get_file('Assets/trivia.txt'), 'r')
for line in file:
    TRIVIA.append(line.rstrip())

#We now have a list that holds our current question, correct answer,
#and the two wrong answers, in that order. We use these variables to 
#display the text on the screen.
question = TRIVIA[0]
answer = TRIVIA[1]
wrong_choice_1 = TRIVIA[2]
wrong_choice_2 = TRIVIA[3]

ANSWER_CHOICES = [answer, wrong_choice_1, wrong_choice_2]

line_number = 0
number_of_questions = 8
questions_answered = 0
display_intro_screen() #Gets the screen ready.
running = False
while running == False:
    #We're waiting for the player to click "Click here to start the game."
    if check_game_started() == True:
        running = True
while running:
    display_question(question, ANSWER_CHOICES) #Displays the new question and the three answer choices.
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == pygame.QUIT:
            running = False
        mouse_position = pygame.mouse.get_pos() 
        if event.type == pygame.MOUSEBUTTONDOWN: #If the player clicks the mouse.
            if answer_1_rect.collidepoint(mouse_position): #If the player clicks the first answer on the top.
                if ANSWER_CHOICES[0] == answer: #If it's the correct answer.
                    screen.blit(correct_text,(300,0))
                    codala = correct_a
                    screen.blit(codala, (0,0))
                    pygame.display.update()
                    time.sleep(5)
                    if line_number >= (number_of_questions * 4)-4: #If it's the last question.
                        display_end_screen()
                        time.sleep(5)
                        running = False
                    else: #If it's the not the last question, we display the next question.
                        line_number = line_number+4
                        question = TRIVIA[line_number]
                        answer = TRIVIA[line_number+1]
                        wrong_choice_1 = TRIVIA[line_number+2]
                        wrong_choice_2 = TRIVIA[line_number+3]
                        ANSWER_CHOICES = [answer, wrong_choice_1, wrong_choice_2]
                        randomize_answers(ANSWER_CHOICES)
                else: #If it's an incorrect answer.
                    screen.blit(incorrect_text,(300,0))
                    codala = incorrect_a
                    screen.blit(codala, (0,0))
                    pygame.display.update()
                    time.sleep(5)
                    if line_number >= (number_of_questions * 4)-4: #If it's the last question.
                        display_end_screen()
                        time.sleep(5)
                        running = False
                    else: #If it's the not the last question, we display the next question.
                        line_number = line_number+4
                        question = TRIVIA[line_number]
                        answer = TRIVIA[line_number+1]
                        wrong_choice_1 = TRIVIA[line_number+2]
                        wrong_choice_2 = TRIVIA[line_number+3]
                        ANSWER_CHOICES = [answer, wrong_choice_1, wrong_choice_2]
                        randomize_answers(ANSWER_CHOICES)
#            if answer_2_rect.collidepoint(mouse_position): #If the player clicks the second answer.
#                if ANSWER_CHOICES[1] == answer: #If it's the correct answer.
#                    screen.blit(correct_text,(300,0))
#                    codala = correct_b
#                    screen.blit(codala, (0,0))
#                    pygame.display.update()
#                    time.sleep(5)
#                    if line_number >= (number_of_questions * 4)-4: #If it's the last question.
#                        display_end_screen()
#                        time.sleep(5)
#                        running = False
#                    else: #If it's not the last question, we display the next question.
#                        line_number = line_number+4
#                        question = TRIVIA[line_number]
#                        answer = TRIVIA[line_number+1]
#                        wrong_choice_1 = TRIVIA[line_number+2]
#                        wrong_choice_2 = TRIVIA[line_number+3]
#                        ANSWER_CHOICES = [answer, wrong_choice_1, wrong_choice_2]
#                        randomize_answers(ANSWER_CHOICES)    
#                else: #If it's an incorrect answer.
#                    screen.blit(incorrect_text,(300,0))
#                    codala = incorrect_b
#                    screen.blit(codala,(0,0))
#                    pygame.display.update()
#                    time.sleep(5)
#                    if line_number >= (number_of_questions * 4)-4: #If it's the last question.
#                        display_end_screen()
#                        time.sleep(5)
#                        running = False
#                    else: #If it's not the last question, we display the next question.
#                        line_number = line_number+4
#                        question = TRIVIA[line_number]
#                        answer = TRIVIA[line_number+1]
#                        wrong_choice_1 = TRIVIA[line_number+2]
#                        wrong_choice_2 = TRIVIA[line_number+3]
#                        ANSWER_CHOICES = [answer, wrong_choice_1, wrong_choice_2]
#                        randomize_answers(ANSWER_CHOICES)    
# 
# TODO:Write the code here for the third answer.
