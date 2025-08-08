# enhanced LMS tracker with string operations
# 

print("="*30)
print("Enhanced LMS Grade Tracker")
print("=" * 30)

# validate id
student_id_valid =False
while not student_id_valid:
    student_id = input("Enter your ID: ")
    # check if valid id based on -sign
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("PLEASE input positive values only")
    elif student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else:
            print("Please input non-zero value")
    else:
        print("Enter only numbers")

print(student_id)
# format id
formatted_id = "STU" + str(student_id).zfill(5)
print(formatted_id)

#valaidate name
student_name_valid = False
while not student_name_valid:
    student_name = input("Enter your name:")
    student_name = student_name.strip().capitalize()
    student_name = student_name.strip().title()
    # strip will remove front and back spaces, not in between
   
    # name check should have only alphabets
    name_check = student_name.replace(" ","")
    
    # look for only alphabets
    if name_check.isalpha():
        student_name_valid = True
        print("Name:"+ student_name)
    else:
        if not name_check.isalpha():
            print("Name should container only letters")
        elif len(student_name) < 3:
            print("Name should have at least 3 characters")