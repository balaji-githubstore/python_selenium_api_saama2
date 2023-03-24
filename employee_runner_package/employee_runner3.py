from employee_package.employee_module import Employee

emp1=Employee()
emp1.emp_name="jane"
# emp1.emp_id=500
# print(emp1.emp_id)

emp2=Employee(601)
emp2.emp_name="victor"
# print(emp2.emp_id)


name=emp2.get_emp_name
print(name)

print(emp2.get_emp_name)

print(emp1.get_emp_name)

emp1.set_emp_name='bala'

print(emp1.get_emp_name)