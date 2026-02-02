class Animal:
    
    def __init__(self):
        print("the animal barks ")



class pets(Animal):
    def __init__(self):
        super().__init__()




class Dog(pets):
    @staticmethod
    def bark():
        print("bow bow ! ")



d=Dog()
d.bark()