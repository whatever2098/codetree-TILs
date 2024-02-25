#include <iostream>
using namespace std;

int pow(int a, int b){
    int res = 1;
    while(b--){
        res *= a;
    }
    return res;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    cout << pow(a, b) << "\n";
    return 0;
}