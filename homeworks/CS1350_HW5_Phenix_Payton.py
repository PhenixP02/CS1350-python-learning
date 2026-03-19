## Phenix Payton
## CS1350
## Homework 5
## 3/20/26 


from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        # TODO: Store name and employee_id
        self.name = name
        self.employee_id = employee_id
        pass

    @abstractmethod
    def calculate_pay(self):
        # TODO: Make this abstract
        pass

    @abstractmethod
    def description(self):
        # TODO: Make this abstract
        pass

    def pay_stub(self):
        # TODO: Return "[name] (ID: [employee_id]): $[pay]"
        # Hint: call self.calculate_pay() — polymorphism!
        # Format pay to 2 decimal places
        pass

    @staticmethod
    def validate_positive(value, name):
        # TODO: Check if value > 0
        # Raise ValueError if not
        # Return True if valid
        pass

class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        # TODO: Call super().__init__
        # TODO: Validate and store annual_salary
        pass
    
    def calculate_pay(self):
        # TODO: Return annual_salary / 24
        pass

    def description(self):
        # TODO: Return "Salaried: [name]"
        pass

class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        # TODO: Call super().__init__
        # TODO: Validate and store hourly_rate and hours_worked
        pass

    def calculate_pay(self):
        # TODO: First 40 hours at regular rate
        # TODO: Hours beyond 40 at 1.5x rate
        pass

    def description(self):
        # TODO: Return "Hourly: [name]"
        pass

class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        # TODO: Call super().__init__
        # TODO: Validate all values (commission_rate must also be <= 1.0)
        # TODO: Store all attributes
        pass

    def calculate_pay(self):
        # TODO: Return base_salary + (sales * commission_rate)
        pass

    def description(self):
        # TODO: Return "Commission: [name]"
        pass

class Payroll:
    def __init__(self):
        # TODO: Initialize employees list
        pass

    def add_employee(self, employee):
        # TODO: Add employee to list
        pass

    def total_payroll(self):
        # TODO: Sum all employee pay using calculate_pay()
        pass

    def print_all_stubs(self):
        # TODO: Print each employee's pay_stub()
        pass

# Test your code
if __name__ == "__main__":
    # Create employees
    alice = SalariedEmployee("Alice Johnson", "E001", 84000)
    bob = HourlyEmployee("Bob Smith", "E002", 25.00, 45)
    carol = CommissionEmployee("Carol Davis", "E003", 2000, 50000, 0.05)

# Test individual employees
print("Employee Descriptions:")
for emp in [alice, bob, carol]:
    print(f" {emp.description()}")
    print("\nPay Stubs:")
for emp in [alice, bob, carol]:
    print(f" {emp.pay_stub()}")

# Test payroll (polymorphism!)
payroll = Payroll()
payroll.add_employee(alice)
payroll.add_employee(bob)
payroll.add_employee(carol)