N = int(input())
number = 2 # 2로 나누기 시작

while N != 1:
    if N % number == 0:
        print(number)
        N = N // number
    else:
        number += 1
# 소인수 분해가 걍 나누는 과정 보여주면 되니까