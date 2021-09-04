'''

T= input()    # 4단계 1번
T = int(T)
while  True:
    a,b=map(int,input().split(''))
    if a==0 and b==0:
        break
    print(a+b)

   # 4단계 2번
while  True:
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break

# 4단계 3번


f=int(input())
fir=f
count=0

while True:
    a = f // 10 #몫
    b = f % 10 # 나머지
    c = (a + b) % 10 # 결과의 끝자리
    f = (b * 10) + c #
    count += 1

    if fir == f:
        break
print(count)

'''