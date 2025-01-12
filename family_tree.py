# parent class of family tree

class Family:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    
    def summary(self):
        return f'{self.firstName} {self.lastName} is {self.age} years old'
