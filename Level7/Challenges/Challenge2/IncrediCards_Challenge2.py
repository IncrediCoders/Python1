from init import * # Imports code from the init.py file

# Create all of the cards
#TODO: Add the Coded Attack names for each card as the last argument for creating the Card object (the first one is done for you)
annie_conda = Card('Annie Conda', 'python', 'java', 'bash', annie_conda_img, icon_python, 'gain_health', 'Super Squeeze')
bayo_wolf = Card('Bayo Wolf', 'scratch', 'small_basic', 'java', bayo_wolf_img, icon_scratch, 'opponent_tails')
captain_javo = Card('Captain Javo', 'java', 'scratch', 'python', captain_javo_img, icon_java, 'opponent_tails')
cryptic_creeper = Card('Cryptic Creeper', 'bash', 'python', 'small_basic', cryptic_creeper_img, icon_bash, 'extra_hit')
emily_airheart = Card('Emily Airheart', 'small_basic', 'bash', 'scratch', emily_airheart_img, icon_small_basic, 'gain_health')
grafika_turtle = Card('Grafika Turtle', 'small_basic', 'bash', 'scratch', grafika_turtle_img, icon_small_basic, 'extra_turn')
intelli_scents = Card('Intelli-Scents', 'scratch', 'small_basic', 'java', intelli_scents_img, icon_scratch, 'extra_hit')
java_lynn = Card('Java Lynn', 'java', 'scratch', 'python', java_lynn_img, icon_java, 'opponent_tails')
jitter_bug = Card('Jitter Bug', 'java', 'scratch', 'python', jitter_bug_img, icon_java, 'extra_turn')
justin_timbersnake = Card('Justin Timbersnake', 'python', 'java', 'bash', justin_timbersnake_img, icon_python, 'opponent_tails')
mrs_scratcher = Card('Mrs. Scratcher', 'scratch', 'small_basic', 'java', mrs_scratcher_img, icon_scratch, 'extra_hit')
paul_python = Card('Paul Python', 'python', 'java', 'bash', paul_python_img, icon_python, 'extra_hit')
queen_cobra = Card('Queen Cobra', 'python', 'java', 'bash', queen_cobra_img, icon_python, 'extra_turn')
ram_rom = Card('Ram and Rom', 'java', 'scratch', 'python', ram_rom_img, icon_java, 'extra_turn')
sidewinder = Card('Sidewinder', 'python', 'java', 'bash', sidewinder_img, icon_python, 'gain_health')
syntax_turtle = Card('Syntax Turtle', 'small_basic', 'bash', 'scratch', syntax_turtle_img, icon_small_basic, 'extra_turn')
viralmuto = Card('Viralmuto', 'bash', 'python', 'scratch', viralmuto_img, icon_bash, 'extra_hit')
virobotica = Card('Virobotica', 'bash', 'python', 'small_basic', virobotica_img, icon_bash, 'opponent_tails')
virobots = Card('Virobots', 'bash', 'python', 'small_basic', virobots_img, icon_bash, 'extra_turn')
woodchuck_norris = Card('Woodchuck Norris', 'scratch', 'small_basic', 'java', woodchuck_norris_img, icon_scratch, 'gain_health')

DECK = []

# Add all cards to deck
DECK.append(annie_conda)
DECK.append(bayo_wolf)
DECK.append(captain_javo)
DECK.append(cryptic_creeper)
DECK.append(emily_airheart)
DECK.append(grafika_turtle)
DECK.append(intelli_scents)
DECK.append(java_lynn)
DECK.append(jitter_bug)
DECK.append(justin_timbersnake)
DECK.append(mrs_scratcher)
DECK.append(paul_python)
DECK.append(queen_cobra)
DECK.append(ram_rom)
DECK.append(sidewinder)
DECK.append(syntax_turtle)
DECK.append(viralmuto)
DECK.append(virobotica)
DECK.append(virobots)
DECK.append(woodchuck_norris)

random.shuffle(DECK)

class PlayScreen(GameState):
	
	def __init__(self):
		super().__init__()
		self.next_state = "Victory"

		self.tech_attack_button = Button("TechType Attack", X_CENTER-105, 625, 210, 40, ondeck_teal, round_dark_blue, parent = self)	
		self.tech_attack_button.action_params = "tech"	
		#TODO: Copy the code to add the Coded Attack button and the action_params attribute below

		
		#TODO: Change the instructions argument for the Info Box to use the CHALLENGE_INSTRUCTIONS instead
		self.instructions_box = InfoBox(INSTRUCTIONS, dialog_inst, BLACK, (200, 300), (X_CENTER, 200), 200)

		self.coin = Coin(coin_img, (X_CENTER, 475))
		self.turn_counter = 1
		self.flipping = False
		self.tech_attack = False
		self.coded_attack = False
		self.side_up = None
		self.force_tails = False
		
	def start(self, players):
		self.players = players
		self.player1 = players["player1"]
		self.player2 = players["player2"]
		
		self.attacker = self.player1 if self.player1.active_turn else self.player2
		self.defender = self.player1 if not self.player1.active_turn else self.player2
		
		self.player1_card_display = CardDisplay(self.player1, player1_card_display_data)
		self.player2_card_display = CardDisplay(self.player2, player2_card_display_data)

		self.player1_healthbar = Healthbar(self.player1, player1_healthbar_data)
		self.player2_healthbar = Healthbar(self.player2, player2_healthbar_data)
		
		self.player1_ondeck = OnDeck(self.player1, player1_ondeck_data)
		self.player2_ondeck = OnDeck(self.player2, player2_ondeck_data)

		self.dialog_box = DialogBox((200,300), (X_CENTER-100, 50))
		
	def get_event(self, event):
		if not self.flipping:
			self.tech_attack_button.get_event(event)
			self.coded_attack_button.get_event(event)
		self.player1_ondeck.get_event(event)
		self.player2_ondeck.get_event(event)
		
	def button_action(self, params):
		if params == "coded":
			self.coded_attack = True
		self.side_up = self.flip_coin()
		self.coin.set_side(self.side_up)
		self.flipping = True

	def update(self, dt):
		self.player1_healthbar.update()
		self.player2_healthbar.update()
		
		self.player1_ondeck.update()
		self.player2_ondeck.update()
		
		self.player1_card_display.update()
		self.player2_card_display.update()
		
		if self.flipping:
			self.flipping = self.coin.update(dt)
			if not self.flipping:
				self.tech_attack = True
		
		if self.tech_attack:
			offense_card = self.attacker.current_card 
			defense_card = self.defender.current_card
			
			message = add_to_message("", "{}".format(self.turn_counter))
			message = add_to_message(message, "{}".format(self.attacker.name))
			message = add_to_message(message, "{}".format(self.side_up))

			# Tech Type Attack logic
			if not self.coded_attack:
				if self.side_up == 'Heads':
					damage = defense_card.attacked_by(offense_card)
					if damage == 2:
						turn_msg = "{} is resistant to {}'{} attack! They only take 2 damage.".format(defense_card.name, offense_card.name, offense_card.s_flag)
					elif damage == 4:
						turn_msg = "{} is weak to {}'{} attack! They receive 4 damage.".format(defense_card.name, offense_card.name, offense_card.s_flag)
					else:
						turn_msg = "{} took {} damage from {}'{} attack\n".format(defense_card.name, damage, offense_card.name, offense_card.s_flag)
					message = add_to_message(message, turn_msg, defense_card)
				else:
					turn_msg = "{} took no damage from {}\n".format(defense_card.name, offense_card.name)
					message = add_to_message(message, turn_msg)
				
				# Dialog box shows the result of the turn
				self.dialog_box.set_message(message)
				
				# Update player hands
				self.player1.refresh_hand()
				self.player2.refresh_hand()
				
				self.tech_attack = False
				self.turn_counter += 1
						
				# Switch active player
				self.switch_active_player()
			
			# Coded Attack logic
			else:
				#TODO: Add the code to make the defense card take 1 damage (Hint: Cards have a method called take_damage())
				

				# Flip the coin for the offense card's extra effect
				if self.side_up == 'Heads':
					# Execute Coded Attack - four different paths:

					# Extra Hit - This deals 1 more damage to the opponent and switches active player
					if offense_card.coded_type == 'extra_hit':
						#TODO: Add the code to make the defense card take 1 damage 

						turn_msg = "{}'{} {} landed, dealing 2 damage to {} this turn!\n".format(offense_card.name, offense_card.s_flag, offense_card.coded_attack, defense_card.name)
						#TODO: Add the code to switch the active player

					# Extra Turn - This gives the active player an extra turn, does not switch active player
					if offense_card.coded_type == 'extra_turn':
						turn_msg = "{}'{} {} hit - {} took 1 damage and {} gets another turn!\n".format(offense_card.name, offense_card.s_flag, offense_card.coded_attack, defense_card.name, self.attacker.name)
					# Gain Health - This lets the active card (or any other card in the player's hand with damage) to gain 1 HP and switches active player
					if offense_card.coded_type == 'gain_health':
						#TODO: Add the code to make the offense player gain 1 health point (Hint: Players have a method called gain_health())
						healed_card = # Add code here
						if healed_card is None:
							turn_msg = "{}'{} {} worked but all cards had max health!\n".format(offense_card.name, offense_card.s_flag, offense_card.coded_attack)
						else:
							turn_msg = "{}'{} {} worked and {} gained 1 health point back!\n".format(offense_card.name, offense_card.s_flag, offense_card.coded_attack, healed_card.name)
						#TODO: Add the code to switch the active player
						

					# Opponent Tails - This forces the next roll to be a 'Tails' and switches the active player
					if offense_card.coded_type == 'opponent_tails':
						#TODO: Add the code to set the game's attribute for forcing tails to be 'True'
						
						turn_msg = "{}'{} {} strikes - {} will roll tails on the next turn!\n".format(offense_card.name, offense_card.s_flag, offense_card.coded_attack, defense_card.name)
						#TODO: Add the code to switch the active player


				else: 
					# Coded attack fails, defense still takes 1 damage and switch active player
					turn_msg = "{}'{} {} missed - {} took 1 damage.\n".format(offense_card.name, offense_card.s_flag, offense_card.coded_attack, defense_card.name)
					#TODO: Add the code to switch the active player


				# Following needs to happen for every coded attack scenario
				message = add_to_message(message, turn_msg, defense_card)
				self.dialog_box.set_message(message)
				
				self.player1.refresh_hand()
				self.player2.refresh_hand()
				
				#TODO: Add the code to set the game's coded attack attribute to 'False' (Hint: Look at line 70)

				self.tech_attack = False
				self.turn_counter += 1

			winner = self.check_game_end()
			if winner:
				winner.set_as_winner()
				self.done = True
			
	def flip_coin(self):
		if self.force_tails:
			self.force_tails = False
			return "Tails"
		side = "Heads" if random.random() < 0.5 else "Tails"
		return side

	def switch_active_player(self):
		if self.player1.active_turn:
			self.attacker = self.player2
			self.defender = self.player1
		else:
			self.attacker = self.player1
			self.defender = self.player2
		
		self.attacker.active_turn = True
		self.defender.active_turn = False

	def check_game_end(self):
		# Check status of both players, if one player surviving then end the game
		exiting = False
		if not self.player1.active:
		    exiting = self.player2
		elif not self.player2.active:
		    exiting = self.player1

		return exiting
		
	def draw(self, surface):
		super().draw(surface)
		
		if self.turn_counter == 1:
			self.instructions_box.draw(surface)
		self.dialog_box.draw(surface)
		
		self.player1_card_display.draw(surface)
		self.player2_card_display.draw(surface)
		
		self.player1_healthbar.draw(surface)
		self.player2_healthbar.draw(surface)
		
		self.player1_ondeck.draw(surface)
		self.player2_ondeck.draw(surface)
		
		self.coin.draw(surface)
		self.tech_attack_button.draw(surface)
		self.coded_attack_button.draw(surface)
		
states = {
		"Title" : TitleScreen(),
		"GetNames": GetNameScreen(),
		"CoinFlip": CoinFlipScreen(),
		"ChooseHand" : ChooseHandScreen(DECK),
		"Game" : PlayScreen(),
		"Victory" : VictoryScreen()
			}

game = GameRunner(SCREEN, states, "Title")

