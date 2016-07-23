"""
Fibonacci numbers explained: https://en.wikipedia.org/wiki/Fibonacci_number

Assumption: For this exercise please assume that the Fibonacci numbers start at 0.

Next Fibonacci Number Problem:
Your program will accept integers from stdin.
The first number you read will be the number of integers remaining in the stream.
For each following integer, print the first Fibonacci number larger than it.

Constraints:
Your output lines should not have any trailing or leading whitespaces
Your program should run correctly for the first 60 Fibonacci Numbers

Example Input:

2
9
22
Example Output:

13
34
Example Output Explanation:

13 is the next Fibonacci number greater than 9.
34 is the next Fibonacci number greater than 22.
"""
# return the next Fibonacci number greater than n
def next_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    res = 0
    while b < n:
        a, b = b, a+b
        res = b
    return res


if __name__ == '__main__':
    # Input
    num_elements = int(raw_input())
    arr = [int(raw_input()) for i in range(num_elements)]

    result = []
    for n in arr:
        result.append(next_fib(n))

    # Output
    for num in result:
        print num
