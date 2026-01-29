class emplye:
    a=1

    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")

     
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    

    @name.setter
    def name(self,value):
        self.fname=value.split("  "[0])
        self.lname=value.split("  "[1])


e=emplye()
e.a=24
e.name="harry madarchod "
print(e.fname,e.lname)
e.show()