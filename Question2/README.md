# ENSF338_Assignment2

Repository for Assignment2

1.  This code is an implementation of the quick-sort algorithm where func1 takes in an array along with a high and low bound, these bounds specify the beginning and end of the array. This quicksort uses recursion to slowly increment the pivot point (pi) towards the center of the array which we can see in the func1 calls where pi - 1 or pi + 1 is used in the end and start arguments respectively. In func2 is where all the comparisons and actual sorting happen, it is in func2 that the values of the array at the high index are compared to the pivot point selected in func2 (p) as well as comparing the low index to the pivot and then once we have found values at two indexes where they should not be we swap positions. It is important to note that there are essentially two pivots going on, one in func1 and another in func2 this is because func1 uses the pivot to partition the array into two parts and then inside each of those partitions func2 will go in and compare numbers and sort.

### Average Case Complexity

As this algorithm is a implemenation of the quick sort we know that the average case complexity is

2.

3.  The results from timing the algorithms yielded the expected values described by the complexity analysis. When plotted we were able to determine that the graph was characteristic of exponential growth, specifically that of a 2nd order growth equation.
