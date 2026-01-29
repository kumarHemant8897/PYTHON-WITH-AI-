def avrage_calulate():
    a=int(input("enter the first number : "))
    b=int(input("enter the second number : "))
    c=int(input("enter the third number : "))

    avrage=(a+b+c)/3

    print(f"the avrage is : {avrage}")



#avrage_calulate()


def greet(name, ending,gali="teriii"):
    print("goof morning , " + name + ending + gali)
    return 5

#greet("Hemnat", "chalo chai")




def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num-1)
      
    
   


num=int(input("enter the numbr u want factorial:  "))
answer =factorial(num)
print(f"anwer is: "  ,  {answer})