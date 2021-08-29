# Nested Dict Are the Dict which lie within another Dictionary.
# nested_dict = { 'dictA': {'key_1': 'value_1'},
#               'dictB': {'key_2': 'value_2'}}

emp_details = {'emp': {'sai': {'Id': '001', 'Designation': 'SDE', 'Salary': '20000'},
                       'kumar': {'Id': '002', 'Designation': 'Intern', 'Salary': '12000'},
                       'Satapathy': {'Id': '003', 'Designation': 'Team Lead', 'Salary': '30000'}}}
print(emp_details['emp'])  # for employee dict

# Accessing Dict inside the nested Dict
print(emp_details['emp']['sai'])
print(emp_details['emp']['kumar'])
print(emp_details['emp']['Satapathy'])


emp2 = {'emp1': {'name': 'sai', 'Id': '001', 'Designation': 'SDE', 'Salary': '20000'},
        'emp2': {'name': 'kumar', 'Id': '002', 'Designation': 'Intern', 'Salary': '12000'},
        'emp3': {'name': 'Satapathy', 'Id': '003', 'Designation': 'Team Lead', 'Salary': '30000'}}

print(emp2)
print(emp2['emp1'])

