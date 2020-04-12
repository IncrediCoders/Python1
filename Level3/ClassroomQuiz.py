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
wrongchoice1 = TRIVIA[2]
wrongchoice2 = TRIVIA[3]

ANSWER_CHOICES = [answer, wrongchoice1, wrongchoice2]

i = 0
number_of_questions = 8
questions_answered = 0
display_intro_screen() #Gets the screen ready.
running = False
while running == False: 
    #We're waiting for the player to click "Click here to start the game."
    EVENTS = pygame.event.get()
    for event in EVENTS:
        mpos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sample_click_rect.collidepoint(mpos):
                running = True
while running:
    display_question(question, ANSWER_CHOICES) #Displays the new question and the three answer choices.
    EVENTS = pygame.event.get()
    for event in EVENTS:
        mpos = pygame.mouse.get_pos() 
        if event.type == pygame.MOUSEBUTTONDOWN: #If the player clicks the mouse.
            if answer_1_rect.collidepoint(mpos): #If the player clicks the first answer on the top.
                if ANSWER_CHOICES[0] == answer: #If it's the correct answer.
                    screen.blit(correct_text,(300,0))
                    kodala = correct_a
                    screen.blit(kodala, (0,0))
                    pygame.display.update()
                    time.sleep(5)
                    if i >= (number_of_questions * 4)-4: #If it's the last question.
                        display_end_screen()
                        time.sleep(5)
                        running = False
                    else: #If it's the not the last question, we display the next question.
                        i = i+4
                        question = TRIVIA[i]
                        answer = TRIVIA[i+1]
                        wrong_choice_1 = TRIVIA[i+2]
                        wrong_choice_2 = TRIVIA[i+3]
                        ANSWER_CHOICES = [answer, wrong_choice_1, wrong_choice_2]
                        randomize_answers(ANSWER_CHOICES)
                else: #If it's an incorrect answer.
                    screen.blit(incorrect_text,(300,0))
                    kodala = incorrect_a
                    screen.blit(kodala, (0,0))
                    pygame.display.update()
                    time.sleep(5)
                    if i >= (number_of_questions * 4)-4: #If it's the last question.
                        display_end_screen()
                        time.sleep(5)
                        running = False
                    else: #If it's the not the last question, we display the next question.
                        i = i+4
                        question = TRIVIA[i]
                        answer = TRIVIA[i+1]
                        wrong_choice_1 = TRIVIA[i+2]
                        wrong_choice_2 = TRIVIA[i+3]
                        ANSWER_CHOICES = [answer, wrong_choice_1, wrong_choice_2]
                        randomize_answers(ANSWER_CHOICES)
#            if answer_2_rect.collidepoint(mpos): #If the player clicks the second answer.
#                if ANSWER_CHOICES[1] == answer: #If it's the correct answer.
#                    screen.blit(correct_text,(300,0))
#                    kodala = correct_b
#                    screen.blit(kodala, (0,0))
#                    pygame.display.update()
#                    time.sleep(5)
#                    if i >= (number_of_questions * 4)-4: #If it's the last question.
#                        display_end_screen()
#                        time.sleep(5)
#                        running = False
#                    else:
#                        i = i+4
#                        question = TRIVIA[i]
#                        answer = TRIVIA[i+1]
#                        wrong_choice_1 = TRIVIA[i+2]
#                        wrong_choice_2 = TRIVIA[i+3]
#                        ANSWER_CHOICES = [answer, wrong_choice_1, wrong_choice_2]
#                        randomize_answers(ANSWER_CHOICES)    
#                else: #If it's an incorrect answer.
#                    screen.blit(incorrect_text,(300,0))
#                    kodala = incorrect_b
#                    screen.blit(kodala,(0,0))
#                    pygame.display.update()
#                    time.sleep(5)
#                    if i >= (number_of_questions * 4)-4: #If it's the last question.
#                        display_end_screen()
#                        time.sleep(5)
#                        running = False
#                    else:
#                        i = i+4
#                        question = TRIVIA[i]
#                        answer = TRIVIA[i+1]
#                        wrong_choice_1 = TRIVIA[i+2]
#                        wrong_choice_2 = TRIVIA[i+3]
#                        ANSWER_CHOICES = [answer, wrong_choice_1, wrong_choice_2]
#                        randomize_answers(ANSWER_CHOICES)    
# 
# TODO:Write the code here for the third answer
