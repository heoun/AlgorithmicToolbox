# Uses python3
import sys

def optimal_sequence(n):
    hop_ct = [0] * (n + 1)

    # Path from 1 to 1 is 1.
    hop_ct[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)

        # Get the index with the least hop count to 1.
        min_hops = min([hop_ct[x] for x in indices])

        # Write hop count from current index to 1. Hop count incremented by 1.
        hop_ct[i] = min_hops + 1

    # ptr points to current position of hop_ct.
    ptr = n
    best_seq = [ptr]
    while ptr != 1:

        # The list contains next hop candida.
        candida = [ptr - 1]
        if ptr % 2 == 0:
            candida.append(ptr // 2)
        if ptr % 3 == 0:
            candida.append(ptr // 3)

        # Choose from the candida whose hop count is the least.
        ptr = min(
            [(c, hop_ct[c]) for c in candida],
            key=lambda x: x[1]
        )[0]
        best_seq.append(ptr)

    return reversed(best_seq)
input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
