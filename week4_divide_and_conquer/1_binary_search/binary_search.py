import math

def binary_search(keys, query, right):
    # write your code here
    low = 0
    if right < low :
        return low-1
    mid = math.floor((low + right)/2)

    if keys[mid] == query:
        return mid
    elif keys[mid] > query:
        return binary_search(keys, query, right -1)
    elif keys[mid] < query:
        return binary_search(keys, query, right)

def binary_search_proper(list_values, query, r):
    l = 0
    while l < r:
        m = (l+r)//2
        if query > list_values[m]:
            l = m + 1 
        elif query < list_values[m]:
            r = m
        else:
            return m
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        # print(binary_search(input_keys, q, num_keys), end=' ')
        print(binary_search_proper(input_keys, q, num_keys), end=' ')