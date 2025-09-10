import re

# Custom exception class
class InvalidNameError(Exception):
    pass

def validate_name(name):
    # Check if the name contains digits or special characters
    if not re.match("^[a-zA-Z ]*$", name):  # Only allows alphabets and spaces
        raise InvalidNameError("Name should only contain alphabets and spaces.")
    return name

def main():
    try:
        # Accept name input from the user
        name = input("Enter your name: ")

        # Validate the name
        valid_name = validate_name(name)

        print(f"Hello, {valid_name}!")
    
    except InvalidNameError as e:
        print(f"Invalid input: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()