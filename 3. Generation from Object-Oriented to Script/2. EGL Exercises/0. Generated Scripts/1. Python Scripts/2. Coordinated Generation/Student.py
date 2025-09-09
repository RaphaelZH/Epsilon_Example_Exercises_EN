class Student(Person):
	def __init__(self, *args):
		super().__init__()
		self.args_counter +=1
		self.student_id = args[self.args_counter]
		i += 1
		self.grade = args[self.args_counter]
