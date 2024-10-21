#include <iostream>
using namespace std;

void print(int N){
    if(N < 1){ return; }

    print(N - 1);
    while(N--){
        cout << "*";
    }
    cout << "\n";
}

int main() {
    int N;
    cin >> N;
    print(N);
    return 0;
}