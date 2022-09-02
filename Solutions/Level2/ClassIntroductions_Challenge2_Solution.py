from init import * # Gives us many helpful functions

# Loads the background and images
background = load_file("Assets/Background.png")
annie_conda = load_file("Assets/AnnieConda.png")
bayo_wolf = load_file("Assets/BayoWolf.png")
grafika_turtle = load_file("Assets/GrafikaTurtle.png")
intelli_scents = load_file("Assets/IntelliScents.png")
java_lynn = load_file("Assets/JavaLynn.png")
captain_javo = load_file("Assets/CaptainJavo.png")
jitter_bug = load_file("Assets/JitterBug.png")
paul_python = load_file("Assets/PaulPython.png")
quackintosh = load_file("Assets/Quackintosh.png")
sb_turtle = load_file("Assets/SBTurtle.png")
sidewinder = load_file("Assets/SideWinder.png")
syntax_turtle = load_file("Assets/SyntaxTurtle.png")
ram_rom = load_file("Assets/RAMROM.png")
amphib_ian = load_file("Assets/AmphibIan.png")

# Stores the character text into the variables
text_annie_conda  = "Hello! I'm Annie Conda. \nI come from Sanfran-Hissco, Cowlifornia. I've done a little coding. My favorite musician is Justin Timbersnake. I'm also partial to Hissy Elliott. My favorite Pigxar movie is Rattle-touille. I love to make trivia games and word games. "
text_bayo_wolf  = "I'm Bayo Wolf, from Little Squawk, Barkansas. I'm the best at SpaceWars and great at Mega Mechs in my Grendel mech. My favorite movies are The Dogfather, Jurassic Bark, Citizen Canine, and Stall Wars: The Empire Strikes Cats. My top actors are Brad Pitbull, Howly Berry, and Sandra Bulldog. "
text_grafika_turtle  = "My name is Grafika Turtle. I live here, in Red-mutt, Washeepton. Now I get to go to school with my best friend. Hi, Paul! I love the movie Wizard of Paws, and my favorite artist is Pablo Pigcasso. I like coding in Turtle Graphics, and my brother Syntax and I are pretty good at coding card games. "
text_intelli_scents  = "Hi. I'm Intelli-Scents from Minnea-pawlis, Minnow-soda. My top movies are Hack to the Future, Mission Impawsible with Eat'n Hunt, and Hair-Spay. My top artist is Vincent van Gopher, top book is The Time Machine by H.G. Gills, and my favorite neurologist is Digmund Freud.  "
text_java_lynn  = "I'm Java Lynn, also from Minnea-pawlis. I shop at Blooming Tails and read Vanity Fur. Top movies are Hairy Otter 8, Catsaway with Tomcat Hanks, and the Sound of Mew-sic. My actors are Bill Furry and Scarlett Johamster. I love the art \"Squirrel with the Acorn Earrings."
text_captain_javo  = "I'm Captain Javo, from Indiana-pawlis, Fin-diana. The movies I like are The Fast and Furry-us, Paws, and Clawshank Redemption. My actors are Woodchuck Norris, Billy Grrr-ystal, and Will Ferret. My musicians are Kitty Purry and Britney Ears. My favorite programming language is Java. "
text_jitter_bug  = "I am Jitter Bug, from Ant-aheim, Cowlifornia. My favorite movies are Mrs. Doubtspider and Twi-mite. I love the Stall Wars character Luke Flywalker. My top actors are Kristin Ear-Wiig and Molly Ringworm. My favorite musicians are Beeyonce, Flyley Flyrus, and Nine-Inch Snails. "
text_paul_python  = "Hi. I'm Paul Python. My home is just over the bridge in Sea-cattle. Mega Mechs is my favorite game, and the reason why I'm here, by winning the tournament! I love the actor David Hisselhoff, and I agree with Annie that Justin Timbersnake makes awesome music! But I also like White Snake. "
text_quackintosh = "Hello. I'm Quackintosh, from nearby Bill-view, Washeepton. My top actors are Audrey Honkburn, Goose Willis, Squawkin Phoenix, Robird De Niro, Hennifer Lawrence, and Woody Owlen. My musicians are Swan Bon Jovi, Michael Quackson, and Ozzy Ostrich. My top art is \"Son of Duck.\" "
text_sb_turtle = "Hey. I'm SB Turtle, from New-ark, Moo Jersey. My top actresses are Shelly Long and Zooey Deshell. I'm a founding member of the Shell Scouts, and my favorite programming language is Microsoft Small Basic. Oh, and I grow into a giant monster, but that's for a different book. "
text_sidewinder = "I'm SideWinder, from Salt-Snake City, Mewtah. I'm the best at SpaceWars, despite what Bayo thinks. My favorite movie is Snakes on a Glider, my favorite actor is Sylvester Stallion, and my favorite musician is Nine-Inch Snails. Jitter Bug has good taste. "
text_syntax_turtle = "What's up? Syntax Turtle in the house. I'm from here, Red-Mutt, with my twin sis Grafika. My favorite actress is Natalie Porkman, and my favorite artist is Lizardnardo Da Vinci. My top games are \"Skate and Fly\" and Porkymon, and I'm looking forward to making an IncrediCards game! "
text_ram_rom = "Heya! We're RAM and ROM. We came from the other side of the country, Woolshington DC. We like Meryl Sheep, Dustin Hoofman, and Eva Longhornia. Our favorite musician is Lady Baa-Baa, and our sensei is the Dali Llama. We're working on a top-secret project! "
text_amphib_ian  = "Yo, yo. What's hopping, peeps? Name's Amphib Ian. My launchpad is Croaklahoma City. My choice singer is Demi Lovatoad. And my fave artwork is \"Mourning Son\" by Edwart Hopper. My go-to game to code is Froggy Road. That's it. I'll catch you on the flip flop! "


# Initializes the lists
CHARACTERS = []
# Uncommented the line below to initialize the TEXT list
TEXT = []

# Adds the characters and text to the lists
CHARACTERS.append(annie_conda)
TEXT.append(text_annie_conda)

# Uncommented the two lines below
CHARACTERS.append(bayo_wolf)
TEXT.append(text_bayo_wolf)

# Added the rest of the characters to the lists
CHARACTERS.append(grafika_turtle)
TEXT.append(text_grafika_turtle)
CHARACTERS.append(intelli_scents)
TEXT.append(text_intelli_scents)
CHARACTERS.append(java_lynn)
TEXT.append(text_java_lynn)
CHARACTERS.append(captain_javo)
TEXT.append(text_captain_javo)
CHARACTERS.append(jitter_bug)
TEXT.append(text_jitter_bug)
CHARACTERS.append(paul_python)
TEXT.append(text_paul_python)
CHARACTERS.append(quackintosh)
TEXT.append(text_quackintosh)
CHARACTERS.append(sb_turtle)
TEXT.append(text_sb_turtle)
CHARACTERS.append(sidewinder)
TEXT.append(text_sidewinder)
CHARACTERS.append(syntax_turtle)
TEXT.append(text_syntax_turtle)
CHARACTERS.append(ram_rom)
TEXT.append(text_ram_rom)
CHARACTERS.append(amphib_ian)
TEXT.append(text_amphib_ian)

running = True
# Starts at the first character in the list
index_number = 0
while running:
    current_character = CHARACTERS[index_number]
    current_text = TEXT[index_number]
    display(background, current_text, current_character)
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN: # Checks if the player presses a key

            # Wrote two lines that check if the player presses the RIGHT key, to go to the next character
            if event.key == pygame.K_RIGHT:
                index_number = index_number + 1

            # Wrote two lines that check if the player presses the LEFT key, to go to the previous character
            if event.key == pygame.K_LEFT:
                index_number = index_number - 1

    # If we reach the end of the list, we start from the beginning again
    if index_number == 14: # This if-statement checks if "index_number" is set to the last character in the list
        index_number = 0 # This statement sets "index_number" back to the first character in the list
    if index_number == -1: # This if-statement checks if "index_number" is set to the first character in the list
        index_number = 13 # This statement sets "index_number" to the last character in the list

pygame.quit()
