# Task 1: Create a Dictionary of Student Marks

# Creating a dictionary with student names as keys and marks as values
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 74,
    "Eve": 88
}

# Asking the user for a student's name
student_name = input("Enter the student's name: ")

# Retrieving and displaying marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found in the records.")
