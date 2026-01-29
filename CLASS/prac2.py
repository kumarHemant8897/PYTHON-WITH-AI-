class calculator:
    def __init__(self,n):
        self.n=n

    
    def squre(self):
        print(f"the squre is {self.n * self.n}")

    @staticmethod
    def greet():
        print("hello sir")

    def cube(self):
        print(f"the cube is {self.n * self.n * self.n}")

    def root(self):
        print(f"the root is {self.n ** 1/2}")



    


a=calculator(4)
a.greet()
a.squre()
a.cube()
a.root()