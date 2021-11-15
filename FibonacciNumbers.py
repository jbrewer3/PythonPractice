def FibonacciNumbers(n):
    """
    Returns the `n`th fibonacci number, for positive `n`.
    """
    if 0 <= n <= 1:
        return n
    
    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n -1):
        result = n_minus2 + n_minus1 # 0 + 1, #
        n_minus2 = n_minus1 # n_minus2 = 1,
        n_minus1 = result #= 1,

    return result

for i in range(36):
    print(i, FibonacciNumbers(i))