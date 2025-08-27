def frequency_of_char(s, ch):
    return s.count(ch)

def replace_char(s, old, new):
    return s.replace(old, new)

def remove_first_occurrence(s, ch):
    index = s.find(ch)
    if index == -1:
        return s  # character not found
    return s[:index] + s[index+1:]

def remove_all_occurrences(s, ch):
    return s.replace(ch, '')

def main():
    s = input("Enter the string: ")

    # 1. Frequency of character
    ch = input("Enter character to find frequency: ")
    freq = frequency_of_char(s, ch)
    print(f"Frequency of '{ch}' in string: {freq}")

    # 2. Replace character
    old_char = input("Enter character to replace: ")
    new_char = input("Enter new character: ")
    replaced_string = replace_char(s, old_char, new_char)
    print(f"String after replacing '{old_char}' with '{new_char}': {replaced_string}")

    # 3. Remove first occurrence of character
    ch_remove_first = input("Enter character to remove first occurrence: ")
    removed_first = remove_first_occurrence(s, ch_remove_first)
    print(f"String after removing first occurrence of '{ch_remove_first}': {removed_first}")

    # 4. Remove all occurrences of character
    ch_remove_all = input("Enter character to remove all occurrences: ")
    removed_all = remove_all_occurrences(s, ch_remove_all)
    print(f"String after removing all occurrences of '{ch_remove_all}': {removed_all}")

if __name__ == "__main__":
    main()