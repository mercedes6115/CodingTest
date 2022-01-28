n, m = list(map(int, input().split()))
permutation = []

def dfs1(first):
    if len(permutation) == m:
        print(' '.join(map(str, permutation)))
        return
    for i in range(first,n+1):
        if i not in permutation:
            permutation.append(i)
            dfs1(i+1)
            permutation.pop()
dfs1(1)