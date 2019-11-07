"""Runs the Init.py file and imports the libraries"""
from init import *
import pygame
import sys

def update(delta_time):
    """The Update method checks for all the key presses and button clicks"""
    for event in pygame.event.get():
        #Checks if you click the Replay button to play again
        check_replay_click(event)
        #Checks if you closed the window
        if event.type == pygame.QUIT:
            stop()
        #Fires the two ships' weapons        
        elif key_down(event, pygame.K_SPACE):
            fire_bullet(1)
        elif key_down(event, pygame.K_RETURN):
            fire_bullet(2)           

    #Rotates the Player 1 ship
    if key_held_down(pygame.K_a):
        MY.player1.add_rotation(ship_rotate * delta_time)
    #TODO: Copy the code here for the Player 1 ship to rotate clockwise

    #Moves the Player 1 ship forward and backward
    if key_held_down(pygame.K_w):
        MY.player1.add_velocity(MY.player1.rotation, ship_accel, ship_max_speed)
    #TODO: Copy the code here for the Player 1 ship to move backward

    #Rotates the Player 2 ship
    #TODO: Write the code here to rotate the Player 2 ship

    #Moves the Player 2 ship forward and backward
    #TODO: Write the code here to move the Player 2 ship
    
    # Updates player objects on screen
    update_players(delta_time)

    # Checks if bullets have been fired and updates their behavior on screen
    update_bullets(delta_time)

    # Check win condition
    check_win()   


# states
Manager.register(sys.modules[__name__]) #The current file
Manager.register(GameOver)

# run the game!
Manager.run(SCREEN, WINDOW, BLACK)