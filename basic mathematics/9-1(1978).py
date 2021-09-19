n=int(input())
num=list(map(int,input().split( )))
for i in num:
    if i==1:
        n-=1
    for j in range(2,i): # 1과 자기자신인 i를 제외한 범위 설정
        if i%j==0: # 한번이라도 나누어 떨어지면 소수가 아님
            n-=1 #  위의 조건문에 해당 되는 경우 n을 하나씩 제거
            break # 소수가 아닌 걸 체크 했으므로 break를 걸어줌
print(n)
