n = int(input())
lst = list(map(int, input().split()))
lmin = lst[0]
lmax = lst[0]
for i in lst:
    if lmin > i:
        lmin = i
    if lmax < i:
        lmax = i
for i in range(n):
    if lst[i] == lmax:
        pot2 = i
        break
    if lst[i] == lmin:
        pot1 = i
        break
print(lmin,pot1+1,lmax,pot2+1)