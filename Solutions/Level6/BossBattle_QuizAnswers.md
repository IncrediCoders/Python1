# Boss Battle Quiz Answers

This page includes the answers to the Level 6 Boss Battle Quiz!

**No cheating! Make sure you try to answer the questions before you look up the answers!**

Here are the answers:

1. The process where your game checks whether an object has collided with another object. In this case, we check if Paul Python has collided with the walls. 
2. The code you write to make sure that Paul does not run through the right of the screen is _`if MY.player.location.x > WINDOW_WIDTH - MY.wall_height;`_ then on the next line, indented you would write, _`MY.player.location.x = WINDOW_WIDTH - MY.wall_height;`_.
3. The code you write to make sure that Paul does not run through the top of the screen is _`if MY.player.location.y > WINDOW_WIDTH - MY.wall_height;`_ then on the next line, indented you would write, _`MY.player.location.y = WINDOW_WIDTH - MY.wall_height;`_.
4. The code you write to make sure that Paul does not run through the bottom of the screen is _`if MY.player.location.y > WINDOW_WIDTH - (MY.wall_height + 20);`_ then on the next line, indented you would write, _`MY.player.location.y = WINDOW_WIDTH - (MY.wall_height + 20);`_.
5. _`handle-pillar_collision()`_ prevents Paul from walking through pillars in this program. 
6. If _`MY.player.collides_with(MY.boss)`_  is true, Paul will lose health.
7. _`player_pain_anim()`_ is the function that switches Paul's art to show his pain animation, because Paul takes damage when he collides with the Creeper.  
8. The code command that subtracts one health from Paul in this program is _` MY.player_health -= 1`_.
9. A hitbox is the invisible box-like area in front of a character that shows the range they can attack. In our case, this is the range in front of Paul Python, where he can hit the Creeper with a melee attack. 
10. You set the ".active" attribute to False by writing out "= False".
