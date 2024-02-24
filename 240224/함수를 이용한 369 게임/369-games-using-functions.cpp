#include <iostream>
using namespace std;

bool is369(int n){
    while(n != 0){
        int remainder = n % 10;
        int arr[3] = { 3, 6, 9 };
        for(int e : arr){
            if(remainder == e){ return true; }
        }
        n /= 10;
    }
    return false;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int cnt = 0;
    for(int i{a};i <= b;i++){
        if(is369(i) || i % 3 == 0){ cnt++; }
    }
    cout << cnt << "\n";
    return 0;
}