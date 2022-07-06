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
        MY.boss_health -= 1
        MY.player_hitbox.active = False

    # Wrote code for projectiles that have a square path around the Creeper
    for projectile in MY.shield_projectiles:
        # Wrote code to move the projectile to the right
        if(projectile.location.x >= 320 and projectile.location.x < 480 and projectile.location.y == 240):
            projectile.location.x += MY.projectile_velocity
        # Wrote code to move the projectile down
        elif(projectile.location.x == 480 and projectile.location.y >= 240 and projectile.location.y < 400): 
            projectile.location.y += MY.projectile_velocity
        # Wrote code to move the projectile to the left
        elif(projectile.location.x <= 480 and projectile.location.x > 320 and projectile.location.y == 400): 
            projectile.location.x -= MY.projectile_velocity
        # Wrote code to move the projectile up
        elif(projectile.location.x == 320 and projectile.location.y > 240 and projectile.location.y <= 400): 
            projectile.location.y -= MY.projectile_velocity
        # Paul loses health if he collides with a projectile
        if projectile.collides_with(MY.player):
            MY.player_health -= MY.proj_damage
            player_pain_anim()
            MY.player.hit = True

    player_attack_update()

    update_assets(delta_time)
    
    check_win()

    check_events()

# Register the game states
Manager.register(sys.modules[__name__]) # The current file
Manager.register(GameOver)
Manager.register(PlayAgain)
Manager.register(Intro)

# Run the game
Manager.run(SCREEN, WINDOW, BLACK, "CHALLENGE2")
