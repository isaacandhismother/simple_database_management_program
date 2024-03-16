from employee import Employee
from db import conn

# Manage yor database here

first_user = Employee.get(1)
second_user = Employee.get(2)
if first_user is None:
    first_user = Employee("name", "surname", "age")
    first_user.save()

if second_user is None:
    second_user = Employee("Sherlock", "Holmes", "35")
    second_user.save()

first_user.name = "Tornike"
first_user.surname = "Namchishvili"
first_user.age = "20"
first_user.save()

print(Employee.get_list(name="Tornike"))
print(Employee.get_list(name="Sherlock"))

second_user.delete()

print(Employee.get_list(name="Sherlock"))

conn.commit()
conn.close()
