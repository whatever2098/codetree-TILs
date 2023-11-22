#include <iostream>
using namespace std;

void PrintSquare(int n){
    int num = 0;
    for(int i = 0; i < n;i++){
        for(int j = 0; j < n;j++){
            num++;
            if(num != 10) cout << num << " ";
            else{ num = 1; cout<< num << " ";}
        }
        cout << "\n";
    }
}
int main() {
    int N;
    cin >> N;
    PrintSquare(N);
    return 0;
}