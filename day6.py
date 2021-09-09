'''
a = int(input()) #5단계 마지막
b = []
for i in range(a):
    list1 = list(map(int, input().split()))
    avg = (sum(list1) - list1[0]) / list1[0]
    student = 0
    for k in (list1[1:]):
        if k > avg:
            student += 1
    b = b.append(student / list1[0] * 100)

for i in range(a):
    print('%0.3f%%' % b[i])


def total(n): # 6-1번
    return sum(n)
'''
'''
def d(n): #6-2번
   n = n + map(int,str(n)) # n자리수 들어오면 map함수로 각 자리수 나눠주고 int로 변환후 더해줌
   return n
a = [1]*10001 # 생성자를 탐색해줄 리스트 생성

for i in range(1,10001):
    a[i]=d(i)   # 생성자들을 리스트에 저장시켜줌
for i in range(1,10001): # 검색해서 없을경우 셀프 넘버이므로 그 넘버 출력력
    if i not in a:
        print(i)
'''

print(sum(map(int, str(123))))#
