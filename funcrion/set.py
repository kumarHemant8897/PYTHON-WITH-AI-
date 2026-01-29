




def sum(n):
    if(n==1):
        return 1
    else:
        return sum(n-1)+n

print(sum(4))



def pattern(n):
    if(n==0):
        return
    else:
        print(" * " *n )
        pattern(n-1)


pattern(5)




def multiplication(n):
    if(n==0):
    
        return 0
     
    for i in range(1,11):
        print(f" {n} x {i} = {n*i}")


multiplication(5)
    
        