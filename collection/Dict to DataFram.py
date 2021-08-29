import pandas as pd

emp_details = {'emp': {'sai': {'Id': '001', 'Designation': 'SDE', 'Salary': '20000'},
                       'kumar': {'Id': '002', 'Designation': 'Intern', 'Salary': '12000'},
                       'Satapathy': {'Id': '003', 'Designation': 'Team Lead', 'Salary': '30000'}}}

df1 = pd.DataFrame(emp_details)
print('\n')

df2 = pd.DataFrame(emp_details['emp'])
print(df1)
print(df2)

emp = [{'name': 'sai', 'Id': '001', 'Designation': 'SDE', 'Salary': '20000'},
       {'name': 'kumar', 'Id': '002', 'Designation': 'Intern', 'Salary': '12000'},
       {'name': 'Satapathy', 'Id': '003', 'Designation': 'Team Lead', 'Salary': '30000'}]
print(emp)

df3 = pd.DataFrame(emp)
print(df3)

emp2 = {'emp1': {'name': 'sai', 'Id': '001', 'Designation': 'SDE', 'Salary': '20000'},
        'emp2': {'name': 'kumar', 'Id': '002', 'Designation': 'Intern', 'Salary': '12000'},
        'emp3': {'name': 'Satapathy', 'Id': '003', 'Designation': 'Team Lead', 'Salary': '30000'}}

print(emp2)

df4=pd.DataFrame(emp2)
print(df4)
