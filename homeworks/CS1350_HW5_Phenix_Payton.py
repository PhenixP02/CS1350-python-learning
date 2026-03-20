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
        pay = self.calculate_pay()
        return f"{self.name} (ID: {self.employee_id}): ${pay:.2f}"

    @staticmethod
    def validate_positive(value, name):
        # TODO: Check if value > 0
        # Raise ValueError if not
        # Return True if valid
        if value <= 0:
            raise ValueError(f"{name} must be Positive")
        return True

class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        # TODO: Call super().__init__
        # TODO: Validate and store annual_salary
        super().__init__(name, employee_id)
        if Employee.validate_positive(annual_salary, "annual_salary") == True:
            self.annual_salary = annual_salary
        pass
    
    def calculate_pay(self):
        # TODO: Return annual_salary / 24
        return self.annual_salary / 24

    def description(self):
        # TODO: Return "Salaried: [name]"
        return f"Salaried: {self.name}"

class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        # TODO: Call super().__init__
        # TODO: Validate and store hourly_rate and hours_worked
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked
        if Employee.validate_positive(hourly_rate, "hourly_rate") == True:
            self.hourly_rate = hourly_rate
        pass

    def calculate_pay(self):
        # TODO: First 40 hours at regular rate
        # TODO: Hours beyond 40 at 1.5x rate
        if self.hours_worked <= 40:
            pay = self.hours_worked * self.hourly_rate
        else:
            regular_pay = 40 * self.hourly_rate
            ot_hours = self.hours_worked - 40
            ot_pay = (ot_hours * self.hourly_rate) * 1.5
            pay = regular_pay + ot_pay
        return pay

    def description(self):
        # TODO: Return "Hourly: [name]"
        return f"Hourly: {self.name}"

class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        # TODO: Call super().__init__
        # TODO: Validate all values (commission_rate must also be <= 1.0)
        # TODO: Store all attributes
        super().__init__(name, employee_id)
        self.sales = sales
        if Employee.validate_positive(base_salary, "base_salary") == True:
            self.base_salary = base_salary 
        if commission_rate > 1.0:
            raise ValueError("commission_rate must be <= 1.0")
        else:
            self.commission_rate = commission_rate
        pass

    def calculate_pay(self):
        # TODO: Return base_salary + (sales * commission_rate)
        pay = self.base_salary + (self.sales * self.commission_rate)
        return pay

    def description(self):
        # TODO: Return "Commission: [name]"
        return f"Commission: {self.name}"

class Payroll:
    def __init__(self):
        # TODO: Initialize employees list
        self.employees = []
        pass

    def add_employee(self, employee):
        # TODO: Add employee to list
        self.employees.append(employee)
        pass

    def total_payroll(self):
        # TODO: Sum all employee pay using calculate_pay()
        total_pay = 0
        for emp in self.employees:
            total_pay += emp.calculate_pay()
        return total_pay

    def print_all_stubs(self):
        # TODO: Print each employee's pay_stub()
        for emp in self.employees:
            print(emp.pay_stub())
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
print(f"\nTotal Payroll: ${payroll.total_payroll():.2f}")

# Test validation
print("\nTesting validation:")
try:
    bad = SalariedEmployee("Bad", "E999", -50000)
except ValueError as e:
    print(f" Caught: {e}")
try:
    bad = CommissionEmployee("Bad", "E999", 1000, 5000, 1.5)
except ValueError as e:
    print(f" Caught: {e}")