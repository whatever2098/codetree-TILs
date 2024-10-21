#include <iostream>
using namespace std;

void print(int N){
    if(N < 1){ return; }

    cout << N << " ";
    print(N - 1);
    cout << N << " ";
}
int main() {
    int N;
    cin >> N;
    print(N);
    return 0;
}