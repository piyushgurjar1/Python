class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        print("Subclass must implement this method")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        tax = 0.10 * self.base_salary  # 
        pf = 0.12 * self.base_salary  
        net_salary = self.base_salary - tax - pf
        return net_salary

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        tax = 0.10 * self.base_salary  
        pf = 0.12 * self.base_salary   
        net_salary = self.base_salary - tax - pf
        return net_salary

class ContractorEmployee(Employee):
    def calculate_salary(self):
        tax = 0.10 * self.base_salary  
        net_salary = self.base_salary - tax
        return net_salary

full_time = FullTimeEmployee("Piyush", 1, 50000)
part_time = PartTimeEmployee("Pavesh", 2, 20000)
contractor = ContractorEmployee("Mayur", 3, 30000)


print(f"{full_time.name}'s final salary: {full_time.calculate_salary()}")
print(f"{part_time.name}'s final salary: {part_time.calculate_salary()}")
print(f"{contractor.name}'s final salary: {contractor.calculate_salary()}")
