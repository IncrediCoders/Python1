# Runs the init.py file and imports the libraries
from init import *

def update_asteroids(delta_time):
    #TODO: Write code to update the position of the asteroids in the game window









# The Update method checks for all the key presses and button clicks
def update(delta_time):
    for event in pygame.event.get():
        # Checks if you click the Replay button to play again
        check_replay_click(event)
        # Checks if you closed the window
        if event.type == pygame.QUIT:
            stop()
        # Fires the two ships' weapons
        elif key_down(event, pygame.K_SPACE):
            pygame.mixer.music.load("Solutions/Level4/Challenges/Assets/LaserShoot1.wav")
            pygame.mixer.music.play()
            fire_bullet(1)
        elif key_down(event, pygame.K_RETURN):
            pygame.mixer.music.load("Solutions/Level4/Challenges/Assets/LaserShoot2.wav")
            pygame.mixer.music.play()
            fire_bullet(2)

    # Rotates the Player 1 ship
    if key_held_down(pygame.K_a):
        MY.player1.add_rotation(ship_rotate * delta_time)
    elif key_held_down(pygame.K_d):
        MY.player1.add_rotation(-ship_rotate * delta_time)

    # Moves the Player 1 ship forward and backward
    if key_held_down(pygame.K_w):
        MY.player1.add_velocity(MY.player1.rotation, ship_accel, ship_max_speed)
    elif key_held_down(pygame.K_s):
        MY.player1.add_velocity(MY.player1.rotation, -ship_accel, ship_max_speed)

    # Rotates the Player 2 ship
    if key_held_down(pygame.K_LEFT):
        MY.player2.add_rotation(ship_rotate * delta_time)
    elif key_held_down(pygame.K_RIGHT):
        MY.player2.add_rotation(-ship_rotate * delta_time)

    # Moves the Player 2 ship forward and backward
    if key_held_down(pygame.K_UP):
        MY.player2.add_velocity(MY.player2.rotation, ship_accel, ship_max_speed)
    elif key_held_down(pygame.K_DOWN):
        MY.player2.add_velocity(MY.player2.rotation, -ship_accel, ship_max_speed)

    # Updates player objects on screen
    update_players(delta_time)

    # Checks if bullets have been fired and updates their behavior on screen
    update_bullets(delta_time)

    #TODO: Call the method that updates the position of the asteroids in the game window


    # Check win condition
    check_win()


# Registering the states
Manager.register(sys.modules[__name__]) # The current file
Manager.register(GameOver)

# Run the game!
Manager.run(SCREEN, WINDOW, BLACK, "CHALLENGE2")
