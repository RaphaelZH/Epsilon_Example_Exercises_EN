class Person:
	def __init__(self, *args):
		i = 0
		self.details = args[i]
		i += 1
	
def main():
    my_school = Person("School", "UQAC", "555 Bd de l'Université, Chicoutimi, QC G7H 2B1", "Labubu", "")

    print(f"My school's name is {my_school.oo_name}.")
    print(f"My school's address is {my_school.attribute['address']}.")
    print(f"{my_school.reference['students']} is one of the students from my school.")

if __name__ == "__main__":
    main()