#include <iostream>
using namespace std;

int f(int n){
    if(n == 1 || n == 2){ return n; }
    return n + f(n - 2);
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int N;
    cin >> N;
    cout << f(N) << "\n";
}