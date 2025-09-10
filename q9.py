import string

def process_file(file_name):
    try:
        with open(file_name, 'r') as file:
            # Read the file content
            content = file.readlines()

            # a. Total number of characters, words, and lines
            total_chars = 0
            total_words = 0
            total_lines = len(content)

            # b. Frequency of each character in the file (ignoring case and punctuation)
            char_freq = {}

            # d. Prepare to copy even and odd lines to separate files
            even_lines = []
            odd_lines = []

            # Loop through each line to gather necessary data
            for index, line in enumerate(content):
                # Strip the line of leading/trailing whitespaces
                stripped_line = line.strip()

                # a. Count characters and words
                total_chars += len(stripped_line)
                total_words += len(stripped_line.split())

                # b. Calculate the frequency of each character
                for char in stripped_line.lower():
                    if char in string.ascii_lowercase:  # Count only alphabetic characters
                        char_freq[char] = char_freq.get(char, 0) + 1

                # d. Add the line to even or odd lines
                if index % 2 == 0:  # Even line (index starts from 0)
                    even_lines.append(line)
                else:  # Odd line
                    odd_lines.append(line)

            # a. Print total characters, words, and lines
            print(f"Total number of characters: {total_chars}")
            print(f"Total number of words: {total_words}")
            print(f"Total number of lines: {total_lines}")

            # b. Print character frequency
            print("\nCharacter frequencies:")
            for char, count in sorted(char_freq.items()):
                print(f"{char}: {count}")

            # c. Print words in reverse order
            print("\nWords in reverse order:")
            words = ' '.join(content).split()
            print(" ".join(reversed(words)))

            # d. Copy even and odd lines to separate files
            with open("File1.txt", 'w') as even_file:
                even_file.writelines(even_lines)

            with open("File2.txt", 'w') as odd_file:
                odd_file.writelines(odd_lines)

            print("\nEven lines copied to 'File1.txt' and odd lines copied to 'File2.txt'.")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = "sample.txt"  # Replace with the actual file path
process_file(file_name)
