n = int(input())

total = 0

while total >= 0:
    if n % 5 == 0 :
        total = total + (n // 5)    # 최소의 봉지 수를 구하기 때문에 큰 수로 먼저 나눠줌
        print(total)
        break
    n -= 3  # 나눠준 수에서 3씩 빼준다
    total += 1 # 봉지수는 하나씩 늘려줌

    if n < 0 : # 잘못입력된 경우는 -1을 출력하도록
        print("-1")
        break