# This program allows to collect relevant data for the HR department. Its functions can be extended.
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


time_no = date.today()
time_now = time_no.strftime("%d/%m/%Y")
enter_your_code = input('Please enter the 5 digit unique key: ')
if enter_your_code == 'Xt1223':
    print('Welcome to the HR Portal!')
    employee1 = Employee(input('First Name: '), input('Last Name: '), input('Role: '), input('Age: '),
                         input('Enter phone number: '), input('Email: '),
                         input('Enter Gross monthly pay, RON: '))
    unique_id = employee1.first_name[1:3].lower() + employee1.role[1:3].lower() + employee1.age[1]
    employee_file = open('employee_class', 'a')
    employee_file.write('\n' + employee1.first_name + ',' + employee1.last_name + ',' + employee1.role +
                        ',' + employee1.age + ',' + employee1.phone_number + ',' + employee1.e_mail + ',' +
                        employee1.gross_salary + ',' + unique_id + ',' + time_now)
    employee_file.close()
    print('The employees unique ID is: ' + unique_id)

    print('Data Added! Database successfully closed!')
else:
    print('Invalid code!')
