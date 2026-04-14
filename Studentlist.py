Student_list=[]
student_dict={}
name=input("Enter the name of the student: ")#asking user to input the name of the student and storing it in a variable called name
age = input("Enter the age of the student: ")#asking user to input the age of the student and storing it in a variable called age
grade = input("Enter the grade of the student: ")#asking user to input the grade of the student and storing it in a variable called grade
Student_list.append(name)#adding the name of the student to the Student_list using the append() method
student_dict[name] = {"age#": age, "grade": grade}
print("Student List:", Student_list)
print("Student Dictionary:", student_dict)
search_name = input("Enter the name of the student you want to search for: ")
if search_name in student_dict:
    print(f"Student found! Name: {search_name}, Age: {student_dict[search_name]['age']}, Grade: {student_dict[search_name]['grade']}")
else:
    print("Student not found in the list.")
remove_name = input("Enter the name of the student you want to remove: ")
if remove_name in student_dict:
    Student_list.remove(remove_name)
    del student_dict[remove_name]
    print(f"'{remove_name}' has been removed from the student list.")
else:
    print("Student not found in the list.")