from math import sqrt
n = int(input())
def isPrime():
    check = [True]*(n+1)
    check[0] = False
    check[1] = False
    for i in range(2,int(sqrt(n))+1):
        for j in range(i*i,n+1,i):
            check[j] = False
    for i in range(2, n+1):
        if(check[i]==True):
            print(i, end=' ')
isPrime()