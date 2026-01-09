student_details = {"name": "triral", "age": 16, "grade": "11th", "pass":True, "subjects": ["math", "science", "english"]}
'''
print(student_details.get("age"))
print(student_details.get("subjects"))
print(student_details["pass"])
print(student_details.get("course"))  # None))
'''
'''
print(student_details["course"])  # KeyError)
'''
'''
for name, value in student_details.items():
    print(f"{name},is {value}")

'''
