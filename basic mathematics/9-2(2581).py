a = int(input())
b = int(input())
prime_number = [] # 이게 영어로 소수

for num in range(a, b+1):
    divisor = 2 # 소수는 약수가 2개 이므로 2로 설정
    if num > 1:
        for i in range(2, num):   # 전 문제에서 따오면 될줄 알았는데 전혀 아니다
            if num % i == 0: # 범위내 숫자로 순서대로 나눠서 나머지가 0인게 나오면 divisor 에다가 +1
                divisor += 1
                break
        if divisor == 2: # 범위내 숫자로 순서대로 나머지를 구할때 소수이면(1,나 자신)이면 약수가 2개 이대로 append
            prime_number.append(num)

if len(prime_number) == 0:  # 위 조건을 만족하지 않으면 -1 을 출력
    print(-1)
else:
    print(sum(prime_number))
    print(prime_number[0])


