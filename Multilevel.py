class Person:
    def __init__(self, name, age):
        """
        Initialize the Person class with name and age attributes.
        :param name: str
        :param age: int
        """
        self.name = name
        self.age = age

    def display_person_details(self):
        """
        Display the details of a person.
        """
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        """
        Initialize the Employee class with additional attributes employee_id and salary.
        :param name: str
        :param age: int
        :param employee_id: str
        :param salary: float
        """
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_details(self):
        """
        Display the details of an employee, including inherited details from Person.
        """
        self.display_person_details()
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary:.2f}")

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        """
        Initialize the Manager class with an additional attribute department.
        :param name: str
        :param age: int
        :param employee_id: str
        :param salary: float
        :param department: str
        """
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_manager_details(self):
        """
        Display the details of a manager, including inherited details from Employee and Person.
        """
        self.display_employee_details()
        print(f"Department: {self.department}")

# Example usage:
if __name__ == "__main__":
    while True:
        print("\nChoose an option:\n1. Create a Person\n2. Create an Employee\n3. Create a Manager\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            person = Person(name, age)
            print("\nPerson Details:")
            person.display_person_details()

        elif choice == "2":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            employee_id = input("Enter employee ID: ")
            salary = float(input("Enter salary: "))
            employee = Employee(name, age, employee_id, salary)
            print("\nEmployee Details:")
            employee.display_employee_details()

        elif choice == "3":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            employee_id = input("Enter employee ID: ")
            salary = float(input("Enter salary: "))
            department = input("Enter department: ")
            manager = Manager(name, age, employee_id, salary, department)
            print("\nManager Details:")
            manager.display_manager_details()

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
