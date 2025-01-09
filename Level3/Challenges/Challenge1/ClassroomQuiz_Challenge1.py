from init import *

# We pull each line of text from the file into a list
TRIVIA = read_file('Assets/Trivia.txt')

# We now have a list that holds our current question, correct answer, and the two wrong choices, in that order
# We use these variables to display the text on the screen
question = TRIVIA[0]
answer = TRIVIA[1]
wrong_choice_1 = TRIVIA[2]
wrong_choice_2 = TRIVIA[3]

ANSWER_CHOICES = [answer, wrong_choice_1, wrong_choice_2]
randomize_answers(ANSWER_CHOICES) # Shuffles the first set of answer choices

line_number = 0
number_of_questions = 12
#TODO: Uncomment this line to add the variable of score
#score = 0 #Starts the score at zero

display_intro_screen() # Displays the intro screen

running = True

# This displays the question screen until the last question or until the player closes the window
while running:
    display_question(question, ANSWER_CHOICES) # Displays the new question and the three answer choices
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == pygame.QUIT: # If clicks the close button, it exits the game
            running = False
        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN: # If the player clicks the mouse
             # Check to see if player has clicked on one of the possible answers
            if answer_1_rect.collidepoint(mouse_position) or answer_2_rect.collidepoint(mouse_position) or answer_3_rect.collidepoint(mouse_position):
                if answer_1_rect.collidepoint(mouse_position): # If the player clicks the 1st answer on the top
                    if ANSWER_CHOICES[0] == answer: # If it's the correct answer
                        #TODO: Uncomment this line to add 1 score
                        #score += 1 #The player gets one score
                        display_codala(correct_a, "correct_text") # Displays codala and text for correct answer
                    else: # If it's an incorrect answer
                        display_codala(incorrect_a, "incorrect_text") # Display codala and text for incorrect answer
                if answer_2_rect.collidepoint(mouse_position): # If the player clicks the 2nd answer
                    if ANSWER_CHOICES[1] == answer:
                        #TODO: Add 1 score

                        display_codala(correct_b, "correct_text")
                    else:
                        display_codala(incorrect_b, "incorrect_text")
                if answer_3_rect.collidepoint(mouse_position): # If the player clicks the 3rd answer
                    if ANSWER_CHOICES[2] == answer:
                        #TODO: Add 1 score

                        display_codala(correct_a, "correct_text")
                    else:
                        display_codala(incorrect_a, "incorrect_text")

                #TODO: Check if it's the last question and display end screen with scores
                # Modified from the check_if_last_question function in init.py
            
            
                    # Display the final score on the end screen
            
            
            
            
            
            
            
            
            
            
            
            # We display the next question after an incorrect or correct answer has been chosen
            line_number, question, answer, ANSWER_CHOICES = move_to_next_question(TRIVIA, question, line_number, ANSWER_CHOICES)
            # If it's the last question, we display the end screen with Mrs. Codala
            if not running:
                display_end_screen()
