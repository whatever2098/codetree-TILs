#include <iostream>

using namespace std;

int N;

int rec(int n, int m){
    if(n == 1){ return m; }
    if(n % 2 == 0){
        return rec(n / 2, m + 1);
    }
    return rec(n / 3, m + 1);
}
int main() {
    cin >> N;
    cout << rec(N, 0)<< "\n";
    return 0;
}