n, m = list(map(int, input().split()))
permutation = []
'''check=[False]*(n)
def dfs(depth,n,m):
    if len(permutation) == m: #출력길이를 만족하는경우 출력
        print(' '.join(map(str, permutation)))
        return
    for i in range(n):
        if check[i]:
            continue # 해당 값이 트루면 건너뒤고 다음 진행
        check[i]=True # 갑을 트루로 저장 이건 가지를 방문했으며 true 안했으면 false 이런식
        permutation.append(i+1) # i번째를 기준으로 새로운 가지치기를 진행
        dfs(depth+1,n,m) # 끝나면 깊이를 1만큼 늘려주고 다음 가지로 진행
        permutation.pop() # 끝났으면 가지치기
        check[i]=False#방문안한 상태로 초기화

dfs(0,n,m)
# 깊이라는 인자를 추가해줘서 겨우 풀었다 생각해보니 깊이가 없으니 언제 pop을 시켜야할지 모르니까 재귀식으로 길이를 정해주니 풀림
'''

def dfs1():
    if len(permutation) == m:
        print(' '.join(map(str, permutation)))
        return
    for i in range(1,n+1):
        if i not in permutation:
            permutation.append(i)
            print(permutation)
            dfs1()
            permutation.pop()
            print(permutation)


dfs1()