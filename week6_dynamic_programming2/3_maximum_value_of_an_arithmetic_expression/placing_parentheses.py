import math
def calculator(a, b, op):
    """ Evaluate the expression (a op b)
    (int, int, char) -> (int) """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

def minMax(M, m, i, j, operators):
    """ Finds the best values i.e. min and max for a subproblem 
    (2D-array, 2D-array, int, int, list) -> (int, int) """
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = calculator(M[i][k], M[k+1][j], operators[k])
        b = calculator(M[i][k], m[k+1][j], operators[k])
        c = calculator(m[i][k], M[k+1][j], operators[k])
        d = calculator(m[i][k], m[k+1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value

def get_max_val(operands, operators):
    """ Adds parentheses to a given arithmetic expression to maximize its value 
    (list, list) -> (int) """
    n = len(operands)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = minMax(M, m, i, j, operators)

    return M[0][n-1]


if __name__ == "__main__":
    expression = input()
    operators, operands = [], []

    for i in expression:
        if i in ['+', '-', '*']:
            operators.append(i)
        else:
            operands.append(int(i))

    print(get_max_val(operands, operators))