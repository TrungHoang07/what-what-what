def bs(n, a, k):
    l = 0
    h = n-1
    while(l<=h):
        mid = l+int((h-l)/2)
        if(a[mid]==k):
            return 1
        elif (a[mid]>k):
            h=mid-1
        else:
            l=mid+1
    return 0

inp = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for k in b:
    print(bs(len(a), a, k), end = "")