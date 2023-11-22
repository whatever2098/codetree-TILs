#include <iostream>
using namespace std;

void PrintString(int input){
    while(input--){
        cout << "12345^&*()_" << "\n";
    }
}
int main() {
    int N;
    cin >> N;
    PrintString(N);
    return 0; 
}