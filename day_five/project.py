

def greet():
    user_choice = input("enter 1 to create profile, enter 2 to update profile, 3 for view, enter 4 for delete and 5 to search student profile 0 to stop the program")
    return user_choice

def create_use(name, age, school):
    user_profile = {
        "name": name,
        "age": age,
        "school": school
    }
    user_details.append(user_profile)
    print("Profile created successfully!")

def users_list():
    for user in user_details:
        print(user)

def update_profile():
    update_name = input("Enter the name of the profile to update: ")
    found = False

    for user in user_details:
        if user["name"] == update_name:
            user["name"] = input("Enter new name: ")
            user["age"] = int(input("Enter new age: "))
            user["school"] = input("Enter new school: ")
            print("Profile updated successfully!")
            found = True
            break

    if not found:
        print("Profile not found")

def view_profile():
    if not user_details:
        print("No profiles to show")
    else:
        users_list()

def delete_profile():
    delete_name = input("Enter the name of the profile to delete:")
    found = False
    for user in user_details:
        if user["name"] == delete_name:
            user_details.remove(user)
            print("Profile deleted succesfully")
            found = True
def search_profile():
    view_name = input("Enter the name of the profile to view:")
    found = False
    for user in user_details:
        if user["name"] == view_name:
            print(user)
            found = True
    if not found:
        print("Profile not found")

user_details = []

while True:
    a = greet()
    if a == "1":
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        school = input("Enter your school name: ")
        create_use(name, age, school)
    elif a == "2":  # update profile by name
        update_profile()
    elif a == "3":
        view_profile()
    elif a == "4":
        delete_profile()
    elif a == "5":
        search_profile()
    elif a == "0":
        break

