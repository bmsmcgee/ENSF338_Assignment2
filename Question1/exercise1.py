
# Fibonacci function
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n - 1) + func(n - 2)

