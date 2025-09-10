
class School:
	def __init__(self, *args):
		self.args_counter = 0
		self.school_id = args[self.args_counter]
		self.args_counter += 1
		self.address = args[self.args_counter]
		self.args_counter += 1
		self.students_id = args[self.args_counter]
		self.args_counter += 1
		self.postCodesAccepted = args[self.args_counter]

