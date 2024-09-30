#Nabila Raisa, 09/30, period: 1 and 2, CFU#5

pennies = int(input("How many pennies do you have?"))
print("Great! You have " + str(pennies))

nickles = int(input("How many nickles do you have?"))
print("Great! You have " + str(nickles))

dimes = int(input("How many dimes do you have?"))
print("Great! You have " + str(dimes))

quarters = int(input("How many quarters do you have?"))
print("Great! You have " + str(quarters))

loonies = int(input("How many loonies do you have?"))
print("Great! You have " + str(loonies))

toonies = int(input("How many toonies do you have?"))
print("Great! You have " + str(toonies))


total_cents= pennies * 1 + nickles * 5 + dimes * 10 + quarters * 25 + loonies * 100 + toonies * 200

dollars= total_cents // 100 #The double division is so the output is a whole number
cents= total_cents % 100 #this is to get the remaining cents

print(f"\nTotal amount: ${total_cents / 100:.2f}")

print(f"That's {dollars} dollars, and {cents} cents.")

