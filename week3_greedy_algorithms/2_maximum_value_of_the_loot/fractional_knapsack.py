# Uses python3

def best_idx(ratios):
    best = 0.
    best_idx = 0


def get_optimal_value(capacity, weights, values):
    ratio = {}
    if capacity==0 or weights==0:
        return 0
    score = 0

    while capacity > 0 and weights:
        ratio={}
        # print(weights,capacity)
        for i in range(len(weights)):
            ratio[i] = values[i]/weights[i]
        
        ratio_val = list(ratio.values())

        max_idx = max(ratio, key=ratio.get)
        if (weights[max_idx] >= capacity):
            score += capacity*ratio_val[max_idx]
            capacity = 0
            # print(weights,values,capacity)
            return score
        else:
            capacity -= weights[max_idx]
            score = ratio_val[max_idx]*weights[max_idx]
            weights.remove(weights[max_idx])
            values.remove(values[max_idx])
   
    return score


if __name__ == "__main__":
    data = list(map(int, input().split()))
    # print(data)
    n, capacity = data[0:2]
    # values = data[2:(2 * n + 2):2] #2:4:2 - print every 2nd character from 2 to 4
    # weights = data[3:(2 * n + 2):2]
    
    values = [0]*n
    weights = [0]*n
    for i in range(n):
        values[i], weights[i] = map(int, input().split())
    
    opt_value = get_optimal_value(capacity, weights, values) #capacity is the size of the backpack. n = number of items
    print("{:.10f}".format(opt_value))
