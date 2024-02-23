n = int(input())
lst = list(map(int, input().split()))
for i in lst:
    max_l = lst.count(lst[0])
    if max_l < lst.count(i):
        max_l = lst.count(i)
print(max_l)