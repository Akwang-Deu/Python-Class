class Student:
    school = "AkiraChix"
    def __init__(self, first_name,last_name,age, country,code):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.country= country
        self.code= code

    def greet_student(self):
        greeting = f"hello {self.first_name},welcome to {self.school}.Your code is {self.code}"
        return greeting

    def student_birth_year(self):
        birth_year = f"Hey {self.first_name}, you were born in {2024-self.age}"
        return greeting

    def student_initials(self):
        initials = f"Your initials are {self.first_name[0]} and {self.last_name[0]}"
        return initials

    def studennt_full_name(self):
        full_name= f"My name {self.first_name} {self.last_name}"
        return full_name

    def enroll_student(self):
        enrollment= f"Hello {self.last_name} {self.last_name} you have been seelected to join {self.school}"
        return enrollment



