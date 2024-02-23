lst = list(input())
lst.reverse()
sum = 0
for i in range(len(lst)-1,-1,-1):
    sum += int(lst[i])*(2**i)
print(sum)