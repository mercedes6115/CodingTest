n, m = list(map(int, input().split()))
permutation = []

def dfs1(a):
    if len(permutation) == m:
        print(' '.join(map(str, permutation)))
        return
    for i in range(a,n+1):
            permutation.append(i)
            dfs1(i)
            permutation.pop()
dfs1(1)