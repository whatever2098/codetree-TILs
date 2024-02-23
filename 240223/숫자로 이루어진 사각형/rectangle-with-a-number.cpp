#include <iostream>
using namespace std;

void rec(int n){
    int number = 1;
    for(int i{0};i < n;i++){
        for(int j{0};j < n;j++){
            if(number == 10){ number = 1; }
            cout << number << " ";
            number++;
        }
        cout << "\n";
    }
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    rec(n);
    return 0;
}