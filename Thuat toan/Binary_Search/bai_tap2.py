def bs(lst, n, k):
    l = 0
    h = n-1
    while(l<=h):
        mid = l+int((h-l)/2)
        if(lst[mid]==k):
            return "Y"
        elif (lst[mid]>k):
            h=mid-1
        else:
            l=mid+1
    return "N"
n = int(input())
lst = list(map(int, input().split()))
t = int(input())
l = []
for i in range(1,t+1):
    l.append(int(input()))
for i in l:
    print(bs(lst, n, i))