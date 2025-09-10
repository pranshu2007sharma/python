def cube_of_even_integers(input_list, use_comprehension=True):
    if use_comprehension:
        # List comprehension to filter even integers and cube them
        cubes = [x ** 3 for x in input_list if isinstance(x, int) and x % 2 == 0]
    else:
        # Initialize an empty list to store the cubes
        cubes = []
        
        # Loop through the input list
        for x in input_list:
            # Check if the element is an integer and even
            if isinstance(x, int) and x % 2 == 0:
                cubes.append(x ** 3)  # Cube and add it to the list
    
    return cubes

# Example usage
input_list = [1, 2, 'hello', 3.5, 4, 6, 'world', 7, 8]

# Using list comprehension (True)
result_comprehension = cube_of_even_integers(input_list, use_comprehension=True)
print("Cubes of even integers (list comprehension):", result_comprehension)

# Using for loop (False)
result_for_loop = cube_of_even_integers(input_list, use_comprehension=False)
print("Cubes of even integers (for loop):", result_for_loop)