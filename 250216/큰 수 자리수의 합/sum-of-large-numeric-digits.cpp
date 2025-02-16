#include <iostream>
using namespace std;

int number_sum(int n){
    if(n == 0){ return 0; }
    return number_sum(n / 10) + n  % 10;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int a, b, c;
    cin >> a >> b >> c;

    cout << number_sum(a * b * c) << "\n";
}