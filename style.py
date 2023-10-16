def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage
num_terms = 10
fibonacci_sequence = fibonacci(num_terms)
print("Fibonacci Sequence:", fibonacci_sequence)
