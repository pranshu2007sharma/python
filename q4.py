def main():
    digit_names = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    char = input("Enter a single character: ")

    if len(char) != 1:
        print("Please enter exactly one character.")
        return

    if char.isalpha():
        print(f"'{char}' is a letter.")
        if char.isupper():
            print("It is uppercase.")
        else:
            print("It is lowercase.")
    elif char.isdigit():
        print(f"'{char}' is a numeric digit.")
        print(f"Its name in text is '{digit_names[char]}'.")
    else:
        print(f"'{char}' is a special character.")

if __name__ == "__main__":
    main()