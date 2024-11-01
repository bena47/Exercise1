from abc import ABC, abstractmethod

class Department:
      def __init__(self, name):
        self.__name = name
        self.__employees = []
        def get_name(self):
            return self.__name

        def add_employee(self, employee):
            self.__employees.append(employee)

        def remove_employee(self, employee):
            if employee in self.__employees:
                self.__employees.remove(employee)

        def get_employees(self):
            return self.__employees  
        
class Role(ABC):
    @abstractmethod
    def get_responsibilities(self):
        pass

class ManagerRole(Role):
    def get_responsibilities(self):
        return "Oversee team, assign tasks, report to upper management"    
    
class Employee:
    def __init__(self, name, employee_id, department, role):
        self.__name = name
        self.__employee_id = employee_id
        self.__department = department
        self.__role = role    

    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__employee_id

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role

    def display_info(self):
        return f"Name: {self.__name}, ID: {self.__employee_id}, Department: {self.__department.get_name()}, Role: {type(self.__role).__name__}" 
      
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id, department, ManagerRole())

    def assign_task(self, employee, task):
        print(f"{self.get_name()} assigned '{task}' to {employee.get_name()}")     

class Developer(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id, department, DeveloperRole())

    def code_review(self, code):
        print(f"{self.get_name()} is reviewing code: {code}")        

class EmployeeManagementSystem:
    def __init__(self):
        self.__employees = []
        self.__departments = []        
    def add_employee(self, employee):
        self.__employees.append(employee)
        employee.get_department().add_employee(employee)

    def remove_employee(self, employee):
        if employee in self.__employees:
            self.__employees.remove(employee)
            employee.get_department().remove_employee(employee)

    def add_department(self, department):
        self.__departments.append(department)

    def get_employee_by_id(self, employee_id):
        for employee in self.__employees:
            if employee.get_employee_id() == employee_id:
                return employeefrom abc import ABC, abstractmethod

class Department:
    def __init__(self, name):
        self.__name = name
        self.__employees = []

    def get_name(self):
        return self.__name

    def add_employee(self, employee):
        self.__employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.__employees:
            self.__employees.remove(employee)

    def get_employees(self):
        return self.__employees

class Role(ABC):
    @abstractmethod
    def get_responsibilities(self):
        pass

class ManagerRole(Role):
    def get_responsibilities(self):
        return "Oversee team, assign tasks, report to upper management"

class DeveloperRole(Role):
    def get_responsibilities(self):
        return "Write code, participate in code reviews, report to manager"

class Employee:
    def __init__(self, name, employee_id, department, role):
        self.__name = name
        self.__employee_id = employee_id
        self.__department = department
        self.__role = role

    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__employee_id

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role

    def display_info(self):
        return f"Name: {self.__name}, ID: {self.__employee_id}, Department: {self.__department.get_name()}, Role: {type(self.__role).__name__}"

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id, department, ManagerRole())

    def assign_task(self, employee, task):
        print(f"{self.get_name()} assigned '{task}' to {employee.get_name()}")

class Developer(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id, department, DeveloperRole())

    def code_review(self, code):
        print(f"{self.get_name()} is reviewing code: {code}")

class EmployeeManagementSystem:
    def __init__(self):
        self.__employees = []
        self.__departments = []

    def add_employee(self, employee):
        self.__employees.append(employee)
        employee.get_department().add_employee(employee)

    def remove_employee(self, employee):
        if employee in self.__employees:
            self.__employees.remove(employee)
            employee.get_department().remove_employee(employee)

    def add_department(self, department):
        self.__departments.append(department)

    def get_employee_by_id(self, employee_id):
        for employee in self.__employees:
            if employee.get_employee_id() == employee_id:
                return employee
        return None

    def display_all_employees(self):
        for employee in self.__employees:
            print(employee.display_info())

    def transfer_employee(self, employee, new_department):
        old_department = employee.get_department()
        old_department.remove_employee(employee)
        new_department.add_employee(employee)
        employee.set_department(new_department)

    def display_department_employees(self, department_name):
        for department in self.__departments:
            if department.get_name() == department_name:
                for employee in department.get_employees():
                    print(employee.display_info())
                return
        print("Department not found")

    def display_employee_responsibilities(self, employee_id):
        employee = self.get_employee_by_id(employee_id)
        if employee:
            print(employee.get_role().get_responsibilities())
        else:
            print("Employee not found")
        return None

    def display_all_employees(self):
        for employee in self.__employees:
            print(employee.display_info())

    def transfer_employee(self, employee, new_department):
        old_department = employee.get_department()
        old_department.remove_employee(employee)
        new_department.add_employee(employee)
        employee.set_department(new_department)
    
 # main program
def main():
    ems = EmployeeManagementSystem()    