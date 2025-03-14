import storage
from logger import log_action
def add_student():
    log_action("Loading students from storage")
    students = storage.load_students()
    
    
    if students is None:
        students =[]
        logging = ("no student")
        
    students_id = input("enter student ID:")
    name = input("enter student name:")
    age = input ("enter student age:")
    course = input("enter student cousre: ")
    
    if any (students.get("ID") == students_id for students in students):
        print( "error :A student with the same ID already exists")
        return
    
    new_student = {
        "ID": students_id,
        "Name": name,
        "Age": age,
        "Course": course}
    students.append(new_student)
    log_action(f"add new")
    
    storage.save_students(students)
    
    print("Student added successfully!")