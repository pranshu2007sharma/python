def print_cubes_dict():
    # Create a dictionary using dictionary comprehension
    cubes_dict = {key: key**3 for key in range(1, 6)}
    
    # Print the dictionary
    print(cubes_dict)

# Call the function
print_cubes_dict()