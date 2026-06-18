def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_sequence(count):
    if count <= 0:
        print("Please enter a positive number.")
    else:
        print("Fibonacci sequence:")
        for i in range(count):
            print(fibonacci(i), end=" ")

num = int(input("Enter the number of terms: "))
print_fibonacci_sequence(num)