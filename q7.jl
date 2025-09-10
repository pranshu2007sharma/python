def find_occurrences(s1, s2):
    # List to store the starting indices of all occurrences
    indices = []
    
    # Start searching from the beginning of s1
    start = 0
    
    # Loop through s1 and find all occurrences of s2
    while start < len(s1):
        # Find the index of the next occurrence of s2
        index = s1.find(s2, start)
        
        # If find() returns -1, break the loop as no more occurrences are found
        if index == -1:
            break
        
        # Append the index to the list
        indices.append(index)
        
        # Move the start index to the next position after the found occurrence
        start = index + 1
    
    # Return the list of indices or 1 if no occurrences were found
    return indices if indices else 1

# Example usage
string1 = "ababcabcabc"
string2 = "abc"

result = find_occurrences(string1, string2)
print("Indices of occurrences:", result)
