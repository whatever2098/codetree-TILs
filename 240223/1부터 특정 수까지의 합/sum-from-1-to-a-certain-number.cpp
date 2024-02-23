#include <iostream>
using namespace std;

int divideSum(int n){
    int sum = 0;
    while(n--){
        sum += (n + 1);
    }
    return sum / 10;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int quocient = divideSum(n);
    cout << quocient << '\n';
    return 0;
}