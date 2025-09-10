from Person import Person
class Employee(Person):
	def __init__(self, *args):
		super().__init__(*args)
		self.args_counter +=1
		self.employee_id = args[self.args_counter]
		self.args_counter += 1
		self.salary = args[self.args_counter]

