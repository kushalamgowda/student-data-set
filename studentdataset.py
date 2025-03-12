class StudentGradeManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, grades):
        if student_id in self.students:
            print("Student ID already exists!")
        else:
            self.students[student_id] = {'name': name, 'grades': grades}
            print("Student added successfully!")

    def update_grades(self, student_id, new_grades):
        if student_id in self.students:
            self.students[student_id]['grades'] = new_grades
            print("Grades updated successfully!")
        else:
            print("Student ID not found!")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student record deleted successfully!")
        else:
            print("Student ID not found!")

    def display_students(self):
        if not self.students:
            print("No student records available!")
        else:
            print("\nStudent Records:")
            for student_id, details in self.students.items():
                print(f"ID: {student_id}, Name: {details['name']}, Grades: {details['grades']}")

# Sample usage
def main():
    manager = StudentGradeManager()
    while True:
        print("\n1. Add Student")
        print("2. Update Grades")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            grades = list(map(float, input("Enter Grades (comma separated): ").split(',')))
            manager.add_student(student_id, name, grades)
        
        elif choice == '2':
            student_id = input("Enter Student ID: ")
            new_grades = list(map(float, input("Enter New Grades (comma separated): ").split(',')))
            manager.update_grades(student_id, new_grades)
        
        elif choice == '3':
            student_id = input("Enter Student ID: ")
            manager.delete_student(student_id)
        
        elif choice == '4':
            manager.display_students()
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
