"""
Task:
Implement an employee directory using object-oriented programming.

Requirements:
- Create an `Employee` class.
- Create an `EmployeeDirectory` class.
- An Employee has a name, department, and salary.
- Name and department must not be empty.
- Salary must be greater than 0.
- Invalid values must raise `ValueError`.
- EmployeeDirectory stores multiple Employee objects.
- `add_employee()` adds an employee.
- `find_by_department()` returns all employees from a given department.
- `average_salary()` returns the average salary for a department.
- If a department has no employees, return 0.
- `highest_paid()` returns the employee with the highest salary
  in the given department.
- If a department has no employees, return `None`.
- If multiple employees have the same highest salary, return the first one.

Algorithm:
- Filter employees by department.
- For `average_salary()`, calculate the total salary and divide by
  the number of employees.
- For `highest_paid()`, compare salaries and keep the employee with
  the highest salary.
"""


class Employee:
    def __init__(self, name: str, department: str, salary: float) -> None:
        if not name:
            raise ValueError("Name can not be empty.")

        if not department:
            raise ValueError("Department can not be empty.")

        if salary <= 0:
            raise ValueError("Salary must be greater than 0.")

        self.name = name
        self.department = department
        self.salary = salary


class EmployeeDirectory:
    def __init__(self) -> None:
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def find_by_department(self, department: str) -> list[Employee]:
        if not self.employees:
            return []

        employees_by_department = []

        for employee in self.employees:
            if employee.department == department:
                employees_by_department.append(employee)

        return employees_by_department

    def average_salary(self, department: str) -> float:
        employees_by_department = self.find_by_department(department)

        if not employees_by_department:
            return 0

        total_salary = sum(employee.salary for employee in employees_by_department) 
        return total_salary / len(employees_by_department)

    def highest_paid(self, department: str) -> Employee | None:
        employees_by_department = self.find_by_department(department)

        if not employees_by_department:
            return None

        return max(employees_by_department, key=lambda employee: employee.salary)
