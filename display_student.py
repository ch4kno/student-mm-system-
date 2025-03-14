from storage import load_students

def display_students():
    students = load_students()
    if students : 
        for student  in students:
            print(students)
if __name__ == "__main__":
    display_students()