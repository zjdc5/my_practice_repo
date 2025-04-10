'''
1. Create a class called Student in a file called student.py
The class Student should have the following instance variables:
• fname – first name of student
• lname – first name of student
• id – student id
• energy_level – the initial value for this is 10.

The Student class should have the following class methods:
• __init__ - the init method should have the fname, lname, id, and
energy_level as parameters to initialize the Student. The default value
for energy_level should be 10.
• __str__ - the str method should return “lname: id”
• greeting – this prints a greeting said by the student.
• take_exam – this method subtracts 1 from the student’s energy level.
• get_energy_level – method returns current energy level of student.
'''
class Student:
    def __init__(self, lname, fname, id, energy_level = 10):
        self.lname = lname
        self.fname = fname
        self.id = id

    def __str__(self):
        return f"{self.lname}: {self.id}"
    
    def greeting(self, greeting):
        print(self.greeting)

    def take_exam(self):
        self.energy_level = self.energy_level - 1
    
    def get_energy_level(self):
        return self.energy_level
    
    



