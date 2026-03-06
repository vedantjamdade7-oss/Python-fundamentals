# Four features in OOPs
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism

# Fetures od OOPs is used to desing software more effectively.

# 1. Abstraction
# Hiding unnecesary deatils from users through class, methods

# class - blueprint or template
class student:
    def __init__(self,name,grade,idcard_no,percentage): # method
        self.name = name # Attribute
        self.grade = grade # Attribute
        self.idcard_no = idcard_no
        self.percentage = percentage 

    def student_details(self): #method - Abstraction
        print(f"{self.name} is in class {self.grade} and has {self.percentage+1} % ")# hidden from users

    def student_idcard(self):
        print(f"student name {self.name} class {self.grade} idcard number {self.idcard}")

# object - instance of class
student1 = student('vedant',11,111,89)
# print(student1.name, student1.grade)

student2 = student('falguni',12,121,94)
# print(student2.name, student2.grade)

student1.student_details()
# student2.student_details()

# student1.student_idcard()
# student2.student_idcard()

# -----------------------------------------------------------------------------------------------------------------------------

# 2. Encapsulation
# Restrict access to certain attributes or methods to protect data and enforce controlled access
class student:
    def __init__(self,name,grade,idcard_no,percentage): # method
        self.name = name # Attribute
        self.grade = grade # Attribute
        self.idcard_no = idcard_no
        self.__percentage = percentage # double underscore ("__") limits access

    def get_percentage(self):
        return self.__percentage
        

    def student_details(self): #method - Abstraction
        print(f"{self.name} is in class {self.grade} and has {self.percentage+1} % ")# hidden from users

    def student_idcard(self):
        print(f"student name {self.name} class {self.grade} idcard number {self.idcard}")

# object - instance of class
student1 = student('vedant',11,111,89)
# print(student1.name, student1.grade)

student2 = student('falguni',12,121,94)
# print(student2.name, student2.grade)

# ----------------------------------------------------------------------------------------------------------------------------------------

# 3. Inheritance - 
# allows one class (child) to reuse the prop and methods of another class (parent).

# Encapsulation
# Restrict access to certain attributes or methods to protect data and enforce controlled access 

# parent class - baap

class student:
    def __init__(self, name, grade, idcard_no, percentage):
        self.name = name
        self.grade = grade
        self.idcard_no = idcard_no
        self.__percentage = percentage  # private attribute

    def get_percentage(self):
        return self.__percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade} and has {self.get_percentage()}%")

    def student_idcard(self):
        print(f"Student name: {self.name}, Class: {self.grade}, ID card: {self.idcard_no}")


# objects
student1 = student("Vedant", 11, 111, 89)
student2 = student("Falguni", 12, 121, 94)


# child class - beta
class Graduatestudent(student):
    def __init__(self, name, grade, idcard_no, percentage, stream):
        super().__init__(name, grade, idcard_no, percentage)
        self.stream = stream  # new attribute

    def student_details(self):
        super().student_details()
        print(f"Stream is {self.stream}")

grad_student1 = Graduatestudent("Karan", 12, 222, 96, "PCM")
grad_student1.student_details()

# -------------------------------------------------------------------------------------------------------------------------------

# 4. Polymorphism
# Allows method in different classes to have same name but different behaviour depending on objects

class student:
    def __init__(self, name, grade, idcard_no, percentage):
        self.name = name
        self.grade = grade
        self.idcard_no = idcard_no
        self.percentage = percentage  # private attribute

    def student_details(self):
        print(f"{self.name} is in class {self.grade} and has {self.percentage}%")

    def student_idcard(self):
        print(f"Student name: {self.name}, Class: {self.grade}, ID card: {self.idcard_no}")


# objects
student1 = student("Vedant", 11, 111, 89)
student2 = student("Falguni", 12, 121, 94)


# child class - beta
class Graduatestudent(student):
    def __init__(self, name, grade, idcard_no, percentage, stream):
        super().__init__(name, grade, idcard_no, percentage)
        self.stream = stream  # new attribute

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage}% and Stream is {self.stream}")


# Object - student class
student1 = student('karan', 11, 89, 77)  # added percentage

# Object - Graduatestudent class
Grad_student1 = Graduatestudent('mahima', 12, 98, 88, 'PCM')  # added percentage

Grad_student1.student_details()
student1.student_details()

