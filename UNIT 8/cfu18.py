#Nabila Raisa, 01 and 02 01/07/2025
'''
Write a program that adds up all of the prices in the list
'''
#version 1

prices = [1.95, 4.50, 0.99, 5.99]
#initializing a var for the total sum
total = 0

for price in prices:
    #as the loop runs, it adds up all of the numbers until done
    total += price
    
print("the total sum of the price is: ", total)


#Version 2 

#blank list
prices = []

num_prices = int(input("How many prices do you want to add? "))

#-Populate this list by asking the user how many prices they want to add
for i in range(num_prices):
    price = float(input(f"Enter price {i + 1}: "))
    prices.append(price)

#initializing a var for the total sum
total = 0

#adding up the prices
for price in prices:
    total += price

print("The total sum of the prices is:", total)


#version 3

#blanks for prices and items
items = []
prices = []

#how many items they want
num_items = int(input("How many items do you want to add? "))

#populate the lists with item names and their prices
for i in range(num_items):
    item_name = input(f"Enter the name of item {i + 1}: ")
    item_price = float(input(f"Enter the price of {item_name}: "))
    items.append(item_name)
    prices.append(item_price)

#initializing a var for the total sum
total = 0

#for loop to calculate the sum
for price in prices:
    total += price

#receipt 
print("\n--- Receipt <3 ---")
for i in range(num_items):
    print(f"{items[i]}: ${prices[i]:.2f}")
print("+-----------------+")
print(f"Total: ${total:.2f}")
