# SpaceWars Quiz Answers

This page includes the answers to the Level 4 SpaceWars Quiz!

**No cheating! Make sure you try to answer the questions before you look up the answers!**

Here are the answers:

1. The asterisk at the end of the code line:  _`from init import *`_ means that we are importing all the functions and variable in that file. 
2. _`def update(delta_time)`_ describes the time difference between the previous frame that was drawn and the current frame. This is used in our program to see how much elapsed time there is for the program to run. 
3. An event is when the player interacts with the keyboard. An example would be pressing the "A" key or the "space bar" on the keyboard.
4. The two keys on the keyboard that make the ship fire in this program are the "space bar" and the "Enter" key.
5. An "Elif" statement will come after an "if" statement and you can use it to check for a specific statement to be true, once an elif statement is true, then all the subsequent elifs will not run in the program. 
6. An example of the code that you would write to make Player 1's ship move and rotate would be: _`MY.player1.add_rotation(-ship_rotate * delta_time)`_
7. The code line: _`if key_held_down()`_, checks to see if the button inside the parentheses was pressed. An example of what could go in the parentheses is _`pygame.K_s`_.
8. The way that you would write a line code to increase Player 1's velocity would be _`MY.player1.add_velocity(MY.player1.add_rotation, -ship_accel, ship_max_speed)`_
9. State is everything that the computer remembers about the variables and objects in your game, at one point in time. 
10. An example of state in this program would be when you and Player 2 are firing bullets for the ship, the code for what makes the bullets fire is a part of the state.
