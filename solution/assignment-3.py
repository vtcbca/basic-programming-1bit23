def fibonacci_terms(n):
    fib_sequence = []
    a, b = 0, 1  # Starting values of the Fibonacci sequence
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers
    return fib_sequence

# Example usage
num_terms = int(input("Enter the number of terms: "))
sequence = fibonacci_terms(num_terms)
print(f"The Fibonacci sequence up to {num_terms} terms is: {sequence}")
