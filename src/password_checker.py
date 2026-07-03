def check_length(password):
    """Check if the password meets the minimum length requirement."""
    return len(password) >= 8


def main():
    password = input("Enter a password: ")

    print("\nPassword Analysis")
    print("-" * 20)

    if check_length(password):
        print("✅ Length: Good")
    else:
        print("❌ Length: Password must be at least 8 characters long.")


if __name__ == "__main__":
    main()