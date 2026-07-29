
# Name: Foram Dholariya
# Assignment: Module 8
# Purpose: Read and update a JSON student file.

import json


# Function to print all students
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , "
              f"Email = {student['Email']}")


def main():

    filename = "student.json"

    # Load the JSON file
    with open(filename, "r") as file:
        students = json.load(file)

    # Display original student list
    print("Original Student List")
    print("---------------------")
    print_students(students)

    # Add your information
    new_student = {
        "F_Name": "Foram",
        "L_Name": "Dholariya",
        "Student_ID": 99999,
        "Email": "fdholariya@gmail.com"
    }

    students.append(new_student)

    # Display updated student list
    print("\nUpdated Student List")
    print("--------------------")
    print_students(students)

    # Save updated list
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)

    print("\nThe student.json file has been updated.")


if __name__ == "__main__":
    main()