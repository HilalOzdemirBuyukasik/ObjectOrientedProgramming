
#Create a class called Employee to represent an employee in a company.
#The class should have the following attributes: name, position, and salary.
#Implement the following methods:

#get_info() → Returns a formatted string with the employee's details.

#__str__() → Returns the same output as get_info() when the object is printed.

#apply_raise() → Increases the employee's salary by a certain percentage.

#give_bonus() → Gives a bonus (a fixed amount) to the employee, and adds it to the salary.

class Employee:
    def __init__(self, name, position, salary):
        self.salary = float(salary)
        self.position = position
        self.name = name

    def get_info(self):
        return f'Employee Name: {self.name}, Position: {self.position}, Salary: {self.salary}'

    def __str__(self):
        return self.get_info()

    def apply_raise(self, percentage):

        raise_amount = self.salary * (percentage / 100)
        self.salary += raise_amount
        print(f'Salary raised by {percentage}%. New Salary: {self.salary} TL')

    def give_bonus(self, bonus_amount):
        self.salary += bonus_amount
        print(f'Bonus of {bonus_amount} TL added. New Salary: {self.salary} TL')

employee1 = Employee('Ayşe', 'Software Developer', '15000')
employee2 = Employee('Ahmet', 'Product Manager', '2000')

print(employee1)
print(employee2)

employee1.apply_raise(10)
employee1.give_bonus(5000)

print(employee1)
