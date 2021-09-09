



a = input()                      # 테스트 케이스를 입력받고
for i in range(int(a)):          # 테스트 케이스만큼 반복시켜주기 위한 반복문
    b , c = input().split(" ")    # map함수를 이용하여 b에는 반복 횟수, c에는 문자열을 받고
    count = len(c)                 # 인덱싱을 위해 문자열의 길이를 구해준다음
    for j in range(count):         # 문자열 각 요소에 접근하기 위한 반복문
        print(c[j]*int(b), end="")   # 문자열 요소마다 반복 횟수만큼 문자열을 반복시켜준다.
    print()


