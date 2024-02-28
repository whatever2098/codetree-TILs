#include <iostream>
using namespace std;

bool isIntactNum(int n){
    if(n % 2 == 0 || n % 10 == 5) return false;
    if(n % 3 == 0 && n % 9 != 0) return false;
    return true;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int cnt{0};
    for(int i{a};i <= b;i++){
        if(isIntactNum(i)) cnt++;
    }
    cout << cnt << "\n";
    return 0;
}