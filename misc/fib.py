def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        breakpoint()
        return a

# Calculate F6
n = 6
fn = fibonacci(n)
print(f'The fibonacci number of {n} is {fn}')
