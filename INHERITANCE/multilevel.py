class employee:
    a=1

class programmger(employee):
    b=2

class manager(programmger):
    c=3





o=employee()
print(o.a)


o=programmger()
print(o.a,o.b)


o=manager()
print(o.a,o.b,o.c)