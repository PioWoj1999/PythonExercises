"""
Practice on private class variables with getters and setters. 
"""

class SupperClass: 
    def __init__(self, a, b, pub) -> None:
        # private
        self.__a = a
        # protected
        self._b = b
        self.pub = pub

    def __str__(self) -> str:
        return "SampleClass"

    def get_a(self): 
        """getter method to get the properties using an object"""
        return self.__a
    
    def set_a(self, num) -> None: 
        """setter method to change the value 'a' using an object"""
        self.__a = num
    
    def __hidden_method(self): 
        """Can be used while unit testing on this object."""
        return "I am a secret!"
    
    def access_hidden_method(self):
        return self.__hidden_method()

    @property
    def total(self): 
        return self.__a + self._b


class SampleClass(SupperClass):
    def __init__(self, a, b, pub) -> None:
        super().__init__(a, b, pub)

    def protected_variables_fail(self) -> int: 
        return self._b + self.__a
    
    def protected_variables_success(self) -> int: 
        return self._b + self.get_a()

def main(): 
    privateVariables = SupperClass(5, 10, "Test")
    print(privateVariables.get_a())
    privateVariables.set_a(num=55)
    print(privateVariables.get_a())

    try: 
        # private variable can't be read/passed
        print(privateVariables.__a)
    except AttributeError: 
        pass

    print(f"Public variable access: {privateVariables.pub}")
    try: 
        print(privateVariables.__hidden_method())
    except AttributeError: 
        print("It can't read private method, but public method can access private one within its class.")    
        print(privateVariables.access_hidden_method())
    
    print(f"Total of class {privateVariables}-privateVariables is: {privateVariables.total}\n")


    protected_var = SampleClass(5, 10, "Test")
    try: 
        print(f"Sum of protected: {protected_var.protected_variables_fail()}")
    except AttributeError: 
        print("It is not possible to read private variable without getter, even in inherence.\nContinue ...")
    finally: 
        print(f"Sum of protected: {protected_var.protected_variables_success()}")

if __name__ == "__main__": 
    main()