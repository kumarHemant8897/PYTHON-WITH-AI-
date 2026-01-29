name="Hemant"
name="dev"
print(name)

num1=5
num2=5
print(num1+num2)

power=10**2
print(power)


#STRING
string="my name is Hemant"
sentence="he abuse me alot after marriage"
print(sentence)

firstName="dave"
lastName="dev"
fullName=firstName +" "+ lastName
print(fullName)


#string manulplation

long_dash="-"*10
print(long_dash)

length=len(long_dash)
print(length)








#BOOLEANS

age=25



has_license=True
can_drive = age >=16 and has_license
print(can_drive)


print()

score=10
score=score+10
score+=10

score +=10
print(score)

name="hemant"

string=f"hi, my nmae is {name}"
print(string)


print(string.lower())
print(string.upper())
print(string.title())

print(string.startswith("T"))
print(string.endswith(" D "))

print(string.find("hemant"))

print(string.count("hemant"))

print(string.replace("hemant", "mahi"))




#Conditional statement
score =95

if score<10:
    print("so bad fail")

elif score <=33:
    print("just pass")

elif score <=50:
    print("do better next time")

elif score >=80:
    print("good you miss the firsr place")

else:
    print("fucking good job")




#TICKET

has_ticket=True
age=1

if has_ticket:
    if age >=18:
        print("yes you can go")
    else:
        print("nikal madarchod")

else:
    print("ticket buy")








#LOOP statemetns

for i in range(5):
    print("hemat")



for i in range(1,6):
    print(i)

for i in range(0,10,2):
    print(i)