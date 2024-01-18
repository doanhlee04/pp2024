#PW2
class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # Dictionary to store marks for different courses

    def add_mark(self, course_id, marks):
        self.marks[course_id] = marks
    
    def __str__(self):
        return f"Student ID "
class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name


#Input  Function
def get_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth (YYYY-MM-DD): ")
    return Student(student_id, student_name, student_dob)

def input_course_info():
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    for i in range(num_courses):
        course_id = input("Enter Course code: ")
        course_name = input("Enter course name: ")
        courses.append(Course(course_id, course_name))
    return courses

def select_course(courses):
    print("\nSelect a course to enroll by entering its index number:\n")
    for i, course in enumerate(courses, 1):
        print(f"{i}: {course.course_name}")
    
    selected_course_index = int(input("Enter the index of the course you want to select: "))
    
    if 1 <= selected_course_index <= len(courses):
        return courses[selected_course_index - 1].course_id
    else:
        print("Invalid index. Please enter a valid index.")
        return None

def input_marks(students, selected_course_id):
    for student in students:
        marks = float(input(f"Enter marks for {student.name} in {selected_course_id}: "))
        student.marks[selected_course_id] = marks

# Listing functions
def list_students(students):
    print("List of Students:")
    for student in students:
        print(f"Student ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")
    print()

def list_courses(courses):
    print("List of Courses:")
    for course in courses:
        print(f"Course ID: {course.course_id}, Name: {course.course_name}")
    print()

def show_student_marks(students, selected_course_id):
    print(f"Student Marks for Course {selected_course_id}:")
    for student in students:
        marks = student.marks.get(selected_course_id, "N/A")
        print(f"{student.name}: {marks}")
    print()


#Main
def main():
    students = []  # List to store student objects
    courses = input_course_info()

    while True:
        print("\nChoose an option:")
        print("1. Enroll students in a course and input marks")
        print("2. List students")
        print("3. List courses")
        print("4. Show student marks for a given course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            student = get_student_info()
            students.append(student)
            selected_course_id = select_course(courses)
            input_marks(students, selected_course_id)
        elif choice == '2':
            list_students(students)
        elif choice == '3':
            list_courses(courses)
        elif choice == '4':
            selected_course_id = select_course(courses)
            show_student_marks(students, selected_course_id)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()
    