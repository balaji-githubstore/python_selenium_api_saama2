from employee_package.employee_module import Employee

print("Using Employee Datatype")

Employee.company_name="Saama"
Employee.company_location="Pune"

Employee.company_name="Saama Tech"

emp1=Employee()
emp2=Employee()
emp3=Employee()

emp1.emp_id=1001
emp1.emp_name="Saul"
emp1.emp_salary=9000
emp1.emp_performance="B"

# print(emp1.emp_id)
# print(emp1.emp_name)
#
# print(emp2.emp_id)
# print(emp2.emp_name)
#
# print(emp3.emp_id)
# print(emp3.emp_name)

print(Employee.company_name)
print(Employee.company_location)

print(type(emp1))

name=Employee.get_author_name()
print(name)

emp2.print_employee_details()

emp1.print_employee_details()

emp3.print_employee_details()
