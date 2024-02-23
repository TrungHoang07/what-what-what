h = int(input("Nhập chiều dài: "))
w = int(input("Nhập chiều rộng: "))
while h >= w:
    for i in range(1,h+1):
        for j in range(1,w+1):
            print("*", end = " ")
        print()
    break
else: print("Không hợp lệ")