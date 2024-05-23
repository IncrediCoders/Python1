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

display_intro_screen() # Displays the intro screen

running = True 

# This displays the question screen until the last question or until the player closes the window
while running:
    display_question(question, ANSWER_CHOICES) # Displays the new question and the three answer choices
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == pygame.QUIT: # If the player clicks the Close button, it exits the game
            running = False
        mouse_position = pygame.mouse.get_pos() 
        if event.type == pygame.MOUSEBUTTONDOWN: # If the player clicks the mouse
            # Check to see if player has clicked on one of the possible answers
            if answer_1_rect.collidepoint(mouse_position) or answer_2_rect.collidepoint(mouse_position) or answer_3_rect.collidepoint(mouse_position):     
                if answer_1_rect.collidepoint(mouse_position): # If the player clicks the 1st answer on the top
                    if ANSWER_CHOICES[0] == answer: # If it's the correct answer
                        display_codala(correct_a, "correct_text") # Displays Mrs. Codala and the text for the correct answer
                    # Uncommented these two lines to display Mrs. Codala if the answer is incorrect
                    else: # If it's an incorrect answer
                        display_codala(incorrect_a, "incorrect_text") # Displays Mrs. Codala and the text for an incorrect answer
                
                # Copied the code here for the second answer
                if answer_2_rect.collidepoint(mouse_position): # If the player clicks the 2nd answer
                    if ANSWER_CHOICES[1] == answer: 
                        display_codala(correct_b, "correct_text")
                    else:
                        display_codala(incorrect_b, "incorrect_text")

                # Wrote the code here for the third answer
                if answer_3_rect.collidepoint(mouse_position): # If the player clicks the 3rd answer
                    if ANSWER_CHOICES[2] == answer: 
                        display_codala(correct_a, "correct_text")
                    else:
                        display_codala(incorrect_a, "incorrect_text")
                # We display the next question after an incorrect or correct answer has been chosen
                line_number, question, answer, ANSWER_CHOICES = move_to_next_question(TRIVIA, question, line_number, ANSWER_CHOICES)
            # If it's the last question, we display the end screen with Mrs. Codala
            running = check_if_last_question(line_number, running, number_of_questions)
            
            
                
display_end_screen()
