#Runs the init.py file and imports the libraries
from init import *

#Set timer for 60 seconds
MY.timer = 60

def update(delta_time):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        elif key_down(event, " ") and (MY.grounded or MY.level_num > 3):
            MY.player.velocity.y = -700
            MY.grounded = False

    #Subtract delta time (milliseconds) from timer total
    MY.timer -= delta_time 

    #If timer reaches 0 show lose screen
    if MY.timer <= 0:
        change(1)

    if key_held_down(pygame.K_LEFT): 
        #TODO: Uncomment the two lines below
        MY.player.velocity.x = max(MY.player.velocity.x - PLAYER_ACCEL, -PLAYER_MAX_SPEED)
        MY.player.sprite = MY.paul_run_left
    #TODO: Copy the elif statement here for the player's righthand movement
    elif key_held_down(pygame.K_RIGHT): 
        #TODO: Copy the code here to set the player's velocity 
        MY.player.velocity.x = min(MY.player.velocity.x + PLAYER_ACCEL, PLAYER_MAX_SPEED)
        #TODO: Write the code here to set Paul's righthand movement animation
        MY.player.sprite = MY.paul_run_right
    else:
        if MY.grounded: 
            #TODO: Copy the code here to track and control velocity when grounded
            if MY.player.velocity.x > 0:
                MY.player.velocity.x = max(0, MY.player.velocity.x - PLAYER_DECEL)
            elif MY.player.velocity.x < 0:
                MY.player.velocity.x = min(0, MY.player.velocity.x + PLAYER_DECEL)
            #TODO: Copy the code here to set Paul's movement to idle
            else:
                MY.player.sprite = MY.paul_idle_right
        #TODO: Write code here to track and control velocity when falling
        else:
            if MY.player.velocity.x > 0:
                MY.player.velocity.x = max(0, MY.player.velocity.x - PLAYER_AIR_DECEL)
            elif MY.player.velocity.x < 0:
                MY.player.velocity.x = min(0, MY.player.velocity.x + PLAYER_AIR_DECEL)
    
    #TODO: Write the code here to track and control velocity when flying
    if not MY.grounded:      
        if MY.player.velocity.x > 0:
            MY.player.sprite = MY.paul_jetpack_right
        elif MY.player.velocity.x < 0:
            MY.player.sprite = MY.paul_jetpack_left

    #Gravity
    MY.player.velocity.y = min(MY.player.velocity.y + GRAVITY_ACCEL, PLAYER_TERMINAL_VEL)

    #Check for hazard collisions
    for hazard in MY.hazards:
        if MY.player.collides_with(hazard):
            MY.player_health -= 2
            if MY.player_health <= 0:
                change(1)
            else:
                MY.player.location = MY.player_start_position
                MY.player.set_velocity(0, 0)
                MY.player.sprite = MY.paul_pain_right
                break
    
    MY.player.update(delta_time)

    # check for wall collisions
    touching = False
    for wall in MY.walls:
        if MY.player.collides_with(wall):
            if MY.player.collision[DOWN]:
                MY.player.snap_to_object_y(wall, DOWN)
                MY.player.velocity.y = 0
                MY.grounded = touching = True
                continue
            if MY.player.collision[LEFT]:
                MY.player.snap_to_object_x(wall, LEFT)
                MY.player.velocity.x = 0
                touching = True
                continue
            if MY.player.collision[RIGHT]:
                MY.player.snap_to_object_x(wall, RIGHT)
                MY.player.velocity.x = 0
                touching = True
                continue
            if MY.player.collision[UP]:
                MY.player.snap_to_object_y(wall, UP)
                MY.player.velocity.y = 0
                touching = True
                continue
    if not touching:
        MY.grounded = False
    
    #Check for exit portal collision
    if MY.player.collides_with(MY.exit_portal):
        if MY.level_num >= 1 and MY.level_num < 6:
            #Move to next level
            MY.level_num = MY.level_num + 1
            level_name_as_string = 'level' + str(MY.level_num)
            tilemap = read_file("assets/" + level_name_as_string + ".txt")
            load_level(tilemap)
            #Reset timer 
            MY.timer = 60
        elif MY.level_num == 6:
            #Show win screen
            change(2)

    update_level(delta_time)

# Registering the states
Manager.register(sys.modules[__name__]) #The current file 
Manager.register(Lose)
Manager.register(Win)

# Run the game!
Manager.run(SCREEN, WINDOW, BLUE, "CHALLENGE1")