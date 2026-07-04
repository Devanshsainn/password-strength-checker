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

def calculate_score(password):
    """Calculate the password strength score."""

    score = 0

    if check_length(password):
        score += 1

    if check_uppercase(password):
        score += 1

    if check_lowercase(password):
        score += 1

    if check_digits(password):
        score += 1

    if check_special_characters(password):
        score += 1

    return score

def get_strength_label(score):
    """Return a descriptive strength label based on the score."""

    if score <= 2:
        return "🔴 Weak"

    elif score == 3:
        return "🟡 Moderate"

    elif score == 4:
        return "🟢 Strong"

    else:
        return "🟢 Very Strong"
    

def print_result(condition, success_message, failure_message):
    """Print the result of a password validation."""

    if condition:
        print(f"✅ {success_message}")
    else:
        print(f"❌ {failure_message}")


def main():
    password = input("Enter a password: ")

    print("\nPassword Analysis")
    print("-" * 20)

    print_result(
    check_length(password),
    "Length: Good",
    "Length: Password must be at least 8 characters long."
)

    print_result(
    check_uppercase(password),
    "Uppercase Letter: Present",
    "Uppercase Letter: Missing"
)

    print_result(
    check_lowercase(password),
    "Lowercase Letter: Present",
    "Lowercase Letter: Missing"
)

    print_result(
    check_digits(password),
    "Number: Present",
    "Number: Missing"
)

    print_result(
    check_special_characters(password),
    "Special Character: Present",
    "Special Character: Missing"
)

    score = calculate_score(password)

    print(f"\nPassword Score: {score}/5")
    print(f"Password Strength: {get_strength_label(score)}")

if __name__ == "__main__":
    main()