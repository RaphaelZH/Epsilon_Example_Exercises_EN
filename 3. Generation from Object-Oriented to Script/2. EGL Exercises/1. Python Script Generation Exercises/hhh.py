class Object_Oriented:
    def __init__(self, oo_class, *args, **kwargs):
        self.class_name = oo_class.name
        self.attribute = {}
        self.reference = {}

        self.attribute = self.get_attributes(**kwargs)
        self.reference = self.get_reference(**kwargs)
        
    def get_attributes(self, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                self.attribute[key] = value
        return self.attribute

    def get_reference(self, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                self.reference[key] = value
        return self.reference

def main():
    """
    The main function to demonstrate the Dog class.
    """
    # Create instances of the Dog class
    my_dog = Object_Oriented("Buddy", "Golden Retriever")
    another_dog = Object_Oriented("Lucy", "Labrador")

    # Call methods on the instances
    my_dog.bark()
    another_dog.describe()

    # Access attributes
    print(f"My dog's name is {my_dog.name}.")
    print(f"Another dog's breed is {another_dog.breed}.")

if __name__ == "__main__":
    main()