import sys
'''
# 5-4번
array_list = []
array_set = set()
for i in range (10):
    array_list.append(int(sys.stdin.readline()))
    array_set.add(array_list[i]%42)

print(len(array_set))


a = int(input())
b = list(map(int,input().split()))

sum=0
for i in b:
    sum+=(i/max(b))*100
print(sum/a)


a=int(input())
for i in range (a):
    cnt=0
    sum=0
    list1=list(input())
    for i in range(len(list1)):
        if(list1.pop() == "0"):
            cnt+=1
        else:
            cnt=0
        sum+=cnt
    print(sum)

'''
a = int(input())
b = []
for i in range(a):
    list1 = list(map(int,input().split()))
    avg = (sum(list1)-list1[0])/list1[0]
    student = 0
    for k in (list1[1:]):
        if k > avg :
            student += 1
    b = b.append(student/list1[0]*100)

for i in range(a):
    print('%0.3f%%' % b[i])

