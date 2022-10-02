class Employee:
    def __init__(self, name, age, salary, employment_years):
        self.name = name
        self.age = age
        self. salary = salary
        self.employment_years = employment_years

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years}"
    
    def get_annual_salry(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(name, age, salary, employment_years)
        self.bonus_percentage = bonus_percentage
    
    def __str__(self):
        return f"{super().__str__()}, Bonus: {self.get_bonus()}"
    
    def get_bonus(self):
        return self.bonus_percentage * self.salary

employee_1 = Employee("Ahmed", 23, 1000, 3)
employee_2 = Employee("Sarah", 25, 1300, 5)
employee_3 = Employee("Mike", 28, 700, 2)
manager_1 = Manager("Aziz", 45, 5000, 20, 0.2) 
manager_2 = Manager("Khalid", 36, 4000, 15, 0.15)
manager_3 = Manager("Zain", 40, 5500, 16, 0.25)

def main():
    employees = [employee_1.__str__(), employee_2.__str__(), employee_3.__str__()]
    managers = [manager_1.__str__(), manager_2.__str__(), manager_3.__str__()]

    print("Welcome to HR Pro\nQuestions:\n1. Show employees\n2. Show managers\n3. Add an employee\n4. Add a manager\n5. Exit")
    
    option = int(input("\nWhat would you like to do? "))
    
    while not option == 5:
        if option == 1:
            for employee in employees:
                print(employee) 
            option = int(input("\nWhat would you like to do? "))
        elif option == 2:
            for manager in managers:
                print(manager)
            option = int(input("\nWhat would you like to do? "))
        elif option == 3:
            name = input("Name: ")
            age = int(input("Age: "))
            salary = int(input("Salary: "))
            employment_years = int(input("Employment years:"))
            employee = Employee(name, age, salary, employment_years)
            employees.append(employee.__str__())
            print("Employee added successfully!")
            print(f"{employee} was added.")
            option = int(input("\nWhat would you like to do? "))
        elif option == 4:
            name = input("Name: ")
            age = int(input("Age: "))
            salary = int(input("Salary: "))
            employment_years = int(input("Employment years:"))
            bonus_percentage = int(input("Bonus Percentage: "))
            manager = Manager(name, age, salary, employment_years, bonus_percentage)        
            managers.append(manager.__str__())
            print("Manager added successfully!")
            print(f"{manager} was added.")
            option = int(input("\nWhat would you like to do? "))

    
if __name__ == '__main__':
	main()
