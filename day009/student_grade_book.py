"""
Task:
Implement a simple grade book using object-oriented programming.

Requirements:
- Create a `Student` class.
- Create a `GradeBook` class.
- A `Student` has a name and a list of grades.
- Grades must be integers from 0 to 100 inclusive.
- Invalid grades must raise `ValueError`.
- `add_grade()` adds a valid grade to the student.
- `average_grade()` returns the student's average grade.
- A student with no grades has an average of 0.
- `GradeBook` stores multiple Student objects.
- `find_top_student()` returns the student with the highest average grade.
- If there are no students, return `None`.
- If multiple students have the same average, return the first one added.

Algorithm:
- Iterate through the students.
- Calculate each student's average.
- Keep track of the student with the highest average.
- Return that student.

"""


class Student:
    def __init__(self, name: str) -> None:
        self.name = name
        self.grades: list[int] = []

    def add_grade(self, grade: int) -> None:
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be from 0 to 100 inclusive.")

        self.grades.append(grade)

    def average_grade(self) -> float:
        if not self.grades:
            return 0
        
        return sum(self.grades) / len(self.grades)


class GradeBook:
    def __init__(self) -> None:
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def find_top_student(self) -> Student | None:
        if not self.students:
            return None

        return max(self.students, key=lambda student: student.average_grade())
