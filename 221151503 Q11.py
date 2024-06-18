def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence[:n]

n = int(input("Enter the length of the Fibonacci sequence: "))
print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci(n)}")
