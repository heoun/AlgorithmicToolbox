# Uses python3
#import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_recursion(a,b):
    if(b==0):
        return a
    # elif(b==a):
    #     return a
    return gcd_recursion(b,a%b)

if __name__ == '__main__':
    input = input() #sys.stdin.read()
    a, b = map(int, input.split())
    print(int((a*b)/gcd_recursion(a,b)))

