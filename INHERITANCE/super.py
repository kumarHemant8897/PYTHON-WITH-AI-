class employee:
    def __init__(self):
        print("this is employe constructor")
    a=1


class programmger(employee):
    def __init__(self):
        print("this is programmer constructor")
    b=2

class manager(programmger):
    def __init__(self):
        super().__init__()   #run its parenet constructor also
        print("this is manager constructor")
    c=3





#o=employee()
#print(o.a)


#o=programmger()
#print(o.a,o.b)


o=manager()
print(o.a,o.b,o.c)