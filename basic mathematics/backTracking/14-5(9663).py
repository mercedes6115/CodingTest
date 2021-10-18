n = int(input())
col = [0 for i in range(15)]  # i번째 행에서 퀸이 놓여 있는 열
cnt = 0

def prob(i):
    for k in range(i):
        # k번째 행에 있는 퀸이 같은 열에 있는지 검사: col(i) = col(k)
        # k번째 행에 있는 퀸이 같은 대각선에 있는지 검사: |col(i)-col(k)| = i-k
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            return False
    return True

def queen(i):
    global cnt
    if i == n:
        cnt += 1
    else:
        for j in range(n):
            col[i] = j
            if prob(i):
                queen(i + 1)
queen(0)
print(cnt)
