#include <iostream>

using namespace std;

bool isPrime(int n) {
    // Check if n is less than 2
    if (n < 2) {
        return false;
    }
    
    // Loop from 2 to n-1 and check if n is divisible by any of them
    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    
    // If n is not divisible by any number between 2 and n-1, then it's a prime number
    return true;
}

int main() {
    // Read the input number from user
    int n;
    cout << "Enter a number: ";
    cin >> n;
    
    // Check if the input number is prime or not
    if (isPrime(n)) {
        cout << n << " is a prime number." << endl;
    } else {
        cout << n << " is not a prime number." << endl;
    }
    
    return 0;
}
