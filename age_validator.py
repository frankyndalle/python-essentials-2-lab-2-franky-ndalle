
# Lab 2 - Task 3: Custom Exception Test (Age Validator)

def validate_age(age):
    """Raise ValueError if age is outside the range 0 to 120."""
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120 inclusive.")


try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Age accepted.")
except ValueError as error:
    print("Error:", error)
