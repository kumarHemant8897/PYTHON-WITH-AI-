class Employee:
   
    language="py"
    salary=12000

    def getinfo(self):
        print(f"the lanuage is {self.language}, and salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning")




harry=Employee()
harry.greet()
harry.getinfo()
