'''

a= input()    # 3단계 1번
a = int(a)

for i in range(1,10):
    print(a ,"*", i ,"=", a*i)

T= input()    # 3단계 2번
T = int(T)
for i in range (T):
    a,b=map(int,input().split())
    print(a+b)

s= input()    # 3단계 3번
s = int(s)
print(s*(s+1)//2)

import sys
T= int(sys.stdin.readline().rstrip())
    # 3단계 4번
T = int(T)
for i in range (T):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)

s= input()    # 3단계 5번
s = int(s)

while s>0:
    print(s)
    s-=1

T= input()    # 3단계 6번
T = int(T)
for i in range (T):
    a,b=map(int,input().split())
    print(f'Case #{i+1}: {a+b}')

T= input()    # 3단계 7번
T = int(T)
for i in range (T):
    a,b=map(int,input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')

T= input()    # 3단계 8번
T = int(T)
for i in range(1,T+1):
    print(" "*(T-i) + "*"*i)

a,b=map(int,input().split()) # 3-9번
c=list(map(int,input().split()))
for i in range(a):
    if b > c[i]:
        print(c[i],end=" ")
'''