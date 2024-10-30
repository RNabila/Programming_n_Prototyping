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

# VERSION 1
def version_one():
    password = "simonsnyc"
    user = input("Please enter your password: ")
    while password != user:
        print("Wrong Password! Try again.")
        user = input("Please enter your password: ")
    print("Correct! You may enter...")

# VERSION 2
def version_two():
    password = "simonsnyc"
    num_guesses = 0

    while num_guesses < 3:
        user = input("Please enter your password: ")
        if user != password:
            print("Wrong Password! Try again.")
            num_guesses += 1
        else:
            print("Correct! You may enter...")
            break
    else:
        print("Too many incorrect attempts. Access denied.")

def main():
    choice = input("Which would you prefer? Version 1 or 2. Reply only with 1 or 2: ")
    if choice == "1":
        version_one()
    elif choice == "2":
        version_two()
    else:
        print("Invalid choice.")

# Run main function
if __name__ == "__main__":
    main()

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


