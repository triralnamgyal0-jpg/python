import keyword 
print(keyword.kwlist)
'''\n	New line
\t	Tab space
\\	Backslash
\'	Single quote
\"	Double quote
\b	Backspace
'''

print("hello\t nepal")
print("hello\\nepal")
print("hello\'nepal")
print("hello\b nepal")

'''

1.  Arithmetic Operators
Used for mathematical operations.

Operator	Description
+	Addition
-	Subtraction
*	Multiplication
/	Division
%	Modulus
//	Floor Division
**	Exponent

'''
'''

#membership

country =("nepal")
print("n"in country)
print("t"in country)

#identity operator

a = 10 
b = 10 
print(a is b)
b='10'
print(a is b)

'''

name = input("Enter account holder's name: ")
account_number = int(input("Enter account number: "))
balance = float(input("Enter initial balance: "))

# Ask for transaction details
transaction_type = input("Enter transaction type (deposit or withdraw): ").lower()
amount = float(input("Enter transaction amount: "))

# Process transaction
if transaction_type == "deposit":
    balance += amount
    print("Deposit successful.")

elif transaction_type == "withdraw":
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")

else:
    print("Invalid transaction type.")

# Display account summary
print("\n--- Account Summary ---")
print("Account Holder:", name)
print("Account Number:", account_number)
print("Final Balance:", balance)