class Employee:
    company_name = None
    company_location = "Chennai"
    __company_code = 4501  # private

    def __init__(self, id=None):
        # print(self)
        self.__emp_number = None
        self.emp_id = id
        self.emp_name = None
        self.emp_salary = None
        self.emp_performance = None

    #getter
    @property
    def get_emp_number(self):
        return self.__emp_number

    # setter
    @get_emp_number.setter
    def set_emp_number(self, number):
        if number > 0:
            self.__emp_number = number

    # getters
    # def get_emp_number(self):
    #     return self.__emp_number
    #
    # #setter
    # def set_emp_number(self, number):
    #     if number > 0:
    #         self.__emp_number = number

    @property
    def get_emp_name(self):
        return str(self.emp_name).upper()

    @staticmethod
    def get_author_name():
        return 'Balaji Dinakaran'

    def print_employee_details(self):
        print("-" * 100)
        print(f"Employee Id: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Performance: {self.emp_performance}")
        print(f"Company Name: {Employee.company_name}")
        print(f"Company Location: {Employee.company_location}")
        print("-" * 100)

    def get_bonus_detail(self):
        if self.emp_performance == "A":
            return 1000
        elif self.emp_performance == "B":
            return 500
        elif self.emp_performance == "C":
            return 100
        else:
            return 0
