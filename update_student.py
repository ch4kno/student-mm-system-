from storage import load_students, save_students
from logger import log_action

def update_student():
    students = load_students()
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["ID"] == student_id:
            print(f"Current Details: {student}")
            student["Name"] = input("Enter new Name: ") or student["Name"]
            student["Age"] = input("Enter new Age: ") or student["Age"]
            student["Course"] = input("Enter new Course: ") or student["Course"]
            
            save_students(students)
            log_action(f"Updated student: {student_id}")
            print("Student updated successfully!")
            return

    print("Error: Student not found!")

if __name__ == "__main__":
    update_student()
