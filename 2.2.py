from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
for i in range(5):
    for j in range(5):
        print(m[i][j],end=' ')
    print()
a = m[0][0]
for i in range(n):
    for j in range(n):
        if m[i][j] > a:
            a = m[i][j]
print(a)   