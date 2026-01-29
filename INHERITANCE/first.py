class employee:
    comapny="ITC -> "
    name="default"

    def show(self):
        print(f"the name of the employee is {self.name}, and the company is {self.comapny}")
        

class codeer:
    language="python"

    def persoanllang(self):
        print(f"the personal lanuage is  is {self.language}")



class Programmer(codeer,employee):
    comapny="itc info tech pvt ltd "

    def showlang(self):
        print(f"the lanuage is {self.name}, and he is good with {self.language}")




a=employee()
b=Programmer()

b.show()
b.showlang()
b.persoanllang()
    