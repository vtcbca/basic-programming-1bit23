def print_star_pattern(n):
    for i in range(1, n + 1):
        print("* " * i)  # Print i stars, each followed by a space

# Example usage
num_rows = int(input("Enter the number of rows: "))
print_star_pattern(num_rows)
