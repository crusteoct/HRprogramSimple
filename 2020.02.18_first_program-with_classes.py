# This program allows to collect relevant data for the HR department. It uses classes.
# The password is Xt1223.
from datetime import date


class Employee:
    def __init__(self, first_name, last_name, role, age, phone_number, e_mail, gross_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.age = age
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.gross_salary = gross_salary
        self.unique_id = last_name[1:3].lower() + role[1:3].lower() + age

    # Generating an unique Employee ID.

    def full_data_to_print(self):
        return '{} {} {} {} {} {} {} {}'.format(self.first_name, self.last_name, self.role, self.age, self.phone_number,
                                                self.e_mail, self.gross_salary, self.unique_id + time_now)


# Using this method, I can print all the data at once.


time_no = date.today()
time_now = time_no.strftime("%d/%m/%Y")
enter_your_code = input('Please enter the 5 digit unique key: ')
if enter_your_code == 'Xt1223':
    print('Welcome to the HR Portal!')
    # employee 1 is from the employee class. We use the user input to receive the attributes of it.
    employee1 = Employee(input('First Name: '), input('Last Name: '), input('Role: '), input('Age: '),
                         input('Enter phone number: '), input('Email: '), input('Enter Gross monthly pay, RON: '))

    # we are writing all the relevant data in the txt file, using the append function
    employee_file = open('employee_class', 'a')
    employee_file.write('\n' + employee1.full_data_to_print() + time_now)
    employee_file.close()
    print('The employees unique ID is: ' + employee1.unique_id)

    print('Data Added! Database successfully closed!')
else:
    print('Invalid code!')
