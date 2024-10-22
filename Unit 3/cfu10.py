#Nabila Raisa 10/21/2024 01 and 02

import random

ran_num = randomrandint(1,10)

initial_attempt = 0

def guess_number(initial_attempt, ran_num):
    attempts += 1
    
    guess = int(input("Enter a random number between 1 and 10!"))
    
    if guess == ran_num:
        print(f"That is correct! It took you {attempts}")
