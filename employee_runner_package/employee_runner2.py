from employee_package.employee_module import Employee

from employee_package import employee_module

# e=employee_module.Employee()
# e.print_employee_details()
# print(e.get_bonus_detail())

Employee.company_name = 'Saama Tech'
Employee.company_location = "Pune"

emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

emp1.emp_id=1001
emp1.emp_name="Saul"
emp1.emp_salary=9000
emp1.emp_performance="B"

emp2.emp_id=1002
emp2.emp_name="Kim"
emp2.emp_salary=5000
emp2.emp_performance="A"

emp3.emp_id=1003
emp3.emp_name="Jack"
emp3.emp_salary=4900
emp3.emp_performance="C"

name=Employee.get_author_name()
print(name)

emp3.print_employee_details()
emp2.print_employee_details()
emp1.print_employee_details()

bonus=emp3.get_bonus_detail()
print(bonus)

print(emp1.get_bonus_detail())
print(emp2.get_bonus_detail())

emp4=Employee()

print(emp4.print_employee_details())
print(emp4.get_bonus_detail())
