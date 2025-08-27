def print_pyramid(rows):
    # Print normal pyramid
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

def print_reverse_pyramid(rows):
    # Print reverse pyramid
    for i in range(rows, 0, -1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

def main():
    try:
        rows = int(input("Enter the number of rows: "))
        if rows <= 0:
            print("Please enter a positive integer.")
            return

        print_pyramid(rows)
        print_reverse_pyramid(rows)
        
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()