#Nabila Raisa, 01 and 02, 10/10

def calc_sum(num1, num2, num3):
    total_sum = num1 + num2 + num3
    print("The sum of your three numbers is:", total_sum)
    
def calc_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    print("The average of your numbers is: ", average)
    
def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    num3 = int(input("Enter a number: "))
    calc_sum(num1, num2, num3) #Calling the functions
    calc_average(num1, num2, num3)

main() #Running the main program
