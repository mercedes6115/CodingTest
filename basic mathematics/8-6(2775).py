
n = int(input())

for _ in range(n):
    floor = int(input()) # 층 수
    num = int(input()) # 호 수
    people = [x for x in range(1, num + 1, 1)] # 사람들 수의 합
    #k층 n호 입주민 수 = k-1층 n-1호 입주민 수 + k-1층 n호 입주민 수

    for _ in range(floor):
        for i in range(1, num):
            people[i] += people[i - 1]

    print(people[1])
