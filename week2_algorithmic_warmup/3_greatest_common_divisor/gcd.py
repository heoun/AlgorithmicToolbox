# Uses python3
# import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_fast(a,b):
    current_gcd = 0
    larger_num = b
    smaller_num = a
    if a > b:
        larger_num = a
        smaller_num = b

    if larger_num % smaller_num ==0:
        return smaller_num
    while larger_num % smaller_num != 0:
        remainder = larger_num % smaller_num
        larger_num = smaller_num
        smaller_num = remainder
    return larger_num

def gcd_recursion(a,b):
    if(b==0):
        return a
    # elif(b==a):
    #     return a
    return gcd_recursion(b,a%b)

if __name__ == "__main__":
    # input = sys.stdin.read()
    input = input()
    a, b = map(int, input.split())
    # print(gcd_naive(a, b))
    # print(gcd_fast(a,b))
    print(gcd_recursion(a,b))