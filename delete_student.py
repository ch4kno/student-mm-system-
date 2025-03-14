from storage import load_students, save_students
from logger import log_action

def delete_student():
    students = load_students()
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            save_students(students)
            log_action(f"Deleted student: {student_id}")
            print("Student deleted successfully!")
            return

    print("Error: Student not found!")

if __name__ == "__main__":
    delete_student()
