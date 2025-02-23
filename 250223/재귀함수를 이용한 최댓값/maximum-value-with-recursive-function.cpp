#include <iostream>
using namespace std;

int maxNum{ 0 };

int max(int n){
    if(n == 0){ return maxNum; }
    int num;
    cin >> num;
    if(num > maxNum) maxNum = num;
    return max(--n);
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n;
    cin >> n;
    cout << max(n) << "\n";
}