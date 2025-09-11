class Person:
	def __init__(self, *args):
		self.args_counter = 0
		self.person_id = args[self.args_counter]
		self.args_counter += 1
		self.details = args[self.args_counter]

