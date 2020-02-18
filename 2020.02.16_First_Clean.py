from datetime import date

enter_your_code = input('Please enter the 5 digit unique key: ')


def number_input(user_text):
    while True:
        try:
            user_input = int(input(user_text))
        except ValueError:
            print('Not a number, try again.')
            continue
        else:
            return user_input


if enter_your_code == 'Xt1223':
    print('Welcome to the HR Portal!')
    employee_file = open('employees', 'a')
    employee_first = input('First Name: ')
    employee_last = input('Last Name: ')
    employee_function = input('Role: ')
    age = number_input('Age: ')
    mobile_number = number_input('Enter a Phone number: ')
    employee_email = input('Email: ')
    pay = number_input('Enter Gross monthly pay, RON: ')
    unique_id = employee_last[1:3].lower() + employee_function[1:3].lower() + str(age + 4)
    time_no = date.today()
    time_now = time_no.strftime("%d/%m/%Y")
    employee_file.write('\n' + employee_first + ',' + employee_last + ',' + employee_function + ',' + str(age) + ',0' +
                        str(mobile_number) + ',' + employee_email + ',' + str(pay) + ',' + unique_id + ',' + time_now)
    employee_file.close()
    print('The unique ID of this employee is: ' + unique_id)
    print('Data Added! Database successfully closed!')

else:
    print('Invalid code: ')
