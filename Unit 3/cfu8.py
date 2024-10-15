#nabila raisa, period 1 and 2, CFU#8, 10/15/2024

delivery = input("Did you order delivery? Yes or No. ")

if delivery == "Yes" or delivery == "YES" or delivery == "yes":
    print("Great!")
    cost = float(input("How much did the food cost?"))
    print("The food costed $" + str(cost))
    people = int(input("How many people are splitting the bill?"))
    print(str(people) + " people are splitting the bill.")
    total = cost / people
    rounded_two = round(total, 2)  
    print("The cost per person is $" + str(total))


else:
    print("NO?! So Who is cooking?")
    
