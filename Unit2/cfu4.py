import math

name = input("What is your name? ")

print("Hello, " + name + "! Let's solve a quadratic equation.")

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the constant c: "))

discriminant = b**2 - 4*a*c

root1 = (-b + math.sqrt(discriminant)) / (2*a)
root2 = (-b - math.sqrt(discriminant)) / (2*a)

print("The roots of the quadratic equation are:")
print("x = " + str(root1))
print("x = " + str(root2))
