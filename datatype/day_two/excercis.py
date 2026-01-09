student_name = input("give me your name")
roll_number = int(input("give me your roll number"))
English = int(input("give me your marks for english"))
Math = int(input("give me your marks for maths"))
Science = int(input("give me your marks for sceince"))

print("marks for engish are",English)
print("makrs for maths are",Math)
print("marks for science are",Science)

choice = int(input("press 1 for total marks press 2 for average marks"))

if choice == 1:
    total_marks = English + Math + Science
    print(total_marks)
elif choice == 2:
    total_marks = English + Math + Science
    average = total_marks / 3
    print(average)
else:
    print("wrong input")

grade = int(input("what is your average marks"))

if grade >= 90:
    print("congratulations you have gotten a A+")
elif grade >= 80:
    print("congratulations you have gotten a A")
elif grade >= 70:
    print("congratulations you have gotten a B")
elif grade >= 60:
    print("congratulations you have gotten a C")
elif grade < 60:
    print("congratulations you have gotten a grade F")

    

