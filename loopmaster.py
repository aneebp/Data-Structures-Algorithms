n= 11
symbol = "*"

for i in range(n):
    for j in range(i,n):
        print(' ',end=" ")
    for j in range(i-1):
        print(symbol, end=" ")
    for j in range(i):
        print(symbol, end=" ")
    print()
for i in range(n):
    for j in range(i):
        print(' ', end=" ")
    for j in range(i,n-1):
        print(symbol,end=" ")
    for j in range(i,n):
        print(symbol,end=' ')
    print()
