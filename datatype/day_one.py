print("###faulty calculater###")
choice = int(input("-press 1 for addition, press 2 for multiplication, press 3 for subtraction, press 4 for division-"))
num_1 = int(input("input your first number"))
num_2 = int(input("input your second number"))
answer = 0

if choice == 1:
    answer = num_1 + num_2
    if num_1 == 1 and num_2 == 2:
        answer = 5
elif choice == 2:
    answer = num_1 * num_2
    if num_1 == 20 and num_2 == 20:
        answer = 2
elif choice == 3:
    answer = num_1 - num_2
    if num_1 == 1 and num_2 == 2:
        answer = 6
elif choice == 4:
    answer = num_1 / num_2
    if num_1 == 20 and num_2 == 20:
        answer = 300

print(answer)


