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