# Python Essentials 2 — Lab 2
## Strings, String and List Methods, Exceptions

**Author:** Franky Ndalle

## Task 1: String Manipulation Challenge

**File:** `string_manipulation.py`

Prompts the user for a sentence and displays the sentence in uppercase, in reverse order, the total number of vowels regardless of case, and the sentence with spaces replaced by hyphens.

## Task 2: List Management with Error Handling

**File:** `list_manager.py`

Provides a menu to add integers, remove an element by index, display the current list, and quit. It handles non-integer input and invalid indexes using `try`/`except` without abruptly terminating the program.

## Task 3: Custom Exception Test (Age Validator)

**File:** `age_validator.py`

Defines `validate_age(age)`, which raises a `ValueError` if the age is outside the inclusive range of 0 to 120. The calling code catches errors and reports whether the age is accepted.

## Sample Output Evidence

The `outputs` folder contains text logs demonstrating the behavior of all three programs:

- `outputs/string_manipulation_output.txt`
- `outputs/list_manager_output.txt`
- `outputs/age_validator_output.txt`

## How to Run

Run these commands from the project folder:

```bash
python string_manipulation.py
python list_manager.py
python age_validator.py
```

## Requirements

- Python 3

No third-party packages are required for this lab.
