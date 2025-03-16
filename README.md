# Password Validator

A Python script that checks passwords against security requirements. Validates length, character types, and ensures no repeated characters. Built using basic Python string methods without relying on regex.

## Features

- Validates password length (8-12 characters)
- Ensures password doesn't start with "Pass" or "pass"
- Requires at least one uppercase letter
- Requires at least one lowercase letter
- Requires at least one number
- Requires at least one special character (!, @, #, $, %, ^)
- Prevents passwords containing the user's initials
- Checks that no character appears more than once
- Provides clear feedback on validation failures

## Usage

Simply run the program:

```
python password_validator.py
```

Follow the prompts to:
1. Enter your full name (first and last)
2. Enter your desired password
3. View validation results

If the password is invalid, you'll receive specific feedback about which requirements weren't met. You can then try again with a new password.

## Sample Output

```
Enter full name such as John Smith: Brian Candido
Enter new password: BC12345
Password must be between 8 and 12 characters
Password must contain at least 1 lowercase letter
Password must contain at least 1 of these special characters: ! @ # $ % ^
Password must not contain user initials.

Enter new password: abc!123
Password must be between 8 and 12 characters
Password must contain at least 1 uppercase letter
Password must not contain user initials.

Enter new password: PassW0rd
Password can't start with Pass.
Password must contain at least 1 of these special characters: ! @ # $ % ^
These characters appear more than once:
s: 2 times

Enter new password: Mkc!0618
Password is valid and OK to use.
```

## Requirements

- Python 3.x
- No external libraries required

## Educational Context

This project was developed as a final assignment for a Python programming course, demonstrating the use of:
- Variables and type conversions
- Logical and looping constructs
- Functions
- String manipulation methods
- Input validation
