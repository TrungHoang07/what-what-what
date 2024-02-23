'''
void sieve(int N) {
    bool isPrime[N+1];
    for(int i = 0; i <= N;++i) {
        isPrime[i] = true;
    }
    isPrime[0] = false;
    isPrime[1] = false;
    for(int i = 2; i * i <= N; ++i) {
         if(isPrime[i] == true) {
             // Mark all the multiples of i as composite numbers
             for(int j = i * i; j <= N; j += i)
                 isPrime[j] = false;
        }
    }
}
'''
from math import sqrt
n = int(input())
def sieve(n):
    isPrime = []
    for i in range(n+2):
        isPrime.append(i)
        isPrime[i] == True
    isPrime[0] == False
    isPrime[1] == False
    for i in range(2,sqrt(n+1)):
        if isPrime[i] ==  True:
            for j in range(i*i,n+1,i):
                isPrime[j] == False