#Nabila Raisa, 09/30, period: 1 and 2, CFU#5

pennies = int(input("How many pennies do you have?"))
print("Great! You have " + str(pennies) + " pennies")

nickels = int(input("How many nickels do you have?"))
print("Great! You have " + str(nickels) + " nickles")

dimes = int(input("How many dimes do you have?"))
print("Great! You have " + str(dimes) + " dimes")

quarters = int(input("How many quarters do you have?"))
print("Great! You have " + str(quarters) + " quarters")

loonies = int(input("How many loonies do you have?"))
print("Great! You have " + str(loonies) + " loonies")

toonies = int(input("How many toonies do you have?"))
print("Great! You have " + str(toonies) + " toonies!")


total_cents= (pennies + nickels * 5 + dimes * 10 + quarters * 25 + loonies * 100 + toonies * 200) / 100
print ("Total value of coins: $" + "{:.2f}".format(total_cents))
total_dollars= total_cents // 1
print(total_dollars)
change = total_cents - total_dollars

remainder_in_quarters = (change) % 4

inQrts = int(change * 4)
inDimes = int(change * 10) - inQrts
inNickels= int(change*20)- (inDimes * 2)
inCents = int(change*100)- (inNickels*5)- (inDimes * 10)

print (f"Your total is: ${total_dollars}, {inQrts} quarters, {inDimes} dime, {inNickels} nickles and {inCents} cents.")





