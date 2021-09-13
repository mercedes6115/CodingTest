'''
홀수 -> 분자 n~1 분모 1~n
짝수 -> 분모 n~1 분자 1~n
입력한 수가 몇번째 라인에 있는지 확인 20 이면 (1+2+3+4+5) < 20 < (1+2+3+4+5+6) 이니 6번째 라인
6번째 라인이면 짝수 라인 이면 그 라인의 총합 21 에서 20을 뺴주고 분자와 분모를 설정
분자 -> num (몇번째라인) - (a - num_count(그 전라인 의총합)) + 1
분모 -> 입력값 - 그 전라인의 총합
라인에 따라 분모 분자 설정 반대로 해주면 됨
'''
a = int(input())
num_list = []

num = 0
num_count = 0

while num_count < a:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    i = a - num_count
    j = num - i + 1
else:
    i = num - (a - num_count) + 1 # 분자
    j = a - num_count # 분모

print(f"{i}/{j}")