#include <iostream>
using namespace std;

void Print10Stars() {
    int N = 10;
    while(N--) {
        cout << "*";
    }
    cout << "\n";
}

int main() {
    int N = 5;
    while(N--){
        Print10Stars();
    }
    return 0;
}