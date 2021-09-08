def a(n):
    cnt = 0
    for i in range(1, n+1):
        list1 = list(map(int,str(i)))
        if i < 100:
            cnt += 1  # 100보다 작으면 모두 한수니까 더해주고
        elif list1[0]-list1[1] == list1[1]-list1[2]:
            cnt += 1  # x의 각 자리가 등차수열이면 한수니까 더해주고 아니면 귿그대로 반복문 위로
    return cnt

n = int(input())
print(a(n))