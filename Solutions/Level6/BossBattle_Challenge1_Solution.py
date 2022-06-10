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

    # Wrote code here to play a sound when Paul gets hit
    if MY.player.collides_with_projectile():
        mixer.music.load("Assets/PaulHit.wav")
        mixer.music.play()
        return True

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
        # Wrote code here to play a sound when Creeper is attacked
        mixer.music.load("Assets/BossHit.wav")
        mixer.music.set_volume(0.4)
        mixer.music.play()
        MY.boss_health -= 1
        MY.player_hitbox.active = False

    player_attack_update()

    update_assets(delta_time)
    
    check_win()

    # Wrote code here to play a sound when Paul wins or loses
    if(MY.boss_health <= 0):
        mixer.music.load("Assets/Win.wav")
        mixer.music.play()
    elif(MY.player_health <= 0):
        mixer.music.load("Assets/Lose.wav")
        mixer.music.play()

    check_events()

# Register the game states
Manager.register(sys.modules[__name__]) # The current file
Manager.register(GameOver)
Manager.register(PlayAgain)
Manager.register(Intro)

# Run the game
Manager.run(SCREEN, WINDOW, BLACK, "CHALLENGE1")
