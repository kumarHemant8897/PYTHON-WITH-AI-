class Employee:
   
    language="py"
    salary=12000


    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("this is a dunder method of python ")

    def getinfo(self):
        print(f"the lanuage is {self.language}, and salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning")




harry=Employee("hemat", 13000,"javascript")
print(harry.name,harry.salary,harry.language)
#harry.greet()
#harry.getinfo()
