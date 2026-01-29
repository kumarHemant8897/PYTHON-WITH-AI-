f=open("file.txt")


print(f.read())




f.close()

print("\n")

with open("file.txt") as f:
    print(f.read())