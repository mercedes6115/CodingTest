list_x=[]
list_y=[]
for i in range(3):
    a,b = map(int,input().split())
    list_x.append(a)
    list_y.append(b)

for i in range(3):
    if list_x.count(list_x[i])==1:
        x = list_x[i]
    if list_y.count(list_y[i])==1:
        y = list_y[i]

print(x,y)

# 딱히 뭐라 할게 없는 문제
