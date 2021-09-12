def countMoves(numbers):
    n=len(numbers)
    sm = sum(numbers)
    small = min(numbers)
    minOperation = sm - (n * small)
    return minOperation