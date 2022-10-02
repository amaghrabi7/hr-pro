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

employee = Employee("ahmed", 23, 1000, 3)
print(employee)

class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(name, age, salary, employment_years)
        self.bonus_percentage = bonus_percentage
    
    def __str__(self):
        return f"{super().__str__()}, Bonus: {self.get_bonus()}"
    
    def get_bonus(self):
        return self.bonus_percentage * self.salary

manager = Manager("aziz", 45, 5000, 20, 0.2) 
print(manager)       
# def main():
	# main code here

# if __name__ == '__main__':
# 	main()
