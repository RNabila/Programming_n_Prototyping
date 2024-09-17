#Nabila Raisa, PD: 1 and 2, 09/17/2024, CFU#3

fname= input("What is your first name?")
lname= input("What is your last name?")
print("Hello " + fname + " " + lname +"!")

print("\nLet's play some fun math games!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else 'undefined (cannot divide by zero)'
modulo = num1 % num2 if num2 != 0 else 'undefined (cannot divide by zero)'

print(f"\n{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {modulo}")
