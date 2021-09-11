a,b,c = map(int,input().split()) # 순서대로 고정비용, 가변비용, 가격

'''
A + Bx = Cx
A = (C-B)x
C - B < 0 즉 C < B 이면 손익분기점이 발생 불가능
x = A // (C - B)
그 수를 + 1 출력 
'''
if b >= c: # 가변비용이 가격보다 크면 손기분익점이 발생하지 않으므로 -1
    print(-1)
else :
    n = a // (c-b) # 손익분기점이 발생하는 경우는
    print(n+1)
