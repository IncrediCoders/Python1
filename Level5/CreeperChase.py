# Runs the init.py file and imports the libraries
from init import *

# Checks for player input and updates the game
def update(delta_time):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        elif key_down(event, " ") and (MY.grounded or MY.level_num > 3):
            MY.player.velocity.y = -700
            MY.grounded = False
            jetpack_up_animation()
    if key_held_down(pygame.K_LEFT): 
        #TODO: Uncomment the two lines below
        #MY.player.velocity.x = max(MY.player.velocity.x - PLAYER_ACCEL, -PLAYER_MAX_SPEED)
        #MY.player.sprite = MY.paul_run_left
    #TODO: Copy the elif statement here for Paul's righthand movement

        #TODO: Copy the code here to set Paul's velocity 

        #TODO: Write the code here to set Paul's righthand movement animation

    else:
        if MY.grounded: 
            #TODO: Copy the code here to track and control velocity when grounded






        #TODO: Write the code here to track and control velocity when falling





    
    #TODO: Write the code here to track and control velocity when flying






    # Gravity
    MY.player.velocity.y = min(MY.player.velocity.y + GRAVITY_ACCEL, PLAYER_TERMINAL_VEL)

    #TODO: Write the code here to check for hazard collisions









    
    # Update Paul's location
    MY.player.update(delta_time)

    # Check for wall collisions
    touching = False
    for wall in MY.walls:
        if MY.player.collides_with(wall):
            if MY.player.collision[DOWN]:
                MY.player.snap_to_object_y(wall, DOWN)
                MY.player.velocity.y = 0
                MY.grounded = touching = True
            if MY.player.collision[LEFT]:
                MY.player.snap_to_object_x(wall, LEFT)
                MY.player.velocity.x = 0
                touching = True
            if MY.player.collision[RIGHT]:
                MY.player.snap_to_object_x(wall, RIGHT)
                MY.player.velocity.x = 0
                touching = True
            if MY.player.collision[UP]:
                MY.player.snap_to_object_y(wall, UP)
                MY.player.velocity.y = 0
                touching = True
    if not touching:
        MY.grounded = False
    
    # Check for exit portal collision
    if MY.player.collides_with(MY.exit_portal):
        if MY.level_num >= 1 and MY.level_num < 6:
            # Load and run the next level
            MY.level_num = MY.level_num + 1
            level_name_as_string = 'Level' + str(MY.level_num)
            tilemap = read_file("Assets/" + level_name_as_string + ".txt")
            load_level(tilemap)
        elif MY.level_num == 6:
            # Show the Win screen
            change(2) 

    # Update level assets
    update_level(delta_time)

# Register the states
Manager.register(Intro)
Manager.register(sys.modules[__name__]) # The current file 
Manager.register(Lose)
Manager.register(Win)

# Run the game!
Manager.run(SCREEN, WINDOW, BLUE, "MAIN")
