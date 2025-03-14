from storage import load_students

def search_student():
    students = load_students()
    search_query = input("Enter Student ID or Name: ")

    found_students = [
        student for student in students if student["ID"] == search_query or student["Name"].lower() == search_query.lower()
    ]

    if found_students:
        for student in found_students:
            print(f"Found: {student}")
    else:
        print("No student found!")

if __name__ == "__main__":
    search_student()
