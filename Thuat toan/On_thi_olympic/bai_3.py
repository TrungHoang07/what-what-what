def swap_bin(lst): #Chuyển đổi số nhị phân sang số thực
    lst.reverse()
    sum = 0
    for i in range(len(lst)-1,-1,-1):
        sum += int(lst[i])*(2**i)
    return sum
a = list(input())
b = list(input())
sum = swap_bin(a) + swap_bin(b)

def toBinary(n): #Chuyển đổi số thực về số nhị phân
    if n > 1:
        toBinary(n//2)
    print(n % 2, end='')
toBinary(sum)


"""kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"""