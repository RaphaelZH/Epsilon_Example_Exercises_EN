from Employee import Employee
class Teacher(Employee):
	def __init__(self, *args):
		super().__init__(*args)
		self.args_counter +=1
		self.teacher_id = args[self.args_counter]
		self.args_counter += 1
		self.teaches_id = args[self.args_counter]
