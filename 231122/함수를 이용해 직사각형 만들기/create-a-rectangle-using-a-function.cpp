#include <iostream>
using namespace std;

void PrintSquare(int n, int m){
    while(n--) {
        for(int i = 0; i < m; i++){
            cout << "1";
        }
        cout << "\n";
    }
}
int main() {
    int n, m;
    cin >> n >> m;
    PrintSquare(n, m);
    return 0;
}