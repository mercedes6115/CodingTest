n, m = list(map(int, input().split()))
permutation = []

def dfs1(a):
    if a == m:
        print(' '.join(map(str, permutation)))
        return
    for i in range(n):
            permutation.append(i+1)
            dfs1(a+1)
            permutation.pop()
dfs1(0)