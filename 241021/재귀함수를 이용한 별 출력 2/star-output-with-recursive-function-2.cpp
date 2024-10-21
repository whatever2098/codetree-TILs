#include <iostream>
using namespace std;

void printStar(int n){
    for(int i{0};i < n;i++){
        cout << "* ";
    }
    cout << "\n";
}

void printStars(int n){
    if(n < 1){ return; }

    printStar(n);
    printStars(n - 1);
    printStar(n);
}
int main() {
    int n;
    cin >> n;
    printStars(n);
    return 0;
}