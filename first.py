
my_list=["hemat",25,"Student",2027]

my_list[0]="Mahi"
age=my_list[1]

my_list.append("hemat")
my_list.remove("Mahi")

my_list.insert(2,"rahiuk")

last=my_list.pop()
first=my_list.pop()

print(my_list[0])

print(my_list[: 2])
print(my_list[1: ])




print("\n")














#DICTIONARY


person ={
    "name" : "hemant",
    "age" : 55,
    "city" : "Bnagalore",
    "proffession" : "student"
}

del person["age"]

#print(person["age"])
print(person["name"])
print(person["city"])
print(person["proffession"])


print(person.keys())
print(person.values())
print(person.items())


if "name" in person:
    print("Name found")



person.update({"age": 78, "proffession": "driver"})
print(person["age"])


print("\n")








#TUPLES
#TUPLES ARE THE LIST THAT CANNOT BE CHANGED AFTER CREATED
# MADE WITH () THESE BRACKET ONLY 

empty=()

point=(5,4)
colors=("red","green","blue")

print(colors)

print(colors[0])


print("\n")











#SETS
#sets are the collection that only stored unique elements
#they automatically remove duplicates

emplty_set=set()  #empty sets

numbers={1,2,3,4,5,6}
print(numbers)
fruits=set(["apple","orange","graphes","orange"])
print(fruits)

score={45,45,66,66,88,88}
unique_score=set(score)
print(unique_score)

