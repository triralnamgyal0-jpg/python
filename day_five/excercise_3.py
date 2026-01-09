#3.Ask the user to input numbers until they enter 0, then print the total sum.
total_sum = 0
while True:
        num = int(input("enter a number (0 to stop): "))
        if num == 0:
            break
        total_sum = total_sum + num
            
print("Total sum:", total_sum)