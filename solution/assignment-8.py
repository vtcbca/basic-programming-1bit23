def print_alphabet_pattern(n):
    for i in range(1, n + 1):
        # Calculate leading spaces to center the pattern
        spaces = ' ' * (n - i)

        # Create the first half of the alphabet sequence
        first_half = [chr(65 + j) for j in range(i)]  # chr(65) = 'A'

        # Create the second half (reverse of the first half without the last element)
        second_half = first_half[:-1][::-1]

        # Combine the two halves to create the full row
        row = first_half + second_half

        # Print the pattern with spaces to align it properly
        print(spaces + ' '.join(row))

# Example usage
num_lines = int(input("Enter the number of lines: "))
print_alphabet_pattern(num_lines)
