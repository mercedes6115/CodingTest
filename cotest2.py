def getMinimumMoves(arr):
    sorted_index = {elem: i for i, elem in enumerate(sorted(arr))}
    moves = 0
    for idx, elem in enumerate(arr):
        if idx != sorted_index[elem] + moves:
            moves += 1
    return moves