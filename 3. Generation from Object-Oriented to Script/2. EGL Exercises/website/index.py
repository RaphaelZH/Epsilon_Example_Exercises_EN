class Object_Oriented:
	def __init__(self, oo_class, *args):
		if oo_class == "School":
			i = 0
			self.class_name = "School"
			self.oo_name = args[i]
			self.attribute = {}
			self.reference = {}
			i += 1
			self.attribute["address"] = args[i]
			i += 1
			self.reference["students"] = args[i]
			i += 1
			self.attribute["postCodesAccepted"] = args[i]
		if oo_class == "Student":
			i = 0
			self.class_name = "Student"
			self.oo_name = args[i]
			self.attribute = {}
			self.reference = {}
			i += 1
			self.attribute["grade"] = args[i]
		if oo_class == "Person":
			i = 0
			self.class_name = "Person"
			self.oo_name = args[i]
			self.attribute = {}
			self.reference = {}
			i += 1
			self.attribute["details"] = args[i]
		if oo_class == "Employee":
			i = 0
			self.class_name = "Employee"
			self.oo_name = args[i]
			self.attribute = {}
			self.reference = {}
			i += 1
			self.attribute["salary"] = args[i]
		if oo_class == "Teacher":
			i = 0
			self.class_name = "Teacher"
			self.oo_name = args[i]
			self.attribute = {}
			self.reference = {}
			i += 1
			self.reference["teaches"] = args[i]
		if oo_class == "Class":
			i = 0
			self.class_name = "Class"
			self.oo_name = args[i]
			self.attribute = {}
			self.reference = {}
			i += 1
			self.reference["students"] = args[i]
		
	
def main():
    
    my_school = Object_Oriented("School", "UQAC", "xxx", "xxxx", "xxxx")


    # Access attributes
    print(f"My school's name is {my_school.oo_name}.")
    print(f"My school's address is {my_school.attribute['address']}.")
    print(f"{my_school.reference['students']} is one of the student from my school.")

if __name__ == "__main__":
    main()