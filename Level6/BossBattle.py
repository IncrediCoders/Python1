#Runs the init.py file and imports the libraries
from init import *

def update(delta_time):
    # Checks if player collides with the walls
    if MY.player.location.x < MY.wall_height:
        MY.player.location.x = MY.wall_height
    #TODO: Uncomment Lines 9-10 to make sure that Paul doesn't walk through the wall on the right side of the screen
    #if MY.player.location.x > WINDOW_WIDTH - MY.wall_height:
    #    MY.player.location.x = WINDOW_WIDTH - MY.wall_height
    #TODO: Uncomment Lines 12-13 to make sure that Paul doesn't walk through the wall on the top of the screen
    #if MY.player.location.y < MY.wall_height:
    #    MY.player.location.y = MY.wall_height
    #TODO: Copy the code here to make sure that Paul doesn't walk through the wall on the bottom of the screen



    handle_pillar_collision()

    #TODO: Copy the code here for Paul to lose health if he collides with the Creeper





    #Adds the hit box above Paul
    if MY.player_dir == UP:
        MY.player_hitbox.location = pygame.math.Vector2(
            MY.player.location.x + 20, MY.player.location.y - 20)
    #TODO: Copy the code here to add the hit box below Paul



    #TODO: Copy the code here to add the hit box to the left of Paul



    #TODO: Write the code here to add the hit box to the right of Paul




    #TODO: Copy the code here to reduce Creeper's health when he gets attacked




    player_attack_update()

    update_assets(delta_time)
    
    check_win()

    check_events()

# Register the game states
Manager.register(sys.modules[__name__]) #The current file
Manager.register(GameOver)
Manager.register(PlayAgain)

# Run the game
Manager.run(SCREEN, WINDOW, BLACK)
