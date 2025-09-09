from School import School
from Person import Person
from Student import Student
from Employee import Employee
from Teacher import Teacher
from Class import Class


def main():
    # Create instances of each class

    person = Person("John Doe", "1990-01-01")
    print(f"Person:\n\tID = {person.person_id},\n\tDetails = {person.details}\n")

    student = Student("John Doe", "1990-01-01", "20050515", "L3")
    print(
        f"Student:\n\tID = {student.person_id},\n\tDetails = {student.details}\n\t"
        f"Student ID = {student.student_id},\n\tGrade = {student.grade}\n"
    )

    employee = Employee("Alice Johnson", "1985-03-22", "20250515", 50000)
    print(
        f"Employee:\n\tID = {employee.person_id},\n\tDetails = {employee.details}\n\t"
        f"Employee ID = {employee.employee_id},\n\tSalary = {employee.salary}\n"
    )

    teacher = Teacher(
        "Alice Johnson", "1985-03-22", "20250515", 50000, "0515", ["201", "203", "204"]
    )
    print(
        f"Teacher:\n\tID = {teacher.person_id},\n\tDetails = {teacher.details}\n\t"
        f"Employee ID = {teacher.employee_id},\n\tSalary = {teacher.salary}\n\t"
        f"Teacher ID = {teacher.teacher_id},\n\tSubjects = {teacher.teaches_id}\n"
    )

    class_instance = Class("201", ["20052001", "20052002", "20052003"])
    print(
        f"Class:\n\tID = {class_instance.class_id},\n\tStudents = {class_instance.students_id}\n"
    )

    school = School(
        "UQAC",
        "555 Bd de l'Université, Chicoutimi, QC G7H 2B1",
        ["20052001", "20052002", "20052003"],
        "012",
    )
    print(
        f"School:\n\tID = {school.school_id},\n\tAddress = {school.address}\n\t"
        f"Students = {school.students_id},\n\tPost Codes Accepted = {school.postCodesAccepted}\n"
    )


if __name__ == "__main__":
    main()
