n = int(input())
lst = list(map(int, input().split()))
low = 0
high= n 
res = -1
k = int(input("Nhap vi tri cua so ma ban muon biet o trong list: "))
while low <= high:
    mid = low + int((high-low)/2)
    if lst[mid] == k:
        res = mid
        break
    elif lst[mid] < k:
        low = mid + 1
    elif lst[mid] > k:
        high = mid -1
print(res)

    
    