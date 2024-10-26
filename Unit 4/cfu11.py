def print_numbers_10_to_70():
    for num in range(10, 71, 10):
        print(num)

def print_numbers_0_to_10():
    num = 0
    while num <= 10:
        print(num)
        num += 0.5

def sing_99_bottles():
    bottles = 99
    while bottles > 0:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        print(f"Take one down, pass it around, {bottles} bottles of beer on the wall.\n")
    print("No more bottles of beer on the wall.")

def main():
    choice = input("Enter 1 for printing numbers 10 to 70, 2 for numbers 0 to 10, or 3 for the song: ")
    if choice == '1':
        print_numbers_10_to_70()
    elif choice == '2':
        print_numbers_0_to_10()
    elif choice == '3':
        sing_99_bottles()
    else:
        print("Invalid choice.")

# Run the main program
main()
