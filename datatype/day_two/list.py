#accessing the list item through the index resear about the functions of list


countries = ["nepal","england","america"]
index = [0,1,2]

for element in countries:
    print (element)
print (countries[2])

countries[2] = "pakistan"
print (countries)

countries.append ("bangladesh")
print (countries)

items = countries.pop()
print (items)
print (countries)

items = countries.pop(1)
print (items)
print (countries)


students = []
n = 0

while n<5:
    name = input("enter your student names")
    students.append (name)
    n=n+1

print (students)

