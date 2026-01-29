
def greet():
    print("hiii")
    pass
greet()


def check_whether():
    temp=24
    if temp >=25:
        print("too hot today")
    else:
        print("its normal")
    
check_whether()
    



#function with parameters

def intro(name,surnmae):
    print(f"Hi my name is {name} {surnmae}")

intro("Han","fast")
print("\n")
print("\n")
print("\n")


def calculate_total(price,tax_rate,discount):
    gst=price*tax_rate/100
    final_price=price+gst-discount
    print(f"the final price of the product after discoutn is {final_price}")


calculate_total(100,18,5)
calculate_total(500,200,50)
calculate_total(160,18,57)
calculate_total(170,18,53)

print("\n")
print("\n")
print("\n")
print("\n")









#LOCAL VS GLOBAL VARIABLE 

speed=45 #gloabla variable

def accident():
    car="red"
    if speed >=45:
        print("the bike will skid")
    else:
        print("the bike will run safely")



def fine():
    if speed <=45:
        print(f"ther will no fine ")
    else:
        print("there will be fine ")


accident()
fine()


print("\n")
print("\n")








#FUNCTION WITH RETURN VALUES

def add(a,b):
   print(a+b)

add(5,10)

def add_print(a,b):
    return a+b

print(f"the total is {add_print(4,6)}")


#area of rectangel

def calculate(height,width):

    area=height * width
    area*= 1.05
    return area

total_area=calculate(4,10)
print(f"the total size of the room is {total_area} sq fts")

