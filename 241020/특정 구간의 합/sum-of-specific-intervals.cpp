#include <iostream>
using namespace std;

int A[101];

int main() {
    // 여기에 코드를 작성해주세요.
    int n, m;
    cin >> n >> m;

    for(int i{1};i <= n;i++){
        cin >> A[i];
    }

    while(m--){
        int a1, a2;
        cin >> a1 >> a2;
        int sum{ 0 };
        for(int i{a1};i <= a2;i++){
                sum += A[i];
        }
        cout << sum << "\n";
    }
    return 0;
}