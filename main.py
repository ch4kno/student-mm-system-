import add_student
import update_student
import delete_student
import search_student
import display_student

def main_menu():
    while True:
        print("\nWelcome to Student Management System")
        print("1. Add New Student")
        print("2. Update Student Details")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student.add_student()
        elif choice == "2":
            update_student.update_student()
        elif choice == "3":
            delete_student.delete_student()
        elif choice == "4":
            search_student.search_student()
        elif choice == "5":
            display_student.display_students()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
