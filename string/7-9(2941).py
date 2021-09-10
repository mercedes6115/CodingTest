a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alphabet = input()

for i in a:
    alphabet = alphabet.replace(i,' ')

print(len(alphabet))