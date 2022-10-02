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


      
def main():
    employee_1 = Employee("Ahmed", 23, 1000, 3)
    employee_2 = Employee("Sarah", 25, 1300, 5)
    employee_3 = Employee("Mike", 28, 700, 2)
    manager_1 = Manager("Aziz", 45, 5000, 20, 0.2) 
    manager_2 = Manager("Khalid", 36, 4000, 15, 0.15)
    manager_3 = Manager("Zain", 40, 5500, 16, 0.25)
    employees = [employee_1.__str__(), employee_2.__str__(), employee_3.__str__()]
    managers = [manager_1.__str__(), manager_2.__str__(), manager_3.__str__()]
   

if __name__ == '__main__':
	main()
