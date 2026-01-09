'''
#positional arguements
def add(a, b):
    print(a + b)

add(10, 20)
#Keyword Arguments
#add(b=20, a=10)
#default arguements
def greet(name="User"):
    print("Hello", name)

greet()
greet("triral")
#variable length arguements
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))
#kwargs (Keyword)
def info(**details):
    print(details)

info(name="triral", age=17, country="Nepal")
#Docstring 
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b

print(add.__doc__)

'''
'''

def add(name,age):
    print(name,age)
add(age=17, name="triral")
'''
'''
def greet(name="user"):
    print("hello",name)

greet()
greet("raj")

'''
'''
def total(*numbers):
    return (numbers[0]*numbers[1])*(numbers[2]*numbers[3]*numbers[4])

print(total(1, 2, 3, 4, 5))

'''
'''
def info(**student_details):
    print("student name is",student_details["name"],"age is",student_details["age"],"grade is",student_details["grade"],"country is",student_details["country"])

info(name="triral", age=17, grade="11th", country="nepal")
'''
'''
#excercise 1
def even_odd(n):
    if n%2==0:
        return "even"
    elif n%2!=0:
        return "odd"
print(even_odd(10))
#excercise 2

p = float((input("enter principal amount")))
r = float((input("enter rate of interest")))
t = float((input("enter time period in years")))

def simple_interest(p,r,t):
    SI = (p*r*t)/100
    return SI
print(simple_interest(p,r,t))
'''
'''
#excercise 3
password = input("enter your password")
def password_check(password):
    if len(password)>=8:
        return "true"
    else:
        return "false"
print(password_check(password))
'''
#excercise 4
num_1 = int(input("enter a number"))
num_2 = int(input("enter another number"))
num_3 = int(input("enter one more number"))

def maximum(num_1,num_2,num_3):
    if num_1 > num_2 and num_1 > num_3:
        print("maximum is", num_1)
        return num_1
    elif num_2 > num_1 and num_2 > num_3:
        print("maximum is", num_2)
        return num_2
    elif num_3 > num_1 and num_3 > num_2:
        print("maximum is", num_3)
        return num_3
    else:
        print("all are equal")
        return None
print(maximum(num_1,num_2,num_3)) 