#include <iostream>
using namespace std;

int rec(int n, int m){
    if(n == 1){ return m; }
    if(n % 2 == 0){
        return rec(n / 2, m + 1);
    }
    return rec(n * 3 + 1, m + 1);
}

int main(){
    ios_base::sync_with_stdio(0);
    cout.tie(0); cin.tie(0);

    int N;
    cin >> N;
    cout << rec(N, 0) << "\n";
}