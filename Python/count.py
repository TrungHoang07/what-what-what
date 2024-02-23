#nhập dữ liệu đầu vào của đề bài
n = int(input())
lst = list(map(int, input().split()))
#xóa phần tử trùng nhau trong lst
arr = list(dict.fromkeys(lst))
#tạo 1 list rỗng
l = []
#duyệt từng phần tử trong arr, tạo biến temp đếm số lần xuất hiện của các phần tử trong lst
for i in arr:
    temp = lst.count(i)
    #thêm số lần xuất hiện của các phần tử trong lst ( temp ) vào l 
    l.append(temp)
#xóa phần tử trùng nhau trong l
ll = list(dict.fromkeys(l))
#đếm số lần xuất hiện của phần tử lớn nhất trong l
ma = l.count(max(ll))
#Nếu ma = 1 thì in ra vị phần tử có vị trí tương tự phần tử lớn nhất của l 
if ma == 1:
	print(str(arr[l.index(max(l))]), max(l))
#Nếu ma > 1 thì in ra giá trị lớn nhất của arr ( hoặc lst ) và của l ( hoặc ll )
elif ma > 1:
	print(str(max(arr)), max(ll))