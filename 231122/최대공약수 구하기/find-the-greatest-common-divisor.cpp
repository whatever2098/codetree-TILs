#include <iostream>
#include <algorithm>
using namespace std;

 void GreatestCommonDivisor(int n, int m){
    int dividing = max(n, m);
    int divisor = 0;
    for(int i = 1; i < min(n, m);i++){
        if(min(n, m) % i == 0) divisor = min(n, m) / i;
        else{ continue; }

        if(dividing % divisor == 0){
            cout << divisor << "\n";
            break;
        }
    }

 }
int main() {
    int n, m;
    cin >> n >> m;
    GreatestCommonDivisor(n, m);
    return 0;
}