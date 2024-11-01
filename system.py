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