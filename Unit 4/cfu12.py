#Nabila Raisa, period 1 and 2, 10/29/2024
#CFU 12

'''
Version 1:-Write a program that asks the user for the password.
-The Password should initially be set to “simonsnyc”-It keeps asking 
them for the password until they get it correct.-For the incorrect 
password, it should say “Wrong Password!)-For correct password it should 
say “Correct! You may enter….”-And then it ends the program

'''

password = "simonsync"
user = input("Please enter your password")


while user != password:
    print("Wrong...Try again")
    user = input("Enter your pssword again")
    if user == password:
        print("Good job! You may enter.")

