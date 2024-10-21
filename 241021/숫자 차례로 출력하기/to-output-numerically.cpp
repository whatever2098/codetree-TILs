#include <iostream>
using namespace std;

void firstPrint(int N){
    if(N < 1){ return; }

    firstPrint(N - 1);
    cout << N << " ";
}

void secondPrint(int N){
    if(N < 1){ return; }

    cout << N << " ";
    secondPrint(N - 1);
}

int main() {
    int N;
    cin >> N;

    firstPrint(N);
    cout << "\n";
    secondPrint(N);
    return 0;
}