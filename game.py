import random
from interface import interface

class Game:
	gameover = False
	choices = [
		'Travel',
		'Eat',
		'Fart',
		'Sleep',
		'Give up'
	]

	def __init__(self, config):
		self.player = config['player']

	def start(self):
		interface.printStatus('Player is' + self.player.status)
		while self.gameover == False:
			move = interface.getChoice("What do you want to do?", self.choices)
			interface.printMove(move)

			if (random.randint(1, 10) == 10 or move == 'Give up'):
				self.gameover = True

			if self.gameover == True:
				interface.printGameOver()
				break