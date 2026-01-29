class programmer:
    comapny="microsoft"
    salary=450000
    poistion="SDE"

    def __init__(self,name,salary,poistion):
        self.name=name
        self.salary=salary
        self.poistion=poistion


        
p=programmer("p", 50000,"SENIOR SDE")
print(p.name,p.salary,p.poistion)

hemant=programmer("Hemant", 450000,"SENIOR software SDE")
print(hemant.name,hemant.salary,hemant.poistion)



