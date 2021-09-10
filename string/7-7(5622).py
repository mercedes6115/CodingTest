dial_num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
count = 0
 # 번호당 알파벳이 지정되있으므로 묶음으로 리스트로 표현한다
A = input()

for i in range(len(A)):
    for j in dial_num:
        if A[i] in j:
            count += dial_num.index(j)+3
print(count)
