class Object_Oriented:
	def __init__(self, oo_class, *args):
		if oo_class == "School":
			self.class_name = "School"
			self.oo_name = args[0]
			
			[org.eclipse.emf.ecore.impl.DynamicEObjectImpl@69bc4f0a (eClass: org.eclipse.emf.ecore.impl.EClassImpl@6ff84d82 (name: Attribute) (instanceClassName: null) (abstract: false, interface: false)), org.eclipse.emf.ecore.impl.DynamicEObjectImpl@54dc2235 (eClass: org.eclipse.emf.ecore.impl.EClassImpl@34efeb6e (name: Reference) (instanceClassName: null) (abstract: false, interface: false)), org.eclipse.emf.ecore.impl.DynamicEObjectImpl@7965f171 (eClass: org.eclipse.emf.ecore.impl.EClassImpl@6ff84d82 (name: Attribute) (instanceClassName: null) (abstract: false, interface: false))]
			
			
			
			
		if oo_class == "Student":
			self.class_name = "Student"
			self.oo_name = args[0]
			
			[org.eclipse.emf.ecore.impl.DynamicEObjectImpl@40bac4b6 (eClass: org.eclipse.emf.ecore.impl.EClassImpl@6ff84d82 (name: Attribute) (instanceClassName: null) (abstract: false, interface: false))]
			
			
			
			
		if oo_class == "Person":
			self.class_name = "Person"
			self.oo_name = args[0]
			
			[org.eclipse.emf.ecore.impl.DynamicEObjectImpl@4bf517b4 (eClass: org.eclipse.emf.ecore.impl.EClassImpl@6ff84d82 (name: Attribute) (instanceClassName: null) (abstract: false, interface: false))]
			
			
			
			
		if oo_class == "Employee":
			self.class_name = "Employee"
			self.oo_name = args[0]
			
			[org.eclipse.emf.ecore.impl.DynamicEObjectImpl@7e0d4975 (eClass: org.eclipse.emf.ecore.impl.EClassImpl@6ff84d82 (name: Attribute) (instanceClassName: null) (abstract: false, interface: false))]
			
			
			
			
		if oo_class == "Teacher":
			self.class_name = "Teacher"
			self.oo_name = args[0]
			
			[org.eclipse.emf.ecore.impl.DynamicEObjectImpl@2835c1bc (eClass: org.eclipse.emf.ecore.impl.EClassImpl@34efeb6e (name: Reference) (instanceClassName: null) (abstract: false, interface: false))]
			
			
			
			
		if oo_class == "Class":
			self.class_name = "Class"
			self.oo_name = args[0]
			
			[org.eclipse.emf.ecore.impl.DynamicEObjectImpl@3e3c2f78 (eClass: org.eclipse.emf.ecore.impl.EClassImpl@34efeb6e (name: Reference) (instanceClassName: null) (abstract: false, interface: false))]
			
			
			
			
        #self.attribute = {}
        #self.reference = {}
        
        

        #self.attribute = self.get_attributes(**kwargs)
        #self.reference = self.get_reference(**kwargs)
	'''
    def get_features(self, *args):
    	

        if kwargs:
            for key, value in kwargs.items():
                self.attribute[key] = value
        return self.attribute

    def get_reference(self, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                self.reference[key] = value
        return self.reference
	'''
	
def main():
    
    my_school = Object_Oriented("School", "UQAC", "xxx", "xxxx", "xxxx")


    # Access attributes
    print(f"My school's name is {my_school.oo_name}.")

if __name__ == "__main__":
    main()