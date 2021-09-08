def d(n): #6-2번
    n = n + sum(list(map(int, str(n))))# n자리수 들어오면 map함수로 각 자리수 나눠주고 int로 변환후 더해줌
    return n
a = [1]*10001 # 생성자를 탐색해줄 리스트 생성

for i in range(0,10001):
    a[i]=d(i)   # 생성자들을 리스트에 저장시켜줌
for i in range(0,10001): # 검색해서 없을경우 셀프 넘버이므로 그 넘버 출력력
    if i not in a:
        print(i)