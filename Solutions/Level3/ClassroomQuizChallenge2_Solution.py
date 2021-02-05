from init import *

#We pull each line of text from the file into a list
TRIVIA = read_file('Assets/Trivia.txt')

#We create a list of variables that holds the text for our current question, the correct answer, and
#the two wrong choices, in that order. We use this list to display text on the screen
question = TRIVIA[0]
answer = TRIVIA[1]
wrong_choice_1 = TRIVIA[2]
wrong_choice_2 = TRIVIA[3]

ANSWER_CHOICES = [answer, wrong_choice_1, wrong_choice_2]
randomize_answers(ANSWER_CHOICES) #Shuffles the first set of answer choices

line_number = 0
number_of_questions = 12

display_intro_screen() #Displays the intro screen

running = True 

#This displays question screen until the last question or the player closes the window
while running:
    display_question(question, ANSWER_CHOICES) #Displays the new question and the three answer choices
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == pygame.QUIT: #If the player clicks the Close button, it exits the game
            running = False
        mouse_position = pygame.mouse.get_pos() 
        if event.type == pygame.MOUSEBUTTONDOWN: #If the player clicks the mouse
            if answer_1_rect.collidepoint(mouse_position): #If the player clicks the 1st answer on the top
                if ANSWER_CHOICES[0] == answer: #If it's the correct answer
                    #Uncommented these lines to add an interactive effect
                    #Changes the text color from blue to green
                    answer_1_text = my_font.render(answer, True, (0,128,0))
                    screen.blit(answer_1_text, answer_1_rect)
                    pygame.display.update()
                    pygame.event.get()
                    time.sleep(1)
                    display_codala(correct_a, "correct_text") #Displays Mrs. Codala and the text for a correct answer
                else: #If it's an incorrect answer
                    #Added an interactive effect to the text
                    #Changes the text color from blue to red
                    answer_1_text = my_font.render(ANSWER_CHOICES[0], True, (255,0,0))
                    screen.blit(answer_1_text, answer_1_rect)
                    pygame.display.update()
                    pygame.event.get()
                    time.sleep(1)
                    display_codala(incorrect_a, "incorrect_text") #Display Mrs. Codala and the text for an incorrect answer
            if answer_2_rect.collidepoint(mouse_position): #If the player clicks the 2nd answer
                if ANSWER_CHOICES[1] == answer: 
                    #Added an interactive effect to the text
                    #Changes the text color from blue to green
                    answer_2_text = my_font.render(answer, True, (0,128,0))
                    screen.blit(answer_2_text, answer_2_rect)
                    pygame.display.update()
                    pygame.event.get()
                    time.sleep(1)
                    display_codala(correct_b, "correct_text")
                else:
                    #Added an interactive effect to the text
                    #Changes the text color from blue to red
                    answer_2_text = my_font.render(ANSWER_CHOICES[1], True, (255,0,0))
                    screen.blit(answer_2_text, answer_2_rect)
                    pygame.display.update()
                    pygame.event.get()
                    time.sleep(1)
                    display_codala(incorrect_b, "incorrect_text")
            if answer_3_rect.collidepoint(mouse_position): #If the player clicks the 3rd answer
                if ANSWER_CHOICES[2] == answer: 
                    #Added an interactive effect to the text
                    #Changes the text color from blue to green
                    answer_3_text = my_font.render(answer, True, (0,128,0))
                    screen.blit(answer_3_text, answer_3_rect)
                    pygame.display.update()
                    pygame.event.get()
                    time.sleep(1)
                    display_codala(correct_a, "correct_text")
                else:
                    #Added an interactive effect to the text
                    #Changes the text color from blue to red
                    answer_3_text = my_font.render(ANSWER_CHOICES[2], True, (255,0,0))
                    screen.blit(answer_3_text, answer_3_rect)
                    pygame.display.update()
                    pygame.event.get()
                    time.sleep(1)
                    display_codala(incorrect_a, "incorrect_text")

            #Checks if it's the last question, and then displays the end screen
            running = check_if_last_question(line_number, running, number_of_questions)
            #If it's the not the last question, we display the next question
            line_number, question, answer, ANSWER_CHOICES = move_to_next_question(TRIVIA, question, line_number, ANSWER_CHOICES)
pygame.quit()
