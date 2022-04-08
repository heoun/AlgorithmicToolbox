# import logging
# logging.basicConfig()

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers, n):
    max_index1 = -1
    # print(n)
    for i in range(n):
        if (max_index1 == -1) or (numbers[i] > numbers[max_index1]):
            max_index1 = i
    # print('max1', max_index1, n)
    
    if n > 1:
        max_index2 = -1
        # print('max2',numbers[max_index2])
        for j in range(n):
            if (j != max_index1) & ((max_index2 == -1) or (numbers[j] > numbers[max_index2])):
                max_index2 = j
            # print('iter2',max_index2)
        # print(numbers[max_index1], numbers[max_index2])
        return (numbers[max_index1] * numbers[max_index2])
    else:
        # print(n)
        return (numbers[max_index1])

# def test_case():
#     import sys
#     n = int(sys.argv[1])
#     print(n)
#     print('_'.join([str(i*2) for i in range(n)]))

if __name__ == '__main__':
    input_n = int(input()) #the input is turned into a integer for the number
    input_numbers = [int(x) for x in input().split()] #splitting the 1,2,3 by the spaces
  
    # assert (len(input_numbers) == input_n)
    print(max_pairwise_product_fast(input_numbers,input_n))
