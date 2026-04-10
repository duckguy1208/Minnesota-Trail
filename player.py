class Player:
	status = 'fine'

	def __init__(self, config):
		self.name = config['name']
		self.profession = config['profession']

	def getInfo(self):
		return 'Your name is ' + self.name + ' and you are a ' + self.profession