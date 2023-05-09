#all the imports
from tools.numbers.col import listFNames, listLNames
from tools.numbers.simp import add_numbers, sub_numbers
from tools.numbers.comp import sum_of_digit, ispal

#the combined lists are called first with the /app.py

#the simple menu
def simp_menu():
    """Displays the simp menu options and prompts the user to select an action."""
    print("\n=== Simple Math Menu ===")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Exit")

    # Wait for the user to choose an option
    choice = input("\nSelect an action (1-3): ")

    # Process the user's choice
    if choice == "1":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = add_numbers(num1, num2)
        print(f"\n{num1} + {num2} = {result}")
    elif choice == "2":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = sub_numbers(num1, num2)
        print(f"\n{num1} - {num2} = {result}")
    elif choice == "3":
        raise SystemExit  # Exit the program
    else:
        print("Invalid choice.")


#the complex menu
def comp_menu():
    """Displays the comp menu options and prompts the user to select an action."""
    print("\n=== Complex Math Menu ===")
    print("1. Sum the digits of a number")
    print("2. Check if a number is a palindrome")
    print("3. Exit")

    # Wait for the user to choose an option
    choice = input("\nSelect an action (1-3): ")

    # Process the user's choice
    if choice == "1":
        num = int(input("Enter a number: "))
        result = sum_of_digit(num)
        print(f"\nThe sum of the digits in {num} is {result}")
    elif choice == "2":
        num = int(input("Enter a number: "))
        if ispal(num):
            print(f"\n{num} is a palindrome")
        else:
            print(f"\n{num} is not a palindrome")
    elif choice == "3":
        raise SystemExit  # Exit the program
    else:
        print("Invalid choice.")


# Display the simp menu first
simp_menu()

# Once the user has used a function from the simple menu, they can access the complex menu
print("\nYou have now unlocked the Complex Math Menu!")
comp_menu()