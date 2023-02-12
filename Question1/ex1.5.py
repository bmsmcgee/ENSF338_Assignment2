import timeit
import matplotlib.pyplot as plt
import numpy as np


# Memoization
def fibmemo(n, cache={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibmemo(n-1) + fibmemo(n-2)
            return cache[n]

# Recursive
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n - 1) + func(n - 2)

if __name__ == "__main__":
    memoTime = [timeit.timeit(lambda : fibmemo(i), number=1) for i in range(36)]
    recTime = [timeit.timeit(lambda : func(i), number=1) for i in range(36)]

    print(sum(memoTime))
    print(len(memoTime))

    memoTimeSum = np.cumsum(memoTime)
    recTimeSum = np.cumsum(recTime)
        
    plt.plot(memoTimeSum * 100000, label="Memoization (x100000)")
    plt.plot(recTimeSum, label="Recursive")
    plt.title('Time taken for Fibonacci Sequence for Two Different Function Types:\nMemoization [O(n)] and Recursive [O(2^n)]')
    plt.xlabel("Fibonacci Number")
    plt.ylabel("Time (s)")
    plt.legend(loc='upper left')

    plt.show()
    plt.close()