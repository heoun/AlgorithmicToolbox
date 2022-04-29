# Uses python3
import sys

def get_change(m):
    #write your code here
    coin = 0
    while m >= 10:
        coin +=1
        m = m - 10
    while m >= 5:
        coin +=1
        m = m -5
    if m >= 1:
        coin += m
    return coin

    # return m

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
