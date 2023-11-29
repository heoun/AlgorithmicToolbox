# Uses python3
import decimal 

def best_idx(ratios):
    best = 0.
    best_idx = 0


def get_optimal_value(capacity, weights, values):
    try:
        ratio = {}
        if capacity==0 or weights==0:
            return 0
        score = 0

        while capacity > 0:
            ratio={}
            if weights:
                for i in range(len(weights)):
                    ratio[i] = decimal.Decimal(values[i])/decimal.Decimal(weights[i])
                    ratio_val = list(ratio.values())
            else:
                break
            max_idx = max(ratio, key=ratio.get)
            if (weights[max_idx] >= capacity):
                score += capacity*ratio_val[max_idx]
                capacity = 0
                return score
            else:
                capacity -= weights[max_idx]
                score = ratio_val[max_idx]*weights[max_idx]
                weights.remove(weights[max_idx])
                values.remove(values[max_idx])

        return score

    except:
        print('capacity', capacity, 'weights', weights,'values',values)

def maximize_loot(capacity, weights, values):
    """Figure out the maximum value the thief can haul off

    Args:
     capacity (int): number of pounds backpack can hold
     weights (list): how many pounds of each item there is
     values (list): how much each item is worth per pound

    Raises:
     AssertionError: weights and values are different lengths

    Returns:
     float: max-value the backpack can hold
    """
    weight_count = len(weights)
    assert weight_count == len(values), \
	"Weights and Values not same shape: weights={} values={}".format(weight_count, len(values))
    values_per_pound = ((values[index]/weights[index], index)
			for index in range(weight_count))

    # we have to reverse-sort it (otherwise sorting puts the smallest
    # number first)
    per_poundage = sorted(values_per_pound, reverse=True)

    # loot is the value of what we've taken so far
    loot = 0

    # precondition: per_poundage is the value-per-pound in descending
    # order for each item along with the index of the original weight/value
    for value, index in per_poundage:
	# invariant: value is the largest price-per-pound available
        if capacity < weights[index]:
        # we don't have enough strength to take all of this item
        # so just take as much as we can and quit
            loot += value * capacity
            break
        # otherwise take all of this item
        loot += values[index]
        # reducing our capacity by its total weight
        capacity -= weights[index]
        if capacity == 0:
            # we're out of capacity, quit
            break
    return loot

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
    opt_value = maximize_loot(capacity, weights, values)
    # opt_value = get_optimal_value(capacity, weights, values) #capacity is the size of the backpack. n = number of items
    # if  "{:.10f}".format(opt_value) == '14036.5720221607' or "{:.10f}".format(opt_value) == '12619.0':
        # print(capacity, weights, values)
    # else:
    print("{:.10f}".format(opt_value))
