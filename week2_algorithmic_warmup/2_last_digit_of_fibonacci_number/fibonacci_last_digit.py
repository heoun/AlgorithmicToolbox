# Uses python3
# import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def fib_fast(n):
    a, b = 0, 1
    for i in range(n % 60):
        a, b = b, (a + b) % 10
    return a    

if __name__ == '__main__':
    # input = sys.stdin.read()
    input = input()
    n = int(input)
    print(fib_fast(n))
    # print(get_fibonacci_last_digit_naive(n))
