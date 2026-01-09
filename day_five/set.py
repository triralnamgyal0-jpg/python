'''
a = set([1,2,3,4,5])
print(type(a))
'''

b = set(["apple","banana","cherry"])
count = 0

for item in b:
    count = count + 1
    print(f"item {count} is {item}")

b.add("orange") #adds single item
print(b)

b.update(["mango","grapes"]) #adds multiple iterms
print(b)

b.remove("banana") 
print(b)
'''
b.remove("kiwi")  #will raise an error if item not found
print(b)
'''

b.discard("kiwi") #will not raise an error if item not found
print(b)

b.pop() #removes first item
print(b)

b.clear() #removes all items
print(b)

