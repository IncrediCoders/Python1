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
    # Controls Paul's lefthand movement
    if key_held_down(pygame.K_LEFT): 
        # Set Paul's velocity
        MY.player.velocity.x = max(MY.player.velocity.x - PLAYER_ACCEL, -PLAYER_MAX_SPEED)
        # Set Paul's lefthand movement animation
        MY.player.sprite = MY.paul_run_left
    # Controls Pauls's righthand movement
    elif key_held_down(pygame.K_RIGHT): 
        # Set Paul's velocity 
        MY.player.velocity.x = min(MY.player.velocity.x + PLAYER_ACCEL, PLAYER_MAX_SPEED)
        # Set Paul's righthand movement animation
        MY.player.sprite = MY.paul_run_right
    else:
        if MY.grounded: 
            # Track and control velocity when grounded
            if MY.player.velocity.x > 0:
                MY.player.velocity.x = max(0, MY.player.velocity.x - PLAYER_DECEL)
            elif MY.player.velocity.x < 0:
                MY.player.velocity.x = min(0, MY.player.velocity.x + PLAYER_DECEL)
            # Set Paul's movement to idle
            else:
                MY.player.sprite = MY.paul_idle_right
        # Track and control velocity when falling
        else:
            if MY.player.velocity.x > 0:
                MY.player.velocity.x = max(0, MY.player.velocity.x - PLAYER_AIR_DECEL)
            elif MY.player.velocity.x < 0:
                MY.player.velocity.x = min(0, MY.player.velocity.x + PLAYER_AIR_DECEL)
    
    # Track and control velocity when flying
    if not MY.grounded:      
        if MY.player.velocity.x > 0:
            MY.player.sprite = MY.paul_jetpack_right
        elif MY.player.velocity.x < 0:
            MY.player.sprite = MY.paul_jetpack_left

    # Gravity
    MY.player.velocity.y = min(MY.player.velocity.y + GRAVITY_ACCEL, PLAYER_TERMINAL_VEL)

    # Check for hazard collisions
    for hazard in MY.hazards:
        if MY.player.collides_with(hazard):
            MY.player_health -= 1
            if MY.player_health == 0:
                change(1)
            else:
                MY.player.location = MY.player_start_position
                MY.player.set_velocity(0, 0)
                MY.player.sprite = MY.paul_pain_right
    
    # Wrote code to check for battery collisions
    for battery in MY.batteries:
        if MY.player.collides_with(battery):
            MY.batteries.remove(battery)
            MY.player_health += 1

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
Manager.register(sys.modules[__name__]) #The current file 
Manager.register(Lose)
Manager.register(Win)

# Run the game!
Manager.run(SCREEN, WINDOW, BLUE, "CHALLENGE2")
