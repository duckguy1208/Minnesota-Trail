import inquirer

class Interface:
	def askQuestion(self, question):
		questions = [
			inquirer.Text('answer', message=question)
		]
		response = inquirer.prompt(questions)
		return response['answer']
	
	def getChoice(self, question, options):
		questions = [
			inquirer.List(
				"choice",
				message=question,
				choices=options,
			),
		]
		response = inquirer.prompt(questions)
		return response['choice']
	
	def getName(self):
		return self.askQuestion('What is your name?')
	
	def getProfession(self):
		return self.getChoice("What is your profession?", ["Farmer", "Carpenter", "Banker"])
	
	def printLine(self):
		print('==============================================================')
		
	
	def printMove(self, move):
		self.printLine()
		print('Player chose: ' + move)
		self.printLine()

	def printGameOver(self):
		self.printLine()
		print('   Game Over   ')
		self.printLine()

	def printWelcome(self):
		self.printLine()
		print('   Welcome to Minnesota Trail   ')
		self.printLine()

	def printStatus(self, status):
		print(status)

interface = Interface()