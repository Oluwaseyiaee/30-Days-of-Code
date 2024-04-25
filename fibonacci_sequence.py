def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Generate Fibonacci sequence with user input
fibonacci_sequence = int(input("What is the number of terms you want to take in? "))
print(fibonacci(fibonacci_sequence))

