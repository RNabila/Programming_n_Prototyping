#Nabila Raisa, period 1 and 2, 10/29/2024
#CFU 12

'''
Version 1:-Write a program that asks the user for the password.
-The Password should initially be set to “simonsnyc”-It keeps asking 
them for the password until they get it correct.-For the incorrect 
password, it should say “Wrong Password!)-For correct password it should 
say “Correct! You may enter….”-And then it ends the program

Version 2:Modify Version 1 so that the User gets 
only 3 chances.HINTS:  Use a variable to keep 
track of the number of guesses.The User is stuck 
in the While loop as long as num_guesses < 3 and 
guess != PW

'''

password = "simonsnyc"
num_guesses = 0


while num_guesses < 3:
    user = input("Please enter your password")
    
    if user != password:
        print("That's incorrect loser, try it again")
        num_guesses += 1 
    else:
        print("Correct!! you may enter")
        break
        
if num_guesses == 3:
    print("Too many incorrect attempts. Access denied.")














