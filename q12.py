# Define the tuples
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
t2 = (11, 13, 15)

# a. Print half the values of the tuple in one line and the other half in the next line
mid = len(t1) // 2  # Calculate the midpoint

print("First half:", t1[:mid])  # Print the first half
print("Second half:", t1[mid:])  # Print the second half

# b. Print another tuple with only even numbers
even_numbers = tuple(x for x in t1 if x % 2 == 0)
print("Even numbers from t1:", even_numbers)

# c. Concatenate t2 with t1
combined_tuple = t1 + t2
print("Combined tuple (t1 + t2):", combined_tuple)

# d. Return the maximum and minimum values of the combined tuple
max_value = max(combined_tuple)
min_value = min(combined_tuple)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")