a = int(input())
b=2
i = 1
while True:
    if a == 1:
        print("1")
        break
    if a  >=(3*i*i-3*i+1) and a <= (3*(i+1)*(i+1)- 3*(i+1)+1):
        print(b)
        break
    else:
        b = b + 1
    i = i + 1
