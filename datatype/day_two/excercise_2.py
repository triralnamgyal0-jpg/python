name = input("enter your full name")
age = int(input("enter your age"))
height = float(input("what is your height?"))
weight = float(input("what is your weight in kgs?"))
gender = bool(input("are you male or female?"))
BMI = weight/(height**2)
if BMI<18.5:
    print("underweight")
elif 18.5 <= BMI < 24.9:
    print("normal weight")
elif 25 <= BMI < 29.9:
    print("overweight")
elif BMI >= 30:
    print("obese")
    