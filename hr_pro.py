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
    #Manager class here
        
def main():
	# main code here

if __name__ == '__main__':
	main()
