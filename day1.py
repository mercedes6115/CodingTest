'''

a, b = input().split() # 2단계 1번
a = int(a)
b = int(b)
-10000 <= a, b <= 10000

if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")


a= input()    # 2단계 2번
a = int(a)

0 <= a <= 100

if 90 <= a <= 100:
    print("A")
elif 80 <= a < 90 :
    print("B")
elif 70 <= a < 80:
    print("C")
elif 60 <= a < 70:
    print("D")
elif a < 69:
    print("F")


a= input()    # 2단계 3번
a = int(a)
1< a <=4000
if (a%4 == 0 and a% 400 ==0) or (a%4 == 0 and a%100 !=0):
    print("1")
else :
    print("0")

a= input()    # 2단계 4번
a = int(a)
b= input()
b = int(b)
a,b != 0

-1000 <= a,b <= 1000

if a>0 and b>0 :
    print("1")
if a<0 and b>0 :
    print("2")
if a<0 and b<0 :
    print("3")
if a>0 and b<0 :
    print("4")

H, M = map(int,input().split()) # 2단계 5번

if M >=45:
    print(H, M-45)
elif H>0 and M<45:
    print(H-1,M+15)
else:
    print(23,M+15)

'''

