# IncrediCards Quiz Answers

This page includes the answers to the Level 7 IncrediCards Quiz!

**No cheating! Make sure you try to answer the questions before you look up the answers!**

Here are the answers:

1. There are 6 total parameters in the _`Card()`_ function: the name of the card (such as _`'Annie Conda'`_), the card's TechType (such as _`'python'`_), the card's weakness TechType (such as _`'java'`_), the card's resistance TechType that it's stronger against (such as _`'bash'`_), the card image (such as _`annie_conda_img`_), and the TechType icon for that card (such as _`icon_python`_).
2. The second parameter is the card's TechType. An example TechType is _`'python'`_. These TechTypes represent the different coding languages that the cards use.
3. The _`.append()`_ function adds something (in our case, a card variable) to the Deck. For example: _`DECK.append(annie_conda)`_.
4. _`PlayScreen()`_ is one of the game states, which are kind of like modes or screens that the player switches between. The _`PlayScreen()`_ class sets up the graphics on the screen, including the player names, the player cards, the dialog box, the healthbars, the TechType Attack button, the coin, and the On Deck boxes. It also checks if player clicked the TechType Attack button. It determines what messages are that go in the dialog box, and it displays them. Finally, it determines when a turn is over and it switches turns.
5. A class is where you can organize your program in sections, so that you don't have to repeat code. You can then call the class when you need it. (In Python, it's also called an _object_.) In other words, it creates a new object and might include methods and variables.
6. The _`start()`_ method creates the players and sets which of the players is attacking and which one is defending. 
7. The code statement _`self.player1_ondeck.get_event(event)`_ checks if Player 1 clicked on a different "On Deck" card.
8. The _'if self.flipping:'_ block (on Lines 114-117) checks to see if the coin animation has started (because a player clicked the TechType Attack button). If the animation has started, the code checks to see if the animation is done. Then, when the animation finishes, it updates the coin image to show heads or tails, depending on the results of the coin flip. 
10. If you have a resistance to a card's TechType, then your card is stronger (they have a weakness to your card), and you do 4 damage instead of 3.
11. The 6 game states are the _`Title`_ screen, the _`GetNames`_ screen (where you enter your names), the _`CoinFlip`_ screen (where you flip a coin to see who goes first), the _`ChooseHand`_ screen (where you pick which card to start with), the _`Game`_ or Play screen (the main screen where you play the game), and the _`Victory`_ screen (the screen at the end that tells you who won, and where you can choose to play again).
