#=============================================================
#PART 1: IMPORTING DEPENDENCIES AND ASSIGNING GLOBAL VARIABLES
from os import path
import math
import os
import random
import time
import sys
import pygame
from pygame import mixer

# colors
WHITE = [225, 225, 225]
BLACK = [0, 0, 0]
YELLOW = [255, 255, 0]
RED = [255, 0, 0]
GREEN = [0, 128, 0, 128]
BLUE = [0, 192, 255, 128]

# directions
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

_data = {}

X_VALUE = 0
Y_VALUE = 0

# Note current challenge to hide certain game features
current_challenge = ''

# mixer for sound
mixer.init()

#============================================================
#PART 2: CREATING A FRAMEWORK OF GENERAL CLASSES AND FUNCTIONS
def start(window, name):
    """Initialize pygame and random seed."""
    pygame.init()
    random.seed(time.time())
    pygame.display.set_caption(name)
    return pygame.display.set_mode((int(window[0]), int(window[1])))

def stop():
    sys.exit()

def check_events():
    """
    Checks for pygame events, including boss attacks and if you closed the window.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        elif(MY.display_intro):
            MY.display_intro = False
            Manager.current = 3  
        elif event.type == MY.boss_attack_event:
            MY.is_boss_attacking = True
        else:
            MY.is_boss_attacking = False

def check_ending_events():
    '''Checks for events in the restart state'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if MY.background.collides_with_point(pygame.mouse.get_pos()):
                MY.boss_health = 300
                MY.player_health = 100
                Manager.current = 3
                

def check_intro_events():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if MY.background.collides_with_point(pygame.mouse.get_pos()):
                    MY.boss_health = 300
                    MY.player_health = 100
                    Manager.current = 0

def draw_rect(screen, color, top_left, size):
    pygame.draw.rect(screen, color, (top_left[0], top_left[1], size[0], size[1]))

def health_bar(screen, health, max_health, max_size, location):
    """Creates a health bar at the given position."""
    if health > max_health - max_health * 0.25:
        bar_color = GREEN
    elif health > max_health - max_health * 0.5:
        bar_color = YELLOW
    else:
        bar_color = RED

    width = max_size[0] * (health / max_health)
    draw_rect(screen, bar_color, location, (width, max_size[1]))

def screen_wrap(obj, window):
    """Wraps a given framework object around the screen, returns true if object is at edge."""
    flag = False

    # Wrap X direction
    if obj.location.x > window.x:
        obj.location.x = 0
        flag = True
    elif obj.location.x < 0:
        obj.location.x = window.x
        flag = True

    # Wrap Y direction
    if obj.location.y > window.y:
        obj.location.y = 0
        flag = True
    elif obj.location.y < 0:
        obj.location.y = window.y
        flag = True

    return flag

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

   
def key_down(event, key):
    if isinstance(key, str):
        return event.type == pygame.KEYDOWN and event.key == key
    return event.type == pygame.KEYDOWN and event.key == key

def key_held_down(key):
    if isinstance(key, str):
        return pygame.key.get_pressed()[ord(key)]
    return pygame.key.get_pressed()[key]

def get_file(filename):
    """Returns the absolute path of a file."""
    # This grabs your files from your folder.
    return path.join(path.dirname(__file__), filename)

def read_file(filename):
    """Read a file line by line and return it as an array of strings."""
    # Create an empty array.
    array = []
    # Open our file for read.
    file = open(filename, 'r')

    # Put all the lines in an array
    for line in file:
        array.append(line.rstrip())

    return array

class Machine:
    """Game state machine class."""
    def __init__(self):
        self.current = 0
        self.previous = 0
        self.states = []

    def register(self, module):
        """Registers the state's init, update, draw, and cleanup functions."""
        self.states.append({'initialize': module.initialize,
                            'update': module.update,
                            'draw': module.draw,
                            'cleanup': module.cleanup})

    def update(self, delta_time):
        '''
        Update all of the lerps. Auto removes lerps when done.
        Called internally by the state manager.
        '''
        to_delete = []
        for (obj, lerp_list) in _data.items():
            if not lerp_list:
                to_delete.append(obj)
            elif lerp_list[0].update(obj, delta_time):
                lerp_list.pop(0)
                # Remove duplicates
                while lerp_list and lerp_list[0].end == getattr(obj, lerp_list[0].member):
                    lerp_list.pop(0)

        for key in to_delete:
            del _data[key]

    def run(self, screen, window, fill_color, challenge):
        """Runs the state given machine."""
        clock = pygame.time.Clock()

        # Note current challenge to hide certain game features
        global current_challenge
        current_challenge = challenge

        # First run initialize!
        self.states[self.current]['initialize'](window)

        while True:
            delta_time = clock.tick(60) / 1000
            if self.current != self.previous:
                self.states[self.current]['cleanup']()
                self.states[self.current]['initialize'](window)
                self.previous = self.current

            self.update(delta_time)
            self.states[self.current]['update'](delta_time)
            screen.fill(fill_color)
            self.states[self.current]['draw'](screen)
            pygame.display.flip()

class Image:
    """Loads an image object"""
    def __init__(self, image_file_name):
        if image_file_name is not None:
            self.data = pygame.image.load(get_file(image_file_name)).convert_alpha()
        else:
            self.data = None

    def surface(self):
        return self.data

class SpriteSheet:
    """
    Sprite sheet class for managing sprite animations.

        sheet = SpriteSheet("image.png", (16, 16));
    """

    def __init__(self, filename, frame_size):
        self.sheet = pygame.image.load(get_file(filename)).convert_alpha()
        rect = self.sheet.get_rect()
        self.columns = rect.width / frame_size[0]
        self.rows = rect.height / frame_size[1]
        rect.width = frame_size[0]
        rect.height = frame_size[1]
        self.rectangle = rect

    def image_at(self, index):
        """
        Get an image at the given 0 based index.

            obj.sprite = sheet.image_at(0);
        """
        _x_ = math.floor(index % self.columns) * self.rectangle.width
        _y_ = math.floor(index / self.columns) * self.rectangle.height
        self.rectangle.centerx = _x_ + self.rectangle.width / 2
        self.rectangle.centery = _y_ + self.rectangle.height / 2
        image = Image(None)
        image.data = pygame.Surface(self.rectangle.size, pygame.SRCALPHA, 32).convert_alpha()
        image.data.blit(self.sheet, (0, 0), self.rectangle)
        return image

    def num_frames(self):
        """
        Return the number of frames of animation for the given sheet.

            size = sheet.num_frames();
        return self.columns * self.rows
        """
        return self.columns * self.rows

class Animator:
    """Animator class for animation functions"""
    def __init__(self, sheet, duration_seconds, looping = True, ending=False):
        self.sheet = sheet
        self.frame_num = 0

        self.frame_time = 0.0

        self.playing = True
        self.playspeed = 1.0
        self.looping = looping
        self.ending = ending

        self.reset()
        self.set_duration(duration_seconds)

    def set_duration(self, duration_seconds):
        self.duration = duration_seconds
        self.transition = self.duration / self.num_frames

    def use_anim(self, sheet):
        self.sheet = sheet
        self.reset()

    def reset(self):
        self.frame_num = 0
        self.current = self.sheet.image_at(self.frame_num)
        self.frame_time = 0
        self.num_frames = self.sheet.num_frames()

    def play(self, playspeed=1.0):
        self.playspeed = playspeed
        self.reset()
        self.unpause()

    def pause(self):
        self.playing = False

    def unpause(self):
        self.playing = True
        self.shown = True

    def update(self, d_t):
        d_t = d_t * self.playspeed

        if self.playing:
            self.frame_time += d_t

            if self.frame_time >= self.transition:
                self.frame_time -= self.transition
                self.frame_num += 1

                if self.ending:
                    if self.current == self.num_frames - 1:
                        self.playing = False

                if self.looping:
                    self.frame_num %= self.num_frames

                self.current = self.sheet.image_at(self.frame_num)

                if self.frame_num >= self.num_frames:
                    self.playing = False

    def surface(self):
        return self.current.surface()

class Object:
    """
    Object class used to organize and track common game object data, such as location and appearance

        obj = Object(IMAGE);
    """
    location = pygame.math.Vector2(0, 0)
    scale = 1
    velocity = pygame.math.Vector2(0, 0)

    def __init__(self, image):
        self.sprite = image
        self.rotation = 0
        self.active = False
        self.collision = [False] * 5
        self.hit = False

    def __setattr__(self, name, value):
        if name == "location" or name == "velocity":
            self.__dict__[name] = pygame.math.Vector2(value[0], value[1])
        elif name == "rotation":
            self.__dict__[name] = value - 360 * int(value / 360)
        elif name == "sprite":
            if isinstance(value, Image):
                self.__dict__[name] = value
            elif isinstance(value, Animator):
                self.__dict__[name] = value
        else:
            self.__dict__[name] = value

    def get_transformed_rect(self):
        """
        Returns a transformed version of the object sprite. Generally for internal use only.

            rect = obj.get_transformed_rect();
        """
        sprite = pygame.transform.rotozoom(self.sprite.surface(), self.rotation, self.scale)
        rect = sprite.get_rect()
        rect.center = self.location
        return rect

    def width(self):
        """
        Gets the width of the object in reference to it's image data.

            width = obj.width();
        """
        rect = self.get_transformed_rect()
        return rect.width

    def height(self):
        """
        Gets the height of the object in reference to it's image data.

            height = obj.height();
        """
        rect = self.get_transformed_rect()
        return rect.height

    def add_rotation(self, degrees):
        """
        Add to the existing rotation of an object in degrees. Positive is clockwise.

            obj.add_rotation(90);
        """
        self.rotation = self.rotation + degrees
        self.rotation = self.rotation - 360 * int(self.rotation /360)

    def add_velocity(self, direction, speed, max_speed):
        """
        Add velocity to the object with the given direction and speed.

            obj.add_velocity((0, 1), 1, 10); # increase upwards
        """
        epsilon = 1.0e-15
        direction = pygame.math.Vector2(math.cos(math.radians(direction - 90)),
                                        math.sin(math.radians(direction - 90)))
        if direction.x < epsilon and direction.x > 0:
            direction.x = 0

        if direction.y < epsilon and direction.y > 0:
            direction.y = 0

        vel = pygame.math.Vector2(-1 * direction.x * speed, direction.y * speed)

        self.velocity += vel
        distance_sq = self.velocity.length()

        if distance_sq > max_speed:
            self.velocity.normalize_ip()
            self.velocity *= max_speed

    def set_velocity(self, degrees, speed):
        """
        set velocity of the object with the given angle and speed.

            obj.set_velocity(45, 5); # left 5
        """
        self.velocity = pygame.math.Vector2(-1 * math.cos(math.radians(degrees - 90)) * speed,
                                            math.sin(math.radians(degrees - 90)) * speed)

    def collides_with(self, other_obj):
        """
        Check if this object collides with the given object.

            if obj1.collides_with(obj2):
                do_things();
        """
        # Check for early rejection.
        dist = (self.location - other_obj.location).length_squared()
        # If distance between objects is greater then 64^2
        if dist > 4096:
            self.collision[DOWN] = self.collision[UP] = False
            self.collision[LEFT] = self.collision[RIGHT] = False
            return False

        # Get transformed rectangles
        rect1 = self.get_transformed_rect()
        rect2 = other_obj.get_transformed_rect()

        if not rect1.colliderect(rect2):
            return False

        self.collision[DOWN] = rect2.collidepoint((rect1.center[0] - rect1.width / 4, rect1.center[1] + rect1.height / 2)) or rect2.collidepoint((rect1.center[0] + rect1.width / 4, rect1.center[1] + rect1.height / 2))
        self.collision[UP] = rect2.collidepoint((rect1.center[0] - rect1.width / 4, rect1.center[1] - rect1.height / 2)) or rect2.collidepoint((rect1.center[0] + rect1.width / 4, rect1.center[1] - rect1.height / 2))
        self.collision[LEFT] = rect2.collidepoint((rect1.center[0] - rect1.width / 2, rect1.center[1] + rect1.height / 4)) or rect2.collidepoint((rect1.center[0] - rect1.width / 2, rect1.center[1] - rect1.height / 4))
        self.collision[RIGHT] = rect2.collidepoint((rect1.center[0] + rect1.width / 2, rect1.center[1] + rect1.height / 4)) or rect2.collidepoint((rect1.center[0] + rect1.width / 2, rect1.center[1] - rect1.height / 4))

        return True


    def collides_with_boss(self):
        player = pygame.Rect(MY.player.location.x - 10, MY.player.location.y + 22, 20, 10)
        boss = MY.boss_defence_area
        if player.colliderect(boss) and MY.player_hitbox.active == False:
            MY.player.hit = True
            if(MY.hit_recorded == False):
                MY.last_hit = pygame.time.get_ticks()
                MY.hit_recorded = True
            return True  
        return False
    
    def collides_with_hitbox(self):
        boss = self.get_transformed_rect() 
        hitbox = MY.player_hitbox.get_transformed_rect()
        if boss.colliderect(hitbox):
            return True
        return False

    def collides_with_projectile(self):
        if (self.hit == True):
            self.hit = False
            return True
        return False

    def snap_to_object_x(self, other_obj, facing):
        """
        Snaps the object to the left or right of the other object given.

            # Snap obj1 left of obj2
            obj1.snap_to_object_x(obj2, LEFT);
        """
        if facing == LEFT:
            self.location.x = (other_obj.location.x +
                               other_obj.width() / 2 +
                               self.width() / 2)
        else:
            self.location.x = (other_obj.location.x -
                               (other_obj.width() / 2 +
                                self.width() / 2))

    def snap_to_object_y(self, other_obj, facing):
        """
        Snaps the object to the left or right of the other object given.

            # Snap obj1 left of obj2
            obj1.snap_to_object(obj2, LEFT);
        """
        if facing == UP:
            self.location.y = (other_obj.location.y +
                               other_obj.height() / 2 +
                               self.height() / 2)
        else:
            self.location.y = (other_obj.location.y -
                               (other_obj.height() / 2 +
                                self.height() / 2))

    def collides_with_point(self, point):
        """
        Check if this object collides with the given position.

            # point
            obj.collides_with_point(10, 10);
        """
        sprite = pygame.transform.rotate(self.sprite.surface(), self.rotation)
        rect = sprite.get_rect()
        location = self.location + self.velocity
        rect.center = location
        return rect.collidepoint(point)

    def update(self, delta_time):
        self.location += self.velocity * delta_time
        self.sprite.update(delta_time)

    def draw(self, screen):
        """
        draws the object to the screen.

            # draw the object
            obj.draw(SCREEN);
        """
        sprite = pygame.transform.rotozoom(self.sprite.surface(), self.rotation, self.scale)
        rect = sprite.get_rect()
        rect.center = self.location
        screen.blit(sprite, rect)

class CountdownTimer:
    """
    Countdown timer class for timer logic.
        timer = CountdownTimer(seconds);
        if (timer.tick(delta_time)):
            do_things();
    """
    def __init__(self, max_time):
        """Initialize the timer with the given values."""
        self.max_time = max_time
        self.current_time = 0

    def tick(self, delta_time):
        """update timer and check if finished."""
        self.current_time += delta_time
        if self.current_time >= self.max_time:
            return False
        return True

class TextObject:
    """
    Create an object that renders text. Assumes that the default font
    freesansbold exists in the project directory as a true type font.
        #create a text object
        title = TextObject(color.RED, 12, "example");
    """

    def __init__(self, color_value, font_size, text):
        self.location = pygame.math.Vector2(0, 0)
        self.color = color_value
        self.font_size = font_size
        self.text = text
        self.centered = False

    def __setattr__(self, name, value):
        if name == "location":
            self.__dict__[name] = pygame.math.Vector2(value[0], value[1])
        elif name == "font_size":
            self.__dict__[name] = value
            path = os.path.dirname(__file__) + '/Assets/FreeSansBold.ttf'
            self.font = pygame.font.Font(resource_path(path), int(self.font_size))
        else:
            self.__dict__[name] = value

    def draw(self, screen):
        """
        Draws the object text to the screen.
            text.draw(SCREEN);
        """
        obj = self.font.render(self.text, 1, self.color)
        loc = pygame.math.Vector2(self.location.x, self.location.y)
        if self.centered is True:
            loc.x -= obj.get_rect().width / 2
        screen.blit(obj, loc)

#============================================================
#PART 3: SETUP FOR THE BOSS BATTLE GAME
Manager = Machine()

WINDOW_WIDTH = 800
WINDOW_LENGTH = 600
WINDOW = pygame.math.Vector2(800, 600)
SCREEN = start(WINDOW, "Boss Battle")

# Load sprites constants
PROJECTILE_IMAGE = Image("Assets/Projectile.png")
HITBOX_IMAGE = Image("Assets/Hitbox.png")

# Constants
PLAYER = 0
BOSS = 1
GRASS = 4
TILE_SIZE = 32

class Data:
    """
    Data loads the changeable data for gameplay
    """
    background_sheet = SpriteSheet("Assets/Background.png", (800, 600))
    background_anim = Animator(background_sheet, 0.75)
    background = Object(background_sheet.image_at(0))
    # Player data
    player_idle_forward_sheet = SpriteSheet("Assets/Paul/PaulIdleFront.png", (64, 68))
    player_idle_backward_sheet = SpriteSheet("Assets/Paul/PaulIdleBack.png", (64, 68))
    player_idle_left_sheet = SpriteSheet("Assets/Paul/PaulIdleLeft.png", (64, 68))
    player_idle_right_sheet = SpriteSheet("Assets/Paul/PaulIdleRight.png", (64, 68))
    idle_forward = Animator(player_idle_forward_sheet, 1)
    idle_backward = Animator(player_idle_backward_sheet, 1)
    idle_left = Animator(player_idle_left_sheet, 1)
    idle_right = Animator(player_idle_right_sheet, 1)
    player_walk_forward_sheet = SpriteSheet("Assets/Paul/PaulMoveFront.png", (64, 68))
    player_walk_backward_sheet = SpriteSheet("Assets/Paul/PaulMoveBack.png", (64, 68))
    player_walk_left_sheet = SpriteSheet("Assets/Paul/PaulMoveLeft.png", (64, 68))
    player_walk_right_sheet = SpriteSheet("Assets/Paul/PaulMoveRight.png", (64, 68))
    walk_forward = Animator(player_walk_forward_sheet, 1)
    walk_backward = Animator(player_walk_backward_sheet, 1)
    walk_left = Animator(player_walk_left_sheet, 1)
    walk_right = Animator(player_walk_right_sheet, 1)
    player_attack_forward_sheet = SpriteSheet("Assets/Paul/PaulAttackFront.png", (100, 100))
    player_attack_backward_sheet = SpriteSheet("Assets/Paul/PaulAttackBack.png", (100, 100))
    player_attack_left_sheet = SpriteSheet("Assets/Paul/PaulAttackLeft.png", (128, 68))
    player_attack_right_sheet = SpriteSheet("Assets/Paul/PaulAttackRight.png", (128, 68))
    attack_forward = Animator(player_attack_forward_sheet, 0.5)
    attack_backward = Animator(player_attack_backward_sheet, 0.5)
    attack_left = Animator(player_attack_left_sheet, 0.5)
    attack_right = Animator(player_attack_right_sheet, 0.5)
    player_pain_forward_sheet = SpriteSheet("Assets/Paul/PaulPainFront.png", (64, 68))
    player_pain_backward_sheet = SpriteSheet("Assets/Paul/PaulPainBack.png", (64, 68)) 
    player_pain_left_sheet = SpriteSheet("Assets/Paul/PaulPainLeft.png", (64, 68))
    player_pain_right_sheet = SpriteSheet("Assets/Paul/PaulPainRight.png", (64, 68))
    pain_forward = Animator(player_pain_forward_sheet, 0.5)
    pain_backward = Animator(player_pain_backward_sheet, 0.5)
    pain_left = Animator(player_pain_left_sheet, 0.5)
    pain_right = Animator(player_pain_right_sheet, 0.5)
    player = Object(player_walk_forward_sheet.image_at(2))
    player_start_position = pygame.math.Vector2(0, 0)
    player_health = 100
    player_dir = DOWN
    player_text = TextObject(BLACK, 24, "Player: ")
    player_text.location.x = 25
    player_hitbox = Object(HITBOX_IMAGE)
    attack_allowed = False
    hit_recorded = False
    # Boss data
    boss_attack_sheet = SpriteSheet("Assets/Creeper/CreeperAttack.png", (100, 100))
    boss_attack = Animator(boss_attack_sheet, 2)
    boss_idle_sheet = SpriteSheet("Assets/Creeper/CreeperIdle.png", (100, 100))
    boss_idle = Animator(boss_idle_sheet, 2.5)
    boss_pain_sheet = SpriteSheet("Assets/Creeper/CreeperPain.png", (100, 100))
    boss_pain = Animator(boss_pain_sheet, 0.5)
    boss = Object(boss_idle_sheet.image_at(0))
    boss_start_position = pygame.math.Vector2(0, 0)
    boss_defence_area = pygame.Rect(1,1,1,1)
    boss_text = TextObject(BLACK, 24, "Creeper: ")
    boss_text.location.x = 567
    boss_health = 300
    boss_attack_event = pygame.USEREVENT
    is_boss_attacking = False
    # Projectile data
    projectile_sheet = SpriteSheet("Assets/PlasmaBall.png", (32, 32))
    projectile_anim = Animator(projectile_sheet, 6)
    projectile = Object(projectile_sheet.image_at(0))
    proj_damage = 0.1
    aimed_proj_damage = 12.5
    proj_angle = 0
    num_projectiles = 0
    projectiles = []
    shield_projectiles = []
    projectile_velocity = 1
    aimed_projectile_velocity = 3 
    s_proj_count = 0
    last_hit = 0
    proj_hit = False
    # Miscellaneous data
    wall_height = 70
    pillar_width = 28
    pillar_height = 112
    pillar_top_left = Object(Image("Assets/PillarTop.png"))
    pillar_top_right = Object(Image("Assets/PillarTop.png"))
    pillar_bottom_left = Object(Image("Assets/PillarTop.png"))
    pillar_bottom_right = Object(Image("Assets/PillarTop.png"))
    pillars = [pillar_top_left, pillar_top_right, pillar_bottom_left, pillar_bottom_right]
    state = 0
    last_state = 2
    index = 0
    game_over_sheet = SpriteSheet("Assets/GameOverOverlay.png", (800, 600))
    game_over = Animator(game_over_sheet, 0.75, False, True)
    game_over_time = 0
    you_win_sheet = SpriteSheet("Assets/YouWinOverlay.png", (800, 600))
    you_win = Animator(you_win_sheet, 0.75, False, True)
    ending_overlay = Object(game_over_sheet.image_at(0))
    restart_button = Object(Image("Assets/PlayAgain.png"))
    intro_screen = Object(Image("Assets/IntroScreen.png"))
    intro_time = 0
    display_intro = True

MY = Data()

def initialize(window):
    """Initializes the game play class."""
    MY.background.location = window / 2
    MY.pillar_top_left.location = (207, 140)
    MY.pillar_top_right.location = (560, 140)
    MY.pillar_bottom_left.location = (207, 375)
    MY.pillar_bottom_right.location = (560, 375)
    MY.player.location = (window.x / 2, window.y / 4)
    MY.boss.location = window / 2
    MY.boss_defence_area = pygame.Rect(375, 333, 50, 22)
    pygame.time.set_timer(MY.boss_attack_event, 100)
    # Set up projectiles
    proj = Object(PROJECTILE_IMAGE)
    proj.location = (window.x / 2, window.y/ 2 - 35)
    proj.sprite = MY.projectile_anim
    MY.projectiles.append(proj)

    if(MY.s_proj_count == 0):
        s_proj = Object(PROJECTILE_IMAGE)
        s_proj.location = (window.x / 2.5, window.y / 2.5)
        s_proj.sprite = MY.projectile_anim
        MY.shield_projectiles.append(s_proj)
        MY.projectile_velocity = 1
        MY.s_proj_count += 1

def draw(screen):
    """Draws the state to the given screen for BossBattle."""
    MY.background.draw(screen)

    upper_left_pillar = pygame.Rect(175, 193, 65, 65)
    lower_left_pillar = pygame.Rect(175, 427, 65, 65)
    upper_right_pillar = pygame.Rect(525, 193, 70, 65)
    lower_right_pillar = pygame.Rect(525, 427, 70, 65) 

    player_rect = pygame.Rect(MY.player.location.x - 10, MY.player.location.y + 22, 20, 10)

    # Draw pillars depending on if player is in front or behind it
    if player_rect.colliderect(upper_left_pillar): 
       MY.pillar_top_left.draw(screen)
       MY.player.draw(screen)
       MY.boss.draw(screen)
       MY.pillar_bottom_left.draw(screen)
       MY.pillar_top_right.draw(screen)
       MY.pillar_bottom_right.draw(screen)
    elif player_rect.colliderect(lower_left_pillar):  
       MY.pillar_bottom_left.draw(screen)
       MY.player.draw(screen)
       MY.boss.draw(screen)
       MY.pillar_top_left.draw(screen)
       MY.pillar_top_right.draw(screen)
       MY.pillar_bottom_right.draw(screen)
    elif player_rect.colliderect(upper_right_pillar):
        MY.pillar_top_right.draw(screen)
        MY.player.draw(screen)
        MY.boss.draw(screen)
        MY.pillar_top_left.draw(screen)
        MY.pillar_bottom_left.draw(screen)
        MY.pillar_bottom_right.draw(screen)
    elif player_rect.colliderect(lower_right_pillar):
        MY.pillar_bottom_right.draw(screen)
        MY.player.draw(screen)
        MY.boss.draw(screen)
        MY.pillar_top_left.draw(screen)
        MY.pillar_bottom_left.draw(screen)
        MY.pillar_top_right.draw(screen)
    #Draw the player and boss depending on who's in front when they collide
    else:   
        if(MY.player.location.y < 300):
            MY.player.draw(screen)
            MY.boss.draw(screen)
        else:
            MY.boss.draw(screen)
            MY.player.draw(screen)
                        
        MY.pillar_top_left.draw(screen) 
        MY.pillar_bottom_left.draw(screen)
        MY.pillar_bottom_right.draw(screen)
        MY.pillar_top_right.draw(screen)
 
    # Draw player hitbox
    if MY.player_hitbox.active:
        MY.player_hitbox.draw(screen)

    # Draw projectiles
    for i in range(len(MY.projectiles)):
        if MY.projectiles[i].active:
            MY.projectiles[i].draw(screen)

    # If in Challenge 2 draw shield projectiles
    if(current_challenge == "CHALLENGE2"):
        for i in range(len(MY.shield_projectiles)):
            MY.shield_projectiles[i].draw(screen)

    # Draw healthbars
    MY.player_text.draw(screen)
    health_bar(screen, MY.player_health, 100, (100, 20), (110, 3))
    MY.boss_text.draw(screen)
    health_bar(screen, MY.boss_health, 300, (MY.boss.width(), 20), (675, 3))

def cleanup():
    """Cleans up the Intro State."""
    MY.projectiles = []

def player_attack_anim():
    """Updates animations for player while attacking"""
    if MY.player_dir == UP:
        MY.player.sprite = MY.attack_backward
    elif MY.player_dir == DOWN:
        MY.player.sprite = MY.attack_forward
    elif MY.player_dir == LEFT:
        MY.player.sprite = MY.attack_left
    elif MY.player_dir == RIGHT:
        MY.player.sprite = MY.attack_right

def reset_pain_anim():
    MY.pain_left.reset()
    MY.pain_right.reset()
    MY.pain_forward.reset()
    MY.pain_backward.reset()

def player_pain_anim():
    """Updates animations for player while in pain"""
    if MY.player_dir == UP:
        MY.player.sprite = MY.pain_backward
    elif MY.player_dir == DOWN:
        MY.player.sprite = MY.pain_forward
    elif MY.player_dir == LEFT:
        MY.player.sprite = MY.pain_left
    elif MY.player_dir == RIGHT:
        MY.player.sprite = MY.pain_right

def player_attack_update():
    """Updates player's hitbox and plays animations while attacking"""

    if key_held_down(pygame.K_SPACE) and MY.attack_allowed == True:
        MY.player_hitbox.active = True
        player_attack_anim()

def player_move_update(delta_time):
    """Updates animations for player if moving"""
    moving = (key_held_down(pygame.K_RIGHT) or key_held_down(pygame.K_LEFT) or
              key_held_down(pygame.K_DOWN) or key_held_down(pygame.K_UP))
    
    if not moving and not key_held_down(pygame.K_SPACE) and not MY.player.collides_with_boss() and not MY.projectile.collides_with(MY.player):
        MY.player_hitbox.active = False
        if MY.player_dir == UP:
            MY.player.sprite = MY.idle_backward
        elif MY.player_dir == DOWN:
            MY.player.sprite = MY.idle_forward
        elif MY.player_dir == LEFT:
            MY.player.sprite = MY.idle_left
        elif MY.player_dir == RIGHT:
            MY.player.sprite = MY.idle_right

    if key_held_down(pygame.K_UP):
        MY.player_hitbox.active = False
        MY.player.location.y -= 200 * delta_time
        MY.player_dir = UP
        MY.player.sprite = MY.walk_backward
    elif key_held_down(pygame.K_DOWN):
        MY.player_hitbox.active = False
        MY.player.location.y += 200 * delta_time
        MY.player_dir = DOWN
        MY.player.sprite = MY.walk_forward
    if key_held_down(pygame.K_LEFT):
        MY.player_hitbox.active = False
        MY.player.location.x -= 200 * delta_time
        MY.player_dir = LEFT
        MY.player.sprite = MY.walk_left
    elif key_held_down(pygame.K_RIGHT):
        MY.player_hitbox.active = False
        MY.player.location.x += 200 * delta_time
        MY.player_dir = RIGHT
        MY.player.sprite = MY.walk_right

def check_pillar_collision(player_rect, pillar):
    if player_rect.colliderect(pillar):
        if MY.player_dir == LEFT:
            MY.player.location.x += 9
        elif MY.player_dir == RIGHT:
            MY.player.location.x -= 9
        elif MY.player_dir == DOWN:
            MY.player.location.y -= 9
        elif MY.player_dir == UP:
            MY.player.location.x += 9

def handle_pillar_collision():
    upper_left_pillar =  pygame.Rect(192, 187, 30, 24) 
    upper_right_pillar = pygame.Rect(545, 190, 30, 24)
    lower_left_pillar = pygame.Rect(192, 422, 30, 24)
    lower_right_pillar = pygame.Rect(545, 422, 30, 24)

    player_rect = pygame.Rect(MY.player.location.x - 10, MY.player.location.y + 22, 20, 10)

    check_pillar_collision(player_rect, upper_left_pillar)
    check_pillar_collision(player_rect, upper_right_pillar)
    check_pillar_collision(player_rect, lower_left_pillar)
    check_pillar_collision(player_rect, lower_right_pillar)

def aim_at_player():
    distance_x = MY.player.location.x - MY.boss.location.x
    distance_y = MY.player.location.y - MY.boss.location.y 
    MY.proj_angle = math.atan2(distance_y, distance_x)


def fire_projectile(delta_time, projectile):
    MY.proj_angle 
    if projectile.active:
        projectile.location.x += math.cos(MY.proj_angle ) * MY.aimed_projectile_velocity 
        projectile.location.y += math.sin(MY.proj_angle ) * MY.aimed_projectile_velocity 
        projectile.update(delta_time)
        if projectile.location.x < MY.wall_height or projectile.location.x > WINDOW_WIDTH - MY.wall_height or projectile.location.y < MY.wall_height or projectile.location.y > WINDOW_LENGTH - (MY.wall_height + 20):
            projectile.location = (WINDOW_WIDTH / 2, WINDOW_LENGTH/ 2 - 35)
            aim_at_player()
            projectile.update(delta_time)
        if projectile.collides_with(MY.player):
            MY.player_health -= MY.aimed_proj_damage
            MY.player.hit = True
            MY.last_hit = pygame.time.get_ticks()
            projectile.location = (WINDOW_WIDTH / 2, WINDOW_LENGTH/ 2 - 35)
            aim_at_player()
            projectile.update(delta_time)


def boss_attack(delta_time):
    """shoot projectiles.""" 
    for p in MY.projectiles:
        p.active = True
        fire_projectile(delta_time, p)


def update_assets(delta_time):
    # Background
    MY.background.sprite = MY.background_anim
    MY.background.update(delta_time)

    # Player
    player_move_update(delta_time)
    
    # If player is hit, pause boss and player attacks
    if(pygame.time.get_ticks() - MY.last_hit < 800):
        MY.is_boss_attacking = False
        MY.attack_allowed = False
    else:
        MY.attack_allowed = True

    # Makes sure the pain animation runs for the correct amount of time
    if(MY.player.hit == True):
        player_pain_anim()
        if(pygame.time.get_ticks() - MY.last_hit > 300):
            MY.player.hit = False
            MY.hit_recorded = False
            reset_pain_anim() 
            
    MY.player.update(delta_time)

    # Boss
    if MY.player_hitbox.active and MY.boss.collides_with(MY.player_hitbox):
        MY.boss.sprite = MY.boss_pain 
        boss_attack(delta_time)
    elif MY.player_hitbox.active:
        MY.boss.sprite = MY.boss_attack
        boss_attack(delta_time)
    elif MY.is_boss_attacking:
        MY.boss.sprite = MY.boss_attack
        boss_attack(delta_time)
    else:
        MY.boss.sprite = MY.boss_idle
    MY.boss.update(delta_time)


def check_win():
    """Check win condition and change state if a player has won the game"""
    if MY.boss_health < 1:
        Manager.current = 1
        MY.state = 2
        MY.ending_overlay = Object(MY.you_win_sheet.image_at(0))
    elif MY.player_health < 1:
        Manager.current = 1
        MY.state = 2

class GameOver:
    """
    GameOver class to be loaded when the game ends.
    """
    MY = Data()

    def initialize(window):
        """Initializes the restart menu state."""
        pygame.time.set_timer(MY.boss_attack_event, 0)
        MY.ending_overlay.location = window / 2

    def update(delta_time):
        """Updates the restart menu state."""
        if MY.boss_health <= 0:
            MY.ending_overlay.sprite = MY.you_win
        else:
            MY.ending_overlay.sprite = MY.game_over
        MY.background.update(delta_time)
        MY.ending_overlay.update(delta_time)
        check_ending_events()

    def cleanup():
        """Cleans up the restart menu state."""
        MY.projectiles = []
        Manager.current = 2
        MY.state = 3

    def draw(screen):
        """Draws the restart menu state."""
        MY.background.draw(screen)
        MY.player.draw(screen)
        MY.boss.draw(screen)
        MY.ending_overlay.draw(screen)

class PlayAgain:
    MY = Data()

    def initialize(window):
        """Initializes the restart menu state."""
        pygame.time.set_timer(MY.boss_attack_event, 0)
        MY.ending_overlay.location = window / 2
        MY.game_over_time = pygame.time.get_ticks()

    def update(delta_time):
        """Updates the restart menu state."""
        if MY.boss_health <= 0:
            MY.ending_overlay.sprite = MY.you_win_sheet.image_at(3)
        else:
            MY.ending_overlay.sprite = MY.game_over_sheet.image_at(3)
        MY.background.update(delta_time)
        check_ending_events()

    def cleanup():
        """Cleans up the restart menu state."""
        MY.projectiles = []

    def draw(screen):
        """Draws the restart menu state."""
        MY.background.draw(screen)
        MY.player.draw(screen)
        MY.boss.draw(screen)
        if(pygame.time.get_ticks() - MY.game_over_time > 3000):
            MY.restart_button.location = (WINDOW_WIDTH/2, WINDOW_LENGTH/2)
            MY.restart_button.draw(screen)
        else:
            MY.ending_overlay.draw(screen)

class Intro:
    MY = Data()

    def initialize(window):
        """Initializes the intro menu state."""
        pygame.time.set_timer(MY.boss_attack_event, 0)
        MY.intro_screen.location = window / 2
        MY.display_intro = False

    def update(delta_time):
        """Updates the intro menu state."""
        check_intro_events()

    def cleanup():
        """Cleans up the intro menu state."""
        MY.projectiles = []

    def draw(screen):
        """Draws the intro menu state."""
        MY.intro_screen.location = (WINDOW_WIDTH/2, WINDOW_LENGTH/2)
        MY.intro_screen.draw(screen)
