class Student:
    def __init__(self,name,rollno,age,branch):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.branch=branch
s1=Student("Karan",90001,19,"ECE")
s2=Student("Maran",90002,18,"EEE")
s3=Student("Saran",90003,22,"EIE")
print("name - ",s1.name)
print("rollno - ",s1.rollno)
print("age - ",s1.age)
print("branch - ",s1.branch)
print("\n")
print("name - ",s2.name)
print("rollno - ",s2.rollno)
print("age - ",s2.age)
print("branch - ",s2.branch)
print("\n")
print("name - ",s3.name)
print("rollno - ",s3.rollno)
print("age - ",s3.age)
print("branch - ",s3.branch)
