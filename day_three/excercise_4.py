'''
name = "triral"
name[2] = "a"
print (name)
#strings are immutable, meaning once created, their contents cannot be changed.
'''
'''
text = ("triral")
print(len(text))  #output 6

'''
'''
text = "triral" 
print(text.upper()) # TRIRAL 
print(text.lower()) # triral

text = "python programming" 
print(text.capitalize()) # Python programming 
print(text.title()) # Python Programming

text = " triral " 
print(text.strip()) # "triral" 
print(text.lstrip()) # "triral " 
print(text.rstrip()) # " triral"
 
'''
'''

text = "I love Java" 
print(text.replace("Java", "triral")) # I love triral

 text = "Python Programming" 
print(text.find("P")) # 0 
print(text.find("triral")) # -1 

text = "python.py" 
print(text.startswith("python")) # True 
print(text.endswith(".py")) # True 

text = "Python Django Flask" 
words = text.split() 
print(words)

languages = ["Python", "Django", "Flask"] 
result = ", ".join(languages) 
print(result)

print("Python".isalpha()) # True 
print("123".isdigit()) # True 
print("Python123".isalnum()) # True

name = "Amrit" 
age = 25 
print("My name is {} and I am {} years old".format(name, age))

print(f"My name is {name} and I am {age} years old")

text = """Python is easy Django is powerful FastAPI is fast""" 
print(text)

text = "Python Programming" 
print("Python" in text) # True 
print("Java" not in text) # True
'''

