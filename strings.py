n = input('enter a number')
L = list(n)
print(L)

L1 = list(map(int, L))
print(L1)
print(L1[-1]%2 == 0)
