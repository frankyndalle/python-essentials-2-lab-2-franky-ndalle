
# Lab 2 - Task 2: List Management with Error Handling

numbers = []

while True:
    print("\nList Manager")
    print("(a) Add a number")
    print("(b) Remove a number")
    print("(c) Display the list")
    print("(d) Quit")

    choice = input("Choose an option: ").lower()

    if choice == "a":
        try:
            number = int(input("Enter an integer to add: "))
            numbers.append(number)
            print("Number added successfully.")
        except ValueError:
            print("Error: Please enter a valid integer.")

    elif choice == "b":
        try:
            index = int(input("Enter the index to remove: "))
            removed_number = numbers.pop(index)
            print("Removed number:", removed_number)
        except ValueError:
            print("Error: Please enter a valid integer index.")
        except IndexError:
            print("Error: Invalid index. No number was removed.")

    elif choice == "c":
        print("Current list:", numbers)

    elif choice == "d":
        print("Goodbye!")
        break

    else:
        print("Error: Invalid option. Choose a, b, c, or d.")
