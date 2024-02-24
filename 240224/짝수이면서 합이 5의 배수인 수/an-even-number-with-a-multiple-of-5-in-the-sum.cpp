#include <iostream>
using namespace std;

bool isSumMul5(int n){
    int numOfDigitsIn10 = n / 10;
    int sum = n - numOfDigitsIn10 * 10 + numOfDigitsIn10;
    return n % 2 == 0 && sum % 5 == 0;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    cout << ((isSumMul5(n))? "Yes" : "No") << "\n"; //주의!
    return 0;
}