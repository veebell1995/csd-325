import json

# Load the JSON file into a Python list
def load_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return []

# Print the student list
def print_student_list(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Main function
def main():
    file_name = 'students.json'
    student_list = load_json_file(file_name)

    # Print the original student list
    print("Original Student List:")
    print_student_list(student_list)

    # Add new student to the list
    new_student = {
        "F_Name": "Vaneshiea",
        "L_Name": "Bell",
        "Student_ID": 18562,
        "Email": "vaneshieabell@yahoo.com"
    }
    student_list.append(new_student)

    # Print the updated student list
    print("\nUpdated Student List:")
    print_student_list(student_list)

    # Update the JSON file
    with open(file_name, 'w') as file:
        json.dump(student_list, file, indent=4)

    print("\nThe JSON file has been updated.")

if __name__ == "__main__":
    main()
