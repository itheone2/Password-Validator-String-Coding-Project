"""
Password Validator

This program validates a password based on the following criteria:
- Length between 8 and 12 characters
- Doesn't start with 'pass' or 'Pass'
- Contains at least 1 uppercase letter
- Contains at least 1 lowercase letter  
- Contains at least 1 number
- Contains at least 1 special character from: ! @ # $ % ^
- Doesn't contain the user's initials
- No character appears more than once

Author: John G
Date: March 16, 2025
"""

def check_password_length(sPassword):
    """Check if password length is between 8 and 12 characters"""
    if len(sPassword) < 8 or len(sPassword) > 12:
        return False
    return True

def check_password_start(sPassword):
    """Check if password starts with 'Pass' or 'pass'"""
    if sPassword.lower().startswith("pass"):
        return False
    return True

def check_uppercase(sPassword):
    """Check if password contains at least one uppercase letter"""
    for char in sPassword:
        if char.isupper():
            return True
    return False

def check_lowercase(sPassword):
    """Check if password contains at least one lowercase letter"""
    for char in sPassword:
        if char.islower():
            return True
    return False

def check_number(sPassword):
    """Check if password contains at least one number"""
    for char in sPassword:
        if char.isdigit():
            return True
    return False

def check_special_chars(sPassword):
    """Check if password contains at least one special character"""
    special_chars = "!@#$%^"
    for char in sPassword:
        if char in special_chars:
            return True
    return False

def check_initials(sPassword, sInitials):
    """Check if password contains user initials"""
    return sInitials.lower() not in sPassword.lower()

def check_repeating_chars(sPassword):
    """Check for repeating characters in password"""
    char_count = {}
    has_repeats = False

    # Count occurrences of each character (case-insensitive)
    for char in sPassword:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1

    # Check for characters that appear more than once
    repeated_chars = []
    for char, count in char_count.items():
        if count > 1:
            has_repeats = True
            repeated_chars.append((char, count))

    if has_repeats:
        print("These characters appear more than once:")
        for char, count in sorted(repeated_chars):
            print(f"{char}: {count} times")
        return False
    return True

def get_initials(sName):
    """Extract initials from full name"""
    names = sName.split()
    # Check if we have both first and last name
    if len(names) < 2:
        print("Please enter both first and last name")
        return None
    return names[0][0] + names[1][0]

def main():
    while True:
        # Get user's name and validate format
        sName = input("Enter full name such as John Smith: ")
        sInitials = get_initials(sName)
        if sInitials is None:
            continue

        # Get password
        sPassword = input("Enter new password: ")

        # Check all conditions and print appropriate messages
        is_valid = True

        if not check_password_length(sPassword):
            print("Password must be between 8 and 12 characters")
            is_valid = False

        if not check_password_start(sPassword):
            print("Password can't start with Pass.")
            is_valid = False

        if not check_uppercase(sPassword):
            print("Password must contain at least 1 uppercase letter")
            is_valid = False

        if not check_lowercase(sPassword):
            print("Password must contain at least 1 lowercase letter")
            is_valid = False

        if not check_number(sPassword):
            print("Password must contain at least 1 number")
            is_valid = False

        if not check_special_chars(sPassword):
            print("Password must contain at least 1 of these special characters: ! @ # $ % ^")
            is_valid = False

        if not check_initials(sPassword, sInitials):
            print("Password must not contain user initials.")
            is_valid = False

        if not check_repeating_chars(sPassword):
            is_valid = False

        if is_valid:
            print("Password is valid and OK to use.")
        break

if __name__ == "__main__":
    main()
