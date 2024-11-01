SYSTEM OVERVIEW
The Employee Management System is a Python-based application that manages employees, departments, and roles within an organization. It provides functionality for adding, removing, and transferring employees, as well as assigning tasks and performing code reviews.

CLASS OVERVIEW
DEPARTMENT-Represents a department in the organization. It contains methods to add and remove employees, and get department information.
ROLE(ABSTRACT CLASS)-An abstract base class that defines the interface for different roles in the organization.
MANAGERROLE AND DEVELOPER ROLE-Concrete implementations of the Role class, defining specific responsibilities for managers and developers.
EMPLOYEES-Base class for all employees, containing common attributes and methods.
MANAGER AND DEVELOPER-Subclasses of Employee, with role-specific methods like assigning tasks and code reviewing.
EMS-The main class that orchestrates the entire system, managing employees and departments.

KEY FUNCTIONALITIES-Adding and removing employees,Transferring employees between departments,Assigning tasks (for managers),Performing code reviews (for developers),Displaying employee information

MAIN PROGRAM FLOW-The main() function provides an interactive menu-driven interface for users to interact with the system. It allows users to perform various operations like displaying all employees, adding new employees, removing employees, transferring employees, assigning tasks, and performing code reviews.
