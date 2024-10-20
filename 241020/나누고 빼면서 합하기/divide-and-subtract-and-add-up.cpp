#include <iostream>
using namespace std;

int m;
int A[101];

void modifyM(){
    if(m % 2 != 0){
        m -= 1; return;
    }
    m /= 2; return;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n >> m;

    for(int i{1};i <= n;i++){
        cin >> A[i];
    }

    int sum{ 0 };
    while(m >= 1){
        sum += A[m];
        modifyM();
    }
    cout << sum << "\n";
    return 0;
}