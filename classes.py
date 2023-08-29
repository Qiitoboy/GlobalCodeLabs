from datetime import datetime
class Person:
    def --init--(self, name,date_Of_Birth):
        self.name = name
        self.date_Of_Birth = date_Of_Birth
    

    
def speak(self):
    print("hello")
def walk(self):
    print("Walking away")
def get_Name(self):
    return self.name
def get_Age(self):
    today = datetime.today()
    birthdate = datetime.strptime(self.dob, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
    

class Student(Person)



