#include <iostream>

using namespace std;

int N;
int rec(int n){
    if(n == 1){ return 2; }
    if(n == 2){ return 4; }
    return rec(n - 1) * rec(n - 2) % 100;
}
int main() {
    cin >> N;
    cout << rec(N) << "\n";
    return 0;
}