def print_number_triangle(n):
    for i in range(1, n + 1):
        # Calculate spaces to center the numbers
        spaces = ' ' * (n - i)
        
        # Generate the numbers from 1 to (2*i - 1)
        numbers = ' '.join(str(x) for x in range(1, 2 * i))
        
        # Print the pattern for the current row
        print(spaces + numbers)

# Example usage
num_lines = int(input("Enter the number of lines: "))
print_number_triangle(num_lines)
