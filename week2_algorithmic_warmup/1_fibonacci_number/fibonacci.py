# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    list_fib = []
    # if n != 0:a
    for i in range(n+1):
        if (i > 1):
            current_fib = list_fib[i-1] + list_fib[i-2]
            list_fib.append(current_fib)
        elif (i ==1):
            list_fib.append(1)
        elif (i == 0):
            list_fib.append(0)
    return list_fib[n]
    # elif n == 0:
    #     return 0

n = int(input())
print(calc_fib_fast(n))
