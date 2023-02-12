import sys
import os
from os import path
import json
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

__location__ = os.path.realpath(path.join(
    os.getcwd(), path.dirname(__file__)))


def main():
    with open(os.path.join(__location__, 'data.json'), 'r') as file:
        data = json.load(file)

    times = []
    input_sizes = []
    num_arrays = len(data) - 1
    for i in range(num_arrays):
        high = len(data[i]) - 1
        time = timeit.timeit(lambda: func1(data[i], 0, high), number=10)
        print(f'Elapsed time: {time} seconds')
        input_sizes.append(len(data[i]))
        times.append(time)

    plt.plot(input_sizes, times)
    plt.show()


def func1(arr, low, high):
    while (low < high):
        pi = func2(arr, low, high)
        if (pi - low < high - pi):
            func1(arr, low, pi - 1)
            low = pi + 1
        else:
            func1(arr, pi + 1, high)
            high = pi - 1


def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1

        while low <= high and array[low] <= p:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]

        else:
            break

    array[start], array[high] = array[high], array[start]
    return high


if __name__ == "__main__":
    main()
