from init import * # Gives us many helpful functions

"""Loads the background and images"""
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

"""Stores character text into variables"""
text_annie_conda  = "Hello! I'm Annie Conda. \nI come from Sanfran-Hissco, Cowlifornia. I've done a little coding. My favorite musician is Justin Timbersnake. I'm also partial to Hissy Elliott. My favorite Pigxar movie is Rattle-toulle. I love to make trivia games and word games. "
text_bayo_wolf  = "I'm Bayo Wolf, from Little Squawk, Barkansas. I'm the best at SpaceWars and great at Mega Mechs in my Grendel mech. My favorite movies are The Dogfather, Jurassic Bark, Citizen Canine, and Stall Wars: The Empire Strikes Cats. My top actors are Brad Pitbull, Howly Berry, and Sandra Bulldog. "
text_grafika_turtle  = "My name is Grafika Turtle. I live here, in Red-mutt, Washeepton. Now I get to go to school with my best friend. Hi, Paul! I love the movie Wizard of Paws, and my favorite artist is Pablo Pigcasso. I like coding in Turtle Graphics, and my brother Syntax and I are pretty good at coding card games. "
text_intelli_scents  = "Hi. I'm Intelli-Scents from Minnea-pawlis, Minnow-soda. My top movies are Hack to the Future, Mission Impawsible with Eat'n Hunt, and Hair-Spay. My top artist is Vincent van Gopher, top book is The Time Machine by H.G. Gills, and my favorite neurologist is Digmund Freud.  "
text_java_lynn  = "I'm Java Lynn, also from Minnea-pawlis. I shop at Blooming Tails and read Vanity Fur. Top movies are Hairy Otter 8, Catsaway with Tomcat Hanks, and the Sound of Mew-sic. My actors are Bill Furry and Scarlett Johamster. I love the art \"Squirrel with the Acorn Earrings.\" "
text_captain_javo  = "I'm Captain Javo, from Indiana-pawlis, Fin-diana. The movies I like are The Fast and Furry-us, Paws, and Clawshank Redemption. My actors are Woodchuck Norris, Billy Grrr-ystal, and Will Ferret. My musicians are Kitty Purry and Britney Ears. My favorite programming language is Java. "
text_jitter_bug  = "I am Jitter Bug, from Ant-aheim, Cowlifornia. My favorite movies are Mrs. Doubtspider and Twi-mite. I love the Stall Wars character Luke Flywalker. My top actors are Kristin Ear-Wiig and Molly Ringworm. My favorite musicians are Beeyonce, Flyley Flyrus, and Nine-Inch Snails. "
text_paul_python  = "Hi. I'm Paul Python. My home is just over the bridge in Sea-cattle. Mega Mechs is my favorite game, and the reason why I'm here, by winning the tournament! I love the actor David Hisselhoff, and I agree with Annie that Justin Timbersnake makes awesome music! But I also like White Snake. "
text_quackintosh = "Hello. I'm Quackintosh, from nearby Bill-view, Washeepton. My top actors are Audrey Honkburn, Goose Willis, Squawkin Phoenix, Robird De Niro, Hennifer Lawrence, and Woody Owlen. My musicians are Swan Bon Jovi, Michael Quackson, and Ozzy Ostrich. My top art is \"Son of Duck.\" "
text_sb_turtle = "Hey. I'm SB Turtle, from New-ark, Moo Jersey. My top actresses are Shelly Long and Zooey Deshell. I'm a founding member of the Shell Scouts, and my favorite programming language is Microsoft Small Basic. Oh, and I grow into a giant monster, but that's for a different book. "
text_sidewinder = "I'm SideWinder, from Salt-Snake City, Mewtah. I'm the best at SpaceWars, despite what Bayo thinks. My favorite movie is Snakes on a Glider, my favorite actor is Sylvester Stallion, and my favorite musician is Nine-Inch Snails. Jitter Bug has good taste. "
text_syntax_turtle = "What's up? Syntax Turtle in the house. I'm from here, Red-Mutt, with my twin sis Grafika. My favorite actress is Natalie Porkman, and my favorite artist is Lizardnardo Da Vinci. My top games are \"Skate and Fly\" and Porkymon, and I'm looking forward to making a Codu Kids card game! "

"""We assign our character and text variables"""
current_character = annie_conda
current_text = text_annie_conda

while running:
    display(background, current_text, current_character)
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_character = annie_conda
                current_text = text_annie_conda
            if event.key == pygame.K_2:
                current_character = bayo_wolf
                current_text = text_bayo_wolf
            if event.key == pygame.K_3:
                current_character = grafika_turtle
                current_text = text_grafika_turtle
            if event.key == pygame.K_4:
                current_character = intelli_scents
                current_text = text_intelli_scents
            if event.key == pygame.K_5:
                current_character = java_lynn
                current_text = text_java_lynn 
            if event.key == pygame.K_6:
                current_character = captain_javo
                current_text = text_captain_javo
            if event.key == pygame.K_7:
                current_character = jitter_bug
                current_text = text_jitter_bug
            if event.key == pygame.K_8:
                current_character = paul_python
                current_text = text_paul_python
            if event.key == pygame.K_9:
                current_character = quackintosh
                current_text = text_quackintosh
            if event.key == pygame.K_0:
                current_character = sb_turtle
                current_text = text_sb_turtle
            if event.key == pygame.K_q:
                current_character = sidewinder
                current_text = text_sidewinder
            if event.key == pygame.K_w:
                current_character = syntax_turtle
                current_text = text_syntax_turtle
pygame.quit()