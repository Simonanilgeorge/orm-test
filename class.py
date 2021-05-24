class Student:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def insert(self,name):
        print(self.__dict__)
        print(name)


    # @classmethod

student=Student("Simon",24,"abcdsd")

# student.insert("test name")

print(student.__dict__.keys())



