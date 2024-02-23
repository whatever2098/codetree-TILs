#include <iostream>
using namespace std;

void gcd(int n, int m){
    if(m == 0){ cout << n; return; }
    gcd(m, n % m);
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n, m;
    cin >> n >> m;
    gcd(n, m);
    return 0;
}