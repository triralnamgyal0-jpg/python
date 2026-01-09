'''
#list number
number = [1,2,3,4,5,6,7,8,9,10]
x = 0

for x in range(len(number)):
        if number[x] % 2 == 0:
            print("even number", number[x])
            x = x + 1
            if x == 10:
                break
        else:
            print("odd number", number[x])
            x = x + 1
            if x == 10:
                break
'''
#only even number print
even = []
number = [1,2,3,4,5,6,7,8,9,10]
for x in range(len(number)):
    if number[x] % 2 == 0:
        even.append(number[x])
        print("even number", number[x])
        x = x + 1
        if x == 10:
            break
    else:
        print("odd number", number[x])
        x = x + 1
        if x == 10:
            break
print("even numbers are", even)
