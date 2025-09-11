from Person import Person

class Student(Person):
	def __init__(self, *args):
		super().__init__(*args)
		self.args_counter +=1
		self.student_id = args[self.args_counter]
		self.args_counter += 1
		self.grade = args[self.args_counter]

