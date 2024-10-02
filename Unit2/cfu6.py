import random
import math

print("Welcome to the Random Number Calculator!\nI will generate a random number between 1 and 100.")
ranint = random.randint(1,100)
print("\nRandom number generated: " + str(ranint))

num= int(input("Please enter a number: "))
print("The number you entered: " + str(num))

print("Calculating....")

print("\nResults:\nRandom Number: " + str(ranint))
print("Your number: " + str(num))
add = ranint + num
sub = ranint - num
product = ranint * num
quotient = ranint / num
remainder = ranint % num
ranrt = math.sqrt(ranint)
numsq = math.pow(num, ranint)

print("\nSum: " + str(ranint) + " + " + str(num) + " = " + str(add))
print("Difference: " + str(ranint) + " - " + str(num) + " = " + str(sub))
print("Product: " + str(ranint) + " * " + str(num) + " = " + str(product))
print("Quotient: " + str(ranint) + " / " + str(num) + " = " + str(quotient))
print("Remainder: " + str(ranint) + " % " + str(num) + " = " + str(remainder))
print("Square Root of Random Number: sqrt( " + str(ranint) + ") = " + str(ranrt))
print("Square Root of Random Number: " + str(num) + "^" + str(ranint) + " = " + str(numsq))


