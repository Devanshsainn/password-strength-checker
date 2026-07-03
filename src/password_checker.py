def check_length(password):
    """Check if the password meets the minimum length requirement."""
    return len(password) >= 8


def check_uppercase(password):
    """Check if the password contains at least one uppercase letter."""
    return any(char.isupper() for char in password)


def check_lowercase(password):
    """Check if the password contains at least one lowercase letter."""
    return any(char.islower() for char in password)


def check_digits(password):
    """Check if the password contains at least one digit."""
    return any(char.isdigit() for char in password)


import string


def check_special_characters(password):
    """Check if the password contains at least one special character."""
    return any(char in string.punctuation for char in password)


def main():
    password = input("Enter a password: ")

    print("\nPassword Analysis")
    print("-" * 20)

    if check_length(password):
        print("✅ Length: Good")
    else:
        print("❌ Length: Password must be at least 8 characters long.")

    if check_uppercase(password):
        print("✅ Uppercase Letter: Present")
    else:
        print("❌ Uppercase Letter: Missing")

    if check_lowercase(password):
        print("✅ Lowercase Letter: Present")
    else:
        print("❌ Lowercase Letter: Missing")

    if check_digits(password):
        print("✅ Number: Present")
    else:
        print("❌ Number: Missing")

    if check_special_characters(password):
        print("✅ Special Character: Present")
    else:
        print("❌ Special Character: Missing")


if __name__ == "__main__":
    main()