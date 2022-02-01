# Runs the init.py file and imports the libraries
from init import *

def update(delta_time):
    # Check if Paul collides with the walls
    if MY.player.location.x < MY.wall_height:
        MY.player.location.x = MY.wall_height
    if MY.player.location.x > WINDOW_WIDTH - MY.wall_height:
        MY.player.location.x = WINDOW_WIDTH - MY.wall_height
    if MY.player.location.y < MY.wall_height:
        MY.player.location.y = MY.wall_height
    if MY.player.location.y > WINDOW_LENGTH - (MY.wall_height + 15):
        MY.player.location.y = WINDOW_LENGTH - (MY.wall_height + 15)

    handle_pillar_collision()

    # Paul loses health if he collides with the Creeper
    if MY.player.collides_with_boss():
        player_pain_anim()
        MY.player_health -= 1
        MY.player_hitbox.active = False

    #TODO: Write code here to play a sound when Paul gets hit
    
    



    # Add Paul's hitbox depending on his direction
    if MY.player_dir == UP:
        MY.player_hitbox.location = pygame.math.Vector2(
            MY.player.location.x + 20, MY.player.location.y - 20)
    elif MY.player_dir == DOWN:
        MY.player_hitbox.location = pygame.math.Vector2(
            MY.player.location.x - 10, MY.player.location.y + 25)
    elif MY.player_dir == LEFT:
        MY.player_hitbox.location = pygame.math.Vector2(
            MY.player.location.x - 20, MY.player.location.y)
    elif MY.player_dir == RIGHT:
        MY.player_hitbox.location = pygame.math.Vector2(
            MY.player.location.x + 20, MY.player.location.y)

    # Reduce Creeper's health when he gets attacked
    if MY.player_hitbox.active and MY.boss.collides_with_hitbox():
        #TODO: Write code here to play a sound when Creeper is attacked



        MY.boss_health -= 1
        MY.player_hitbox.active = False

    player_attack_update()

    update_assets(delta_time)
    
    check_win()

    #TODO: Write code here to play a sound when Paul wins or loses







    check_events()

# Register the game states
Manager.register(sys.modules[__name__]) # The current file
Manager.register(GameOver)
Manager.register(PlayAgain)

# Run the game
Manager.run(SCREEN, WINDOW, BLACK, "CHALLENGE1")
