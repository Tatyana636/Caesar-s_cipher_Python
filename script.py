a=open('z10.txt', 'r').readlines()
for i in range(len(a)):
    a[i]=a[i].strip()
    for j in range(len(a[i])):
       print(chr(ord(a[i][j])+i+1), end='')
    print()
