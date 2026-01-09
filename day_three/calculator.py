choice = input("enter + for addition, enter - for subtraction, enter * for multiplication, enter / for division")
num_1= int(input("enter first number"))
num_2= int(input("enter second number"))

def add(num_1,num_2):
    return num_1+num_2
def subtract(num_1,num_2):
    return num_1-num_2
def multiply(num_1,num_2):
    return num_1*num_2
def divide(num_1,num_2):
    return num_1/num_2

if choice == "+":
    result = add(num_1,num_2)
    print(result)
elif choice == "-":
    result = subtract(num_1,num_2)
    print(result)
elif choice == "*":
    result = multiply(num_1,num_2)
    print(result)
elif choice == "/":
    result = divide(num_1,num_2)
    print(result)
else:
    print("invalid operation")
    